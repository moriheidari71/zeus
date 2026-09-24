# ۰۳ — پرامپت پلان‌به‌پلان · «نَزنید زنگ»

> این فایل **به‌صورت خودکار** از `prompts.json` ساخته می‌شود.
> دست نزن؛ اگر خواستی چیزی عوض کنی `prompts.json` را ویرایش کن و دوباره اجرا کن:
> `python3 music-video/build_prompts.py`

- نسبت تصویر مستر: **16:9** · رزولوشن: **768P/720p برای همه · 2K فقط برای دو پلان اصلی** · نرخ فریم: **24fps** · زمان هدف: **01:02 (با حذف S04 → 00:58)**
- کات عمودی: 9:16 (کات عمودی)
- **نگتیو پرامپت مشترک** برای همه‌ی تصاویر در انتهای همین فایل و در `out/NEGATIVE.txt`.

## جدول خلاصه‌ی پلان‌ها

| # | تایم‌کد | ثانیه | دسته | عنوان | موتور پیشنهادی |
|---|---------|-------|------|-------|----------------|
| S01 | 00:00–00:06 | 6 | B | کیف نو در تاریکی | LTX-2.5 Fast · 720p · بدون صدا |
| S02 | 00:06–00:14 | 8 | A | ★ او در چارچوب در | MiniMax H3 768P · reference-to-video |
| S03 | 00:14–00:20 | 6 | C | کوچه — بچه‌ها می‌گذرند، او ایستاده | Seedance 2.0 · 1080p |
| S04 | 00:20–00:24 | 4 | B | دست روی طناب زنگ | MiniMax H3 768P |
| S05 | 00:24–00:31 | 7 | A+C | ★★ حیاط خالی — دستِ بالا، «نزنید» | MiniMax H3 · 768P برای تست، فاینال 2K |
| S06 | 00:31–00:37 | 6 | B | قبرستانِ نمکی — سنگ و کیف | LTX-2.5 Fast · 720p · بدون صدا |
| S07 | 00:37–00:44 | 7 | C | ★ زانو زده، سنگ را می‌شوید | MiniMax H3 768P · reference-to-video |
| S08 | 00:44–00:49 | 5 | B | ★ انگشت روی خط، قطره | MiniMax H3 768P |
| S09 | 00:49–00:56 | 7 | A | ★★ کلوزآپ — چشم‌های خیس | MiniMax H3 · 768P برای تست، فاینال 2K |
| S10 | 00:56–01:02 | 6 | B | ★★ زنگ می‌خورد — حیاط پر می‌شود — پسر برمی‌گردد | Seedance 2.0 · 1080p · multi-shot |

**جمع کل: 10 پلان · 62 ثانیه ≈ 1:02**

توزیع: 2 پلان [A] اجرای خواننده · 5 پلان [B] تصویرسازی محض · 2 پلان [C] خواننده داخل صحنه

---


## سکانس ۱ — «بوی کیف و کتاب نو میاید»

### S01 · کیف نو در تاریکی  `00:00–00:06` · 6s
**[B] تصویرسازی محض — او در قاب نیست**

- **موتور:** LTX-2.5 Fast · 720p · بدون صدا  ·  **جایگزین:** MiniMax H3 768P
- **چرا:** ارزان‌ترین پلان ممکن: بدون چهره، بدون آدم، فقط نور. LTX Fast در 720p پایین‌ترین قیمت هر ثانیه را دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01 (پنل خانه)
- **صدا:** میوت کامل. فقط مقدمه‌ی آهنگ.
- **نکته:** با LTX هر دو فریم اول و آخر را بده (image + last_frame_image) تا حرکتِ نور دقیق کنترل شود. generate_audio را خاموش کن — ارزان‌تر است.

**۱) فریم اول — Qwen-Image-2.1**

