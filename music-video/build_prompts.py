#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_prompts.py
-----------------
منبع حقیقتِ پروژه فایل prompts.json است.
این اسکریپت بلوک‌های تکرارشونده ({S}, {M}, {SCHOOL} ...) را داخل پرامپت‌ها باز می‌کند
و خروجی آماده‌ی کپی/پیست می‌سازد:

    music-video/03-shot-prompts.md      سند کامل پلان‌به‌پلان (فارسی + پرامپت انگلیسی)
    music-video/out/SHEETS/<ID>.txt     پرامپت شیت‌های رفرنس (Qwen-Image-2.1)
    music-video/out/SHOTS/<ID>.image.txt    پرامپت فریم اول (Qwen-Image-2.1)
    music-video/out/SHOTS/<ID>.video.txt    پرامپت ویدیو (موتور پیشنهادی)
    music-video/out/NEGATIVE.txt        نگتیو پرامپت مشترک

اجرا:  python3 music-video/build_prompts.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "prompts.json"
OUT = ROOT / "out"
DOC = ROOT / "03-shot-prompts.md"
SHEET_DOC = ROOT / "01-character-sheets.md"
SHEET_INTRO = ROOT / "_partials" / "01-intro.md"

BLOCK_LABELS = {
    "S": "خواننده — قفل هویت",
    "WA": "لباس A (کل کلیپ)",
    "WB": "لباس B (سکانس باران)",
    "M": "مادر — گل‌بانو، ۵۲ ساله",
    "K": "پسر — یاسین، ۹ ساله",
    "BAG": "پراپ — کیف مدرسه",
    "NOTE": "پراپ — دفتر",
    "BELL": "پراپ — زنگ برنجی",
    "STONE": "پراپ — سنگ قبر (تخت، روی زمین)",
    "SCHOOL": "لوکیشن — حیاط مدرسه",
    "CLASS": "لوکیشن — کلاس درس",
    "HOME": "لوکیشن — خانه",
    "CEM": "لوکیشن — قبرستان تپه‌ای",
    "ALLEY": "لوکیشن — کوچه",
    "NOW": "گرید — جهانِ «حالا»",
    "MEM": "گرید — جهانِ «خاطره»",
    "NEG": "نگتیو پرامپت مشترک",
}

TOKEN_RE = re.compile(r"\{([A-Z_]+)\}")

CAT_LABEL = {
    "A": "[A] اجرای خواننده — لب‌خوانی / حضور مستقیم",
    "B": "[B] تصویرسازی محض — بدون خواننده",
    "C": "[C] خواننده داخل صحنه — شاهدِ خاموش",
}


def expand(text: str, blocks: dict[str, str], seen: set[str] | None = None) -> str:
    """توکن‌های {X} را بازگشتی باز می‌کند."""
    if not isinstance(text, str):
        return text
    seen = seen or set()

    def sub(match: re.Match) -> str:
        key = match.group(1)
        if key not in blocks:
            return match.group(0)
        if key in seen:
            return match.group(0)  # جلوگیری از حلقه
        return expand(blocks[key], blocks, seen | {key})

    return TOKEN_RE.sub(sub, text)