```text
Extreme close-up in near-darkness. the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film stands upright on a woven palm-frond mat beside a folded school shirt, inside the HOME: a modest southern Iranian room, a woven palm-frond mat over a bare cement floor, whitewashed plaster walls, one deep shaded window opening with a thin cloth curtain lifting in the sea breeze, a low niche holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a large unglazed clay water jar in the corner. A single narrow blade of early light enters from the edge of the cloth curtain and lies across the brass buckle. Fine dust hangs in the beam. Everything outside the beam falls to deep warm black. Macro 100mm lens, extremely shallow depth of field, focus on the buckle. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast · 720p · بدون صدا**

```text
Locked-off macro shot, the camera does not move for the entire clip. Over six seconds the narrow blade of light creeps slowly across the satchel from the buckle towards the stitched edge, widening slightly and warming from pale grey to soft amber. Dust motes drift lazily through the beam, a few catching the light and flaring for an instant. Nothing else in the frame moves, no people, no hands. Preserve the exact shape, colour and stitching of the satchel. Silent plate, no audio needed.
```

**۲ب) فریم پایانی برای اینترپولیشن (LTX `last_frame_image`)**

```text
The same macro frame, the blade of light now wider and warmer and fully across the satchel, the rest of the room still dark.
```

<sub>بلوک‌های استفاده‌شده: BAG, HOME, NOW</sub>

---
### S02 · ★ او در چارچوب در  `00:06–00:14` · 8s
**[A] می‌خواند — لب‌خوانی رو به دوربین**

- **موتور:** MiniMax H3 768P · reference-to-video  ·  **جایگزین:** Seedance 2.0 (i2v + @Audio)
- **چرا:** اولین بار که چهره و لباسش را می‌بینیم و اولین لب‌خوانی. H3 تا ۹ رفرنس می‌گیرد و قفل هویتش از همه بهتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل نور سوم)، LS-01 (پنل خانه)
- **صدا:** میوت در تدوین.
- **نکته:** در H3 رفرنس‌ها را با role=reference_image بفرست و در متن بنویس: the woman is the person in the reference images.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium shot from inside the dark room looking out. the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her stands in the bright doorway of the HOME: a modest southern Iranian room, a woven palm-frond mat over a bare cement floor, whitewashed plaster walls, one deep shaded window opening with a thin cloth curtain lifting in the sea breeze, a low niche holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a large unglazed clay water jar in the corner, holding the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film flat against her chest with both arms. The doorway blows out to hot white behind her, so she reads as a near-silhouette with only enough bounce off the white walls to hold her eyes and the embroidery of her dress. Her shawl edge lifts in the sea breeze. She looks down at the satchel, not at camera. 35mm lens, shallow depth of field, the dark room framing her. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 768P · reference-to-video**

```text
An almost imperceptible push in over the full eight seconds, no more than eight percent. She stands in the doorway and does not walk in. She sings the opening line quietly, the mouth articulating clearly and naturally, small breaths between phrases, then lifts her eyes from the satchel and looks out past the camera. Her arms stay wrapped around the satchel throughout. The shawl ends and the loose sleeves move continuously in the breeze. Keep her face, shawl, white dress and the satchel exactly as in the reference images. Soundscape: a sea breeze through a doorway, a cloth curtain, distant gulls, a far-off motorcycle. No music.
```

<sub>بلوک‌های استفاده‌شده: BAG, HOME, NOW, S, WA</sub>

---

## سکانس ۲ — «نزنید زنگ و تا بچم بیاید»

### S03 · کوچه — بچه‌ها می‌گذرند، او ایستاده  `00:14–00:20` · 6s
**[C] بازی می‌کند — در صحنه هست ولی نمی‌خواند**

- **موتور:** Seedance 2.0 · 1080p  ·  **جایگزین:** MiniMax H3 768P (ref2v)
- **چرا:** چند آدمِ متحرک + قفل هویت یک نفر + امکان دو شات در یک رندر. تنها جایی که Seedance واقعاً صرف می‌کند.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01 → @Image1، LS-01 (پنل کوچه) → @Image2
- **صدا:** همهمه‌ی بچه‌ها در میکس فقط ۱۵٪ باز.
- **نکته:** قانون: هیچ بچه‌ای به او نگاه نمی‌کند. او در آن لحظه نیست، در حافظه‌ی آن لحظه است.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide shot down the ALLEY: a narrow lane in a Gulf coastal town between houses of coral stone rendered in flaking white and pale ochre, turquoise-painted steel doors, one low wind-catcher tower above the rooftops, hard palm-frond shadows striping the sand-dusted ground in the late morning. Six or seven primary-school children in uniform, seen mostly from behind, walk away from camera towards a turquoise gate at the far end, satchels swinging. In the exact centre of the lane, facing camera and perfectly still, stands the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her. The children flow past her on both sides without looking at her. Hard palm-frond shadows stripe the sand-dusted ground. 35mm lens, deep focus. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — Seedance 2.0 · 1080p**

```text
@Image1 is the woman: keep her face, shawl, white dress and build identical to it. @Image2 is the location. Shot 1, zero to four seconds: a static wide down the lane, the children walking away towards the gate, satchels swinging, one child skipping. The woman stands motionless in the centre facing camera, the only still thing in the frame, her shawl and sleeves moving in the wind. Shot 2, four to six seconds: cut to a low shot at child height as the last children pass close by her, her white hem and the palm shadows in frame. Camera locked off in both shots, no handheld, no push, no pan. Bleached hazy daylight, LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon. Audio: footsteps on grit, children's voices far off and unintelligible, wind. No music.
```

<sub>بلوک‌های استفاده‌شده: ALLEY, NOW, S, WA</sub>

---
### S04 · دست روی طناب زنگ  `00:20–00:24` · 4s
**[B] تصویرسازی محض — او در قاب نیست**

- **موتور:** MiniMax H3 768P  ·  **جایگزین:** LTX-2.5 Fast (اگر پلتفرمت ۴ ثانیه می‌دهد)
- **چرا:** کوتاه‌ترین پلان کلیپ. H3 از ۴ ثانیه شروع می‌شود، پس ارزان‌ترین راه همین است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01 (پنل حیاط)
- **صدا:** سکوتِ عمدی. زنگ اینجا نباید به صدا دربیاید.
- **نکته:** این پلان و S10 یک جمله‌ی بصری‌اند: «نزنید» … و بعد زده می‌شود. اگر بودجه تنگ است، این تنها پلانی است که می‌توانی حذف کنی (کلیپ می‌شود ۰۰:۵۸).

**۱) فریم اول — Qwen-Image-2.1**

```text
Tight shot. the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a turquoise-painted steel door, green patina in the grooves, the clapper visible inside hangs from its hemp rope beside a turquoise-painted steel door in the corner of the SCHOOL: a small school in a Persian Gulf coastal town, a courtyard of pale sand-coloured cement tiles bleached by the sun, low walls of coral stone rendered in flaking white and painted sun-faded turquoise to waist height, two tall date palms throwing hard ragged shadows across the yard, a single flagpole, a one-storey bone-white plastered building with steel-framed windows and a deep shaded arcade, and a wide turquoise-painted metal double gate. An old man's weathered hand, sleeve of a pale grey work shirt, enters from the right edge of frame and reaches for the rope, the fingers not yet closed around it. Hard hazy daylight, a palm shadow cutting across the wall behind. 85mm lens, shallow focus on the bell, the hand slightly soft. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 768P**

```text
Static locked-off shot. Over four seconds the weathered hand moves the last few centimetres towards the hemp rope and the fingers begin to close around it, slowing as they touch. The clip ends exactly at the moment of contact, before any pull. The rope sways a millimetre. The bell does not ring and does not swing. Nothing else moves. Preserve the exact shape, patina and rope of the bell. Soundscape: an empty courtyard, wind, the creak of rope fibre. Absolutely no bell sound.
```

<sub>بلوک‌های استفاده‌شده: BELL, NOW, SCHOOL</sub>

---
### S05 · ★★ حیاط خالی — دستِ بالا، «نزنید»  `00:24–00:31` · 7s
**[A+C] هم می‌خواند هم بازی می‌کند**

- **موتور:** MiniMax H3 · 768P برای تست، فاینال 2K  ·  **جایگزین:** Seedance 2.0
- **چرا:** اوج کلیپ و تنها پلانی که هم می‌خواند و هم بازی می‌کند. یکی از دو پلانی است که ارزش ۲K دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل نور اول)، CS-03 (پنل باد)، LS-01 (پنل حیاط)
- **صدا:** اکو قدم‌ها در حیاط خالی، بعد سکوت.
- **نکته:** اگر مدل آدم اضافه کرد، رندر را دور بریز. «completely empty, absolutely no other people» را سه بار در پرامپت تصویر تکرار کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
High wide shot from the roof of the arcade looking down into the completely empty courtyard of the SCHOOL: a small school in a Persian Gulf coastal town, a courtyard of pale sand-coloured cement tiles bleached by the sun, low walls of coral stone rendered in flaking white and painted sun-faded turquoise to waist height, two tall date palms throwing hard ragged shadows across the yard, a single flagpole, a one-storey bone-white plastered building with steel-framed windows and a deep shaded arcade, and a wide turquoise-painted metal double gate. the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her is small in the centre of the pale bleached tiles, alone, caught mid-stride moving towards the corner where the bell hangs, one arm raised high with the palm open in a stop gesture, the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film still clutched in the other hand. Her white dress is the brightest thing in the frame. Two hard palm shadows cut across the empty tiles. Absolutely no other people anywhere. 24mm lens, deep focus. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 · 768P برای تست، فاینال 2K**