def used_tokens(text: str, blocks: dict[str, str]) -> list[str]:
    if not isinstance(text, str):
        return []
    return sorted({t for t in TOKEN_RE.findall(text) if t in blocks})


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not DATA.exists():
        print(f"prompts.json پیدا نشد: {DATA}", file=sys.stderr)
        return 1

    data = json.loads(DATA.read_text(encoding="utf-8"))
    blocks: dict[str, str] = data["blocks"]
    project = data["project"]
    sheets = data.get("sheets", [])
    shots = data.get("shots", [])

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    neg = expand("{NEG}", blocks)
    write(OUT / "NEGATIVE.txt", neg)

    # ---------- شیت‌های رفرنس ----------
    for sh in sheets:
        body = (
            f"### {sh['id']} — {sh['title_fa']}\n"
            f"# mode: {sh['mode']}\n"
            f"# size: {sh['size']}\n\n"
            f"--- PROMPT ---\n{expand(sh['prompt'], blocks)}\n\n"
            f"--- NEGATIVE ---\n{expand(sh.get('negative', '{NEG}'), blocks)}\n"
        )
        write(OUT / "SHEETS" / f"{sh['id']}.txt", body)

    # ---------- سند شیت‌ها (۰۱) ----------
    sm: list[str] = []
    B = sm.append
    if SHEET_INTRO.exists():
        B(SHEET_INTRO.read_text(encoding="utf-8").rstrip())
        B("")
    for key, val in blocks.items():
        if key == "NEG":
            continue
        B(f"**`{{{key}}}` — {BLOCK_LABELS.get(key, key)}**\n")
        B("```text")
        B(val)
        B("```\n")
    B("---\n")
    B("## پرامپت شیت‌ها (آماده‌ی کپی)\n")
    B("همه‌ی توکن‌ها باز شده‌اند. نسخه‌ی `.txt` هرکدام در `out/SHEETS/` هم هست.\n")

    sec = None
    for sh in sheets:
        kind = sh["id"].split("-")[0]
        label = {"CS": "کاراکترها", "PS": "پراپ‌ها", "LS": "لوکیشن‌ها"}.get(kind, kind)
        if kind != sec:
            sec = kind
            B(f"\n### {label}\n")
        B(f"#### {sh['id']} · {sh['title_fa']}\n")
        B(f"- **حالت:** {sh['mode']}")
        B(f"- **اندازه:** `{sh['size']}`")
        if sh.get("note_fa"):
            B(f"- **نکته:** {sh['note_fa']}")
        B("")
        B("```text")
        B(expand(sh["prompt"], blocks))
        B("```\n")
    B("\n### نگتیو پرامپت مشترک\n")
    B("```text")
    B(neg)
    B("```")
    write(SHEET_DOC, "\n".join(sm))

    # ---------- پلان‌ها ----------
    for s in shots:
        write(OUT / "SHOTS" / f"{s['id']}.image.txt", expand(s["image"], blocks))
        if s.get("image_last"):
            write(OUT / "SHOTS" / f"{s['id']}.image_last.txt", expand(s["image_last"], blocks))
        write(OUT / "SHOTS" / f"{s['id']}.video.txt", expand(s["video"], blocks))
        if s.get("end_frame"):
            write(OUT / "SHOTS" / f"{s['id']}.end_frame.txt", expand(s["end_frame"], blocks))

    # ---------- سند مارک‌داون ----------
    md: list[str] = []
    A = md.append
    A(f"# ۰۳ — پرامپت پلان‌به‌پلان · «{project['title_fa']}»\n")
    A("> این فایل **به‌صورت خودکار** از `prompts.json` ساخته می‌شود.")
    A("> دست نزن؛ اگر خواستی چیزی عوض کنی `prompts.json` را ویرایش کن و دوباره اجرا کن:")
    A("> `python3 music-video/build_prompts.py`\n")
    A(f"- نسبت تصویر مستر: **{project['master_ratio']}** · رزولوشن: **{project['master_res']}** · "
      f"نرخ فریم: **{project['fps']}fps** · زمان هدف: **{project['runtime_target']}**")
    A(f"- کات عمودی: {project['alt_ratio']}")
    A("- **نگتیو پرامپت مشترک** برای همه‌ی تصاویر در انتهای همین فایل و در `out/NEGATIVE.txt`.\n")

    # جدول خلاصه
    A("## جدول خلاصه‌ی پلان‌ها\n")
    A("| # | تایم‌کد | ثانیه | دسته | عنوان | موتور پیشنهادی |")
    A("|---|---------|-------|------|-------|----------------|")
    for s in shots:
        A(f"| {s['id']} | {s['tc']} | {s['dur']} | {s['cat']} | {s['title_fa']} | {s['engine']} |")
    A("")
    total = sum(int(x["dur"]) for x in shots)
    A(f"**جمع کل: {len(shots)} پلان · {total} ثانیه ≈ {total//60}:{total%60:02d}**\n")

    counts = {"A": 0, "B": 0, "C": 0}
    for s in shots:
        counts[s["cat"]] = counts.get(s["cat"], 0) + 1
    A(f"توزیع: {counts.get('A',0)} پلان [A] اجرای خواننده · "
      f"{counts.get('B',0)} پلان [B] تصویرسازی محض · "
      f"{counts.get('C',0)} پلان [C] خواننده داخل صحنه\n")
    A("---\n")

    current_seq = None
    for s in shots:
        if s["seq"] != current_seq:
            current_seq = s["seq"]
            A(f"\n## سکانس {current_seq}\n")

        A(f"### {s['id']} · {s['title_fa']}  `{s['tc']}` · {s['dur']}s")
        A(f"**{CAT_LABEL.get(s['cat'], s['cat'])}**\n")
        A(f"- **موتور:** {s['engine']}  ·  **جایگزین:** {s['engine_alt']}")
        A(f"- **چرا:** {s['why_fa']}")
        A(f"- **نسبت:** {s['ratio']}  ·  **رفرنس‌ها:** {'، '.join(s['refs'])}")
        if s.get("audio_fa"):
            A(f"- **صدا:** {s['audio_fa']}")
        if s.get("note_fa"):
            A(f"- **نکته:** {s['note_fa']}")
        A("")

        A("**۱) فریم اول — Qwen-Image-2.1**\n")
        A("```text")
        A(expand(s["image"], blocks))
        A("```\n")

        if s.get("image_last"):
            A("**۱ب) فریم آخر — Qwen-Image-2.1**\n")
            A("```text")
            A(expand(s["image_last"], blocks))
            A("```\n")

        A(f"**۲) ویدیو — {s['engine']}**\n")
        A("```text")
        A(expand(s["video"], blocks))
        A("```\n")

        if s.get("end_frame"):
            A("**۲ب) فریم پایانی برای اینترپولیشن (LTX `last_frame_image`)**\n")
            A("```text")
            A(expand(s["end_frame"], blocks))
            A("```\n")

        toks = used_tokens(s["image"], blocks) + used_tokens(s["video"], blocks)
        if toks:
            A(f"<sub>بلوک‌های استفاده‌شده: {', '.join(sorted(set(toks)))}</sub>\n")
        A("---")

    A("\n## نگتیو پرامپت مشترک (همه‌ی تصاویر Qwen)\n")
    A("```text")
    A(neg)
    A("```")

    write(DOC, "\n".join(md))

    n_files = sum(1 for _ in OUT.rglob("*.txt"))
    print(f"✓ {SHEET_DOC.relative_to(ROOT.parent)}")
    print(f"✓ {DOC.relative_to(ROOT.parent)}")
    print(f"✓ {n_files} فایل متنی در {OUT.relative_to(ROOT.parent)}/")
    print(f"✓ {len(sheets)} شیت رفرنس · {len(shots)} پلان · {total} ثانیه")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