```text
The camera holds high and static for the whole clip. Over seven seconds the woman takes four or five urgent steps towards the far corner, her raised arm staying up, the white dress and shawl streaming behind her, then she slows and stops dead in the middle of the empty courtyard and the raised arm falls slowly to her side. She stands there, very small in the frame, and does not move again. She is singing throughout, the mouth clearly articulating even at this distance. Keep her white dress, shawl and build exactly as in the reference images. The courtyard must stay completely empty, no other people at any point. Soundscape: running footsteps echoing off courtyard walls, one sharp breath, then wind and total emptiness. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: BAG, NOW, S, SCHOOL, WA</sub>

---

## سکانس ۳ — «نوشتن اسمتو بر روی سنگت»

### S06 · قبرستانِ نمکی — سنگ و کیف  `00:31–00:37` · 6s
**[B] تصویرسازی محض — او در قاب نیست**

- **موتور:** LTX-2.5 Fast · 720p · بدون صدا  ·  **جایگزین:** MiniMax H3 768P
- **چرا:** منظره‌ی ساکن بدون چهره. فقط باد حرکت می‌کند — ارزان‌ترین ممکن.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-02، PS-01
- **صدا:** باد خالص — نقطه‌ی تنفس کلیپ.
- **نکته:** generate_audio را خاموش کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Low wide shot almost at ground level on the salt flats of the CEMETERY: a graveyard on the salt flats at the edge of a Gulf coastal town, flat unpolished stone slabs laid directly onto pale bone-white salt-crusted earth in uneven rows, dry thorn scrub, one leaning half-dead date palm, a low broken wall, and the flat silver line of the sea far behind under a bleached hazy sky. the GRAVE: an Iranian Muslim grave, a flat unpolished pale stone slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut white stems, salt-crusted bone-white earth around it lies in the foreground, pale and new against the bone-white crusted earth. the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film stands upright on the salt immediately beside it, the only warm colour in the whole frame. Rows of older slabs recede behind, one leaning half-dead date palm, and the flat silver line of the sea far away under a bleached haze. No people. 35mm lens, deep focus, level horizon. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast · 720p · بدون صدا**

```text
Locked-off low wide shot, the camera does not move at all for six seconds. Only the wind is alive: dry thorn scrub shivers, a thin veil of salt dust lifts off the crust and travels across the frame, the dead palm fronds rattle, and a gust lifts the satchel's flap and lets it fall closed again. No people, no animals enter the frame. The grave must stay a flat slab lying on the ground, never an upright headstone. Silent plate, no audio needed.
```

<sub>بلوک‌های استفاده‌شده: BAG, CEM, NOW, STONE</sub>

---
### S07 · ★ زانو زده، سنگ را می‌شوید  `00:37–00:44` · 7s
**[C] بازی می‌کند — در صحنه هست ولی نمی‌خواند**

- **موتور:** MiniMax H3 768P · reference-to-video  ·  **جایگزین:** Seedance 2.0
- **چرا:** تعامل فیزیکی با آب + قفل چهره و لباس. H3 هم فیزیک مایع و هم هویت را با هم نگه می‌دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل نور دوم)، CS-03، LS-02
- **صدا:** صدای آب روی سنگ — نزدیک و خیس. بهترین لایه‌ی صوتی کلیپ.
- **نکته:** او اینجا نمی‌خواند. قطعِ لب‌خوانی وسط کلیپ، ریتم بصری می‌سازد.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium shot, camera low, almost at ground level. the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her kneels beside the GRAVE: an Iranian Muslim grave, a flat unpolished pale stone slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut white stems, salt-crusted bone-white earth around it on the salt flat of the CEMETERY: a graveyard on the salt flats at the edge of a Gulf coastal town, flat unpolished stone slabs laid directly onto pale bone-white salt-crusted earth in uneven rows, dry thorn scrub, one leaning half-dead date palm, a low broken wall, and the flat silver line of the sea far behind under a bleached hazy sky, seen in three-quarter profile. She tips a small green plastic watering can over the slab, a thin ribbon of water just beginning to fall, her other palm flat on the stone. Her white sleeve is already dark with water and the hem of her dress rests in the salt dust. Hard raking low sun from the side, wind lifting her shawl. 35mm lens, shallow focus on her, the rows of slabs soft behind. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 768P · reference-to-video**

```text
Static low shot, the camera does not move. Over seven seconds she pours the water slowly across the stone, the thin stream spreading into a bright sheet that runs into the carved border and darkens the slab, then she sets the can down and wipes the wet surface with her flat palm in two slow passes, front to back, the way you would wipe a child's face. She stays kneeling. At the end she stops with her hand flat on the stone and lowers her head. She does not sing in this shot and does not look at camera. Keep her face, shawl and white dress exactly as in the reference images. The grave must remain a flat slab on the ground. Soundscape: water poured onto stone, a wet palm dragging across it, salt-flat wind, one distant gull. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: CEM, NOW, S, STONE, WA</sub>

---

## سکانس ۴ — «دلوم تنگه واسه خط قشنگت»

### S08 · ★ انگشت روی خط، قطره  `00:44–00:49` · 5s
**[B] تصویرسازی محض — او در قاب نیست**

- **موتور:** MiniMax H3 768P  ·  **جایگزین:** LTX-2.5 Fast (۶ ثانیه)
- **چرا:** فیزیکِ قطره و پخش‌شدنِ جوهر در کاغذ — H3 در شبیه‌سازی فیزیکی از بقیه جلوتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01 (پنل خانه)، CS-01 (فقط برای رنگ پوست دست)
- **صدا:** یک نفسِ بریده، خیلی کم.
- **نکته:** پلان کلیدی مصرع «خط قشنگت». خطِ واقعی را در پست کامپوزیت کن — هیچ مدلی خط فارسی را درست نمی‌نویسد.

**۱) فریم اول — Qwen-Image-2.1**

```text
Overhead macro. the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections lies open on a woven palm-frond mat inside the HOME: a modest southern Iranian room, a woven palm-frond mat over a bare cement floor, whitewashed plaster walls, one deep shaded window opening with a thin cloth curtain lifting in the sea breeze, a low niche holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a large unglazed clay water jar in the corner, both pages covered in rows of childish handwriting, deliberately soft and out of focus so no word is legible. One woman's index finger with a henna-darkened tip rests at the start of a line, about to trace it. Soft shaded light from a deep window opening on the left. 100mm macro lens, shallow depth of field, focus on the fingertip and the paper texture. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 768P**

```text
Locked-off overhead macro, no camera movement. Over five seconds the fingertip travels very slowly along one line of writing from right to left, barely touching the paper, and stops halfway. It hovers, trembling. Then a single tear drops onto the page beside the finger and the paper darkens in a slowly spreading circle, the blue ink at its edge blooming and feathering outward into the wet fibres. The finger does not move again. No face enters the frame. Keep the handwriting soft and unreadable throughout. Soundscape: a single unsteady breath, the faintest rustle of paper, a sea breeze outside. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: HOME, NOTE, NOW</sub>

---
### S09 · ★★ کلوزآپ — چشم‌های خیس  `00:49–00:56` · 7s
**[A] می‌خواند — لب‌خوانی رو به دوربین**

- **موتور:** MiniMax H3 · 768P برای تست، فاینال 2K  ·  **جایگزین:** Seedance 2.0 (i2v + @Audio برای لب‌سینک)
- **چرا:** نزدیک‌ترین پلان کلیپ به چهره‌اش و آخرین لب‌خوانی. دومین پلانی که ارزش ۲K دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل حالت دوم و نور دوم)، LS-02
- **صدا:** میوت.
- **نکته:** اگر مدل صورت را بیش‌ازحد صاف کرد: «visible pores, unretouched skin, fine lines» را در پرامپت تصویر تکرار کن و CFG را به ۴ ببر.

**۱) فریم اول — Qwen-Image-2.1**

```text
Very tight close-up, the face filling the frame from the brow to just below the chin, slightly off centre with negative space to the right. the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her stands outdoors on the salt flat of the CEMETERY: a graveyard on the salt flats at the edge of a Gulf coastal town, flat unpolished stone slabs laid directly onto pale bone-white salt-crusted earth in uneven rows, dry thorn scrub, one leaning half-dead date palm, a low broken wall, and the flat silver line of the sea far behind under a bleached hazy sky, wind moving a single loose strand of hair across her cheek and the edge of her white shawl. Her eyes are wet and glassy with the light catching the film of moisture, but no tear has fallen. She looks directly into the lens for the first time in the film. Hard hazy daylight, the bleached salt flat a soft white wash behind. 85mm lens, extremely shallow depth of field, the eyes tack sharp. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 · 768P برای تست، فاینال 2K**

```text
Locked-off extreme close-up, the camera holds absolutely still for seven seconds. She sings the line straight into the lens, the mouth articulating clearly and naturally, the jaw and throat moving, one small breath mid-phrase. A single tear leaves one eye and runs down the cheek, unwiped, while she keeps singing without breaking. She blinks slowly once. The wind keeps moving the loose strand of hair and the shawl edge. No head turn, no hand, no other movement. Keep her face and shawl exactly as in the reference images. Soundscape: only salt-flat wind and breath. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: CEM, NOW, S, WA</sub>

---

## سکانس ۵ — پایان

### S10 · ★★ زنگ می‌خورد — حیاط پر می‌شود — پسر برمی‌گردد  `00:56–01:02` · 6s
**[B] تصویرسازی محض — او در قاب نیست**

- **موتور:** Seedance 2.0 · 1080p · multi-shot  ·  **جایگزین:** MiniMax H3 با فریم اول + فریم آخر
- **چرا:** سه ضربه‌ی روایی در ۶ ثانیه. Seedance تنها موتوری است که سه شات را در یک رندر و با سینکِ ضرب می‌سازد — یعنی یک رندر به‌جای سه تا.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-01 (پنل حیاط) → @Image1، CS-04 → @Image2، فایل صوتی ۶ ثانیه‌ی پایانی آهنگ → @Audio1
- **صدا:** صدای زنگ تنها آمبیانسی است که اجازه دارد تا −۱۲ dB بالا بیاید. بقیه زیر موسیقی.
- **نکته:** اگر Seedance شات سوم را درست درنیاورد، فقط همان ۳ ثانیه را جدا در H3 با role=first_frame و role=last_frame بساز (فریم اول: همه پشت به دوربین / فریم آخر: فقط یک بچه برگشته). گران‌تر ولی قطعی.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide high shot looking down into the courtyard of the SCHOOL: a small school in a Persian Gulf coastal town, a courtyard of pale sand-coloured cement tiles bleached by the sun, low walls of coral stone rendered in flaking white and painted sun-faded turquoise to waist height, two tall date palms throwing hard ragged shadows across the yard, a single flagpole, a one-storey bone-white plastered building with steel-framed windows and a deep shaded arcade, and a wide turquoise-painted metal double gate through the open turquoise gate. A crowd of primary-school children in pale blue-grey uniforms pours in through the gate and spreads across the bleached tiles, satchels swinging. Hard hazy sun, long palm shadows cutting across the yard. 24mm lens, deep focus. LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — Seedance 2.0 · 1080p · multi-shot**

```text
@Image1 is the courtyard, keep its architecture, tiles, palms and gate exactly. @Image2 is the boy and the uniform style. @Audio1 is the music, cut on its beats. Shot 1, zero to two seconds: a tight low shot of the brass bell swinging hard twice as the clapper strikes it, dust shaking off the rope. Shot 2, two to four seconds: a high wide as dozens of children flood in through the turquoise gate and fan out across the bleached courtyard, running, satchels swinging. Shot 3, four to six seconds: a medium shot from behind the last row of children as they settle into lines, and one single boy near the end of the row turns around and looks straight into the lens with a small open smile, raising one hand halfway, while no other child turns or reacts. Camera locked off in every shot, no handheld. Keep the boy's face exactly as in @Image2. Bleached hazy daylight, LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon. Audio: two clear brass bell strikes with a long ring-out, then a rush of children's voices and running feet, then a sudden hush.
```

<sub>بلوک‌های استفاده‌شده: NOW, SCHOOL</sub>

---

## نگتیو پرامپت مشترک (همه‌ی تصاویر Qwen)

```text
text, letters, words, arabic script, persian script, watermark, logo, signature, caption, subtitles, ui, extra fingers, six fingers, deformed hands, fused fingers, extra limbs, distorted face, asymmetrical eyes, plastic skin, waxy skin, beauty retouching, smoothed skin, oversharpened, hdr glow, oversaturated, neon, cartoon, anime, 3d render, cgi, video game, illustration, painting, sketch, blurry, low resolution, jpeg artifacts, duplicate people, cloned faces, upright headstones, western cemetery, crosses, church, coffins, blood, injury, corpse, western school uniforms, blazers, ties, jeans with logos, modern sneakers, smartphones, lens flare, tilted horizon, fisheye, heavy vignette, snow, forest, skyscrapers
```
