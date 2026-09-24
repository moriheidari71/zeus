# ۰۱ — شیت رفرنس کاراکتر، پراپ و لوکیشن

> این فایل **خودکار** ساخته می‌شود از `prompts.json` + `_partials/01-intro.md`.
> برای تغییر، یکی از آن دو را ویرایش کن و بعد اجرا کن: `python3 music-video/build_prompts.py`

---

## چرا اول شیت، بعد سناریو؟

مدل‌های ویدیو حافظه ندارند. هر رندر یک جهانِ نو است. تنها چیزی که چهره، لباس، معماری و رنگِ کلیپ را بین ۳۰ پلان یکی نگه می‌دارد، **یک بانک تصویرِ رفرنسِ ثابت** است که به همه‌ی رندرها تزریق می‌شود.

بنابراین ترتیب کار این است:

```
عکس‌های واقعیِ خواننده
        │
        ▼
 [Qwen-Image-2.1 · Edit]  ──►  CS-01  ترن‌اراند سه‌نما   ◄── مادرِ کل پروژه
        │                      CS-02  حالات چهره
        │                      CS-03  چرخش سر
        │                      CS-04  لباس
        │                      CS-05  نور و لوکیشن
        ▼
 [Qwen-Image-2.1 · T2I]   ──►  CS-06/07 مادر و پسر
                               PS-01    پراپ‌ها (RGBA)
                               LS-01/02/03 لوکیشن‌ها
        │
        ▼
 [Qwen-Image-2.1 · Edit]  ──►  فریم اولِ هر ۳۰ پلان (با CS/LS به‌عنوان رفرنس)
        │
        ▼
 [H3 / Seedance 2.0 / LTX-2.5]  ──►  ویدیو
```

Qwen-Image-2.1 تا **۱۰ تصویر رفرنس** در یک درخواست می‌گیرد و خودِ Qwen اعلام کرده که از یک «شیت سه‌نمای کاراکتر» می‌تواند استوری‌برد کامل بسازد — یعنی این ورک‌فلو دقیقاً همان چیزی است که مدل برایش ساخته شده.

---

## عکس‌هایی که باید از خواننده آماده کنی

برای CS-01 بین **۳ تا ۶ عکس** بده:

| # | عکس | چرا |
|---|-----|-----|
| ۱ | روبه‌روی کامل، نور یکنواخت، بدون لبخند | مرجعِ اصلی هویت |
| ۲ | سه‌رخ ۴۵ درجه | حجمِ گونه و بینی |
| ۳ | نیم‌رخ ۹۰ درجه | خط فک و پیشانی |
| ۴ | تمام‌قد ایستاده | تناسب بدن و قد |
| ۵ | (اختیاری) با همان لباسِ کلیپ | قفلِ وارُدرُب |
| ۶ | (اختیاری) در نور طبیعیِ ابری | قفلِ رنگ پوست |

**نباید:** عینک آفتابی، فیلتر سنگین اینستاگرام، فلاش مستقیم، رزولوشن پایین، عکس گروهی، زاویه‌ی از پایین که بینی را بزرگ می‌کند.

اگر فقط **یک عکس** داری: همان را به عنوان تصویر ۱ بده و در پرامپت CS-01 بنویس
`infer the profile and back views from the single reference, keep the front view identical to it` — نتیجه ۸۰٪ خوب است، و بعد CS-01 خروجی را دوباره به عنوان رفرنس به خودش بده تا تثبیت شود.

---

## تنظیمات Qwen-Image-2.1

| پارامتر | مقدار پیشنهادی | توضیح |
|---------|----------------|-------|
| رزولوشن | `2752 x 1536` برای ۱۶:۹ · `2048 x 2048` برای شیت‌های مربعی | خروجی نیتیو ۲K مدل |
| Steps | `40` | پیش‌فرض کد مرجع (Flow Matching / Euler) |
| CFG | `3.0 – 4.0` | زیر ۱ اصلاً کار نمی‌کند؛ برای جزئیات بیشتر تا ۴.۵ |
| Sampler | `Euler` + dynamic shifting | پیش‌فرض |
| Seed | **ثابت نگه‌دار** برای هر کاراکتر (مثلاً خواننده = `71001`) | پایین‌آوردن دریفت |
| رفرنس | تصویر ۱ = سوژه‌ی هدف، بقیه = رفرنس (تا ۱۰ تا) | ترتیب مهم است |
| ادیت موضعی | دایره‌ی رنگی / نقاشیِ روی تصویر / ماسک جدا | برای اصلاح فقط یک ناحیه، ماسک بهترین است |
| خروجی شفاف | برای PS-01 حالت RGBA را روشن کن | کامپوزیت پراپ‌ها در پست |

**روالِ اصلاح بدون خراب‌کردن بقیه‌ی فریم:** ماسک بده، نه پرامپت دوباره. Qwen-2.1 با `original + mask` به‌صورت دو ورودی، بقیه‌ی تصویر را دست‌نخورده نگه می‌دارد.

---

## هشدار مهم: خط فارسی

هیچ‌کدام از این چهار مدل خط فارسی/عربی را درست نمی‌نویسند. حروف را جدا می‌نویسند، بی‌معنی می‌سازند، یا آینه می‌کنند. پس:

1. در همه‌ی پرامپت‌ها `no text, no readable writing` گذاشته شده.
2. هر جا خط لازم است (اسم روی سنگ، دفترِ پسر، دفتر حضور و غیاب) تصویر را **بدون نوشته** بساز و متن را در پست (Photoshop / After Effects) کامپوزیت کن.
3. برای «خط قشنگ» پسر، بهترین راه: خطِ یک بچه‌ی واقعی را روی کاغذ خط‌دار بنویس، اسکن کن، و با بلندمود `Multiply` روی صفحه بگذار و با ترکرِ AE قفل کن. این تنها راهی است که واقعاً باورپذیر می‌شود.

---

## بلوک‌های هویت (متنِ خام)

اینها رشته‌هایی هستند که در `prompts.json` تعریف شده‌اند و داخل همه‌ی پرامپت‌ها با `{نام}` صدا زده می‌شوند. اگر می‌خواهی خواننده یا لوکیشن را عوض کنی، **فقط همین بلوک را ویرایش کن** — تمام ۳۰ پلان خودکار به‌روز می‌شوند.

**`{S}` — خواننده — قفل هویت**

```text
the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders
```

**`{WA}` — لباس A (کل کلیپ)**

```text
wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns
```

**`{WB}` — لباس B (سکانس باران)**

```text
wardrobe B: the same charcoal-grey collarless shirt, soaked through and clinging, sleeves down, no overshirt, black trousers dark with rain, hair wet and flattened
```

**`{M}` — مادر — گل‌بانو، ۵۲ ساله**

```text
the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk
```

**`{K}` — پسر — یاسین، ۹ ساله**

```text
the BOY (Yasin, 9): an Iranian primary-school boy; a round face, large dark-brown eyes with long lashes, thick straight black hair with a stubborn cowlick at the crown, slightly large front teeth with a narrow gap, light olive skin, a healing scratch on the right knee; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile
```

**`{BAG}` — پراپ — کیف مدرسه**

```text
the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap
```

**`{NOTE}` — پراپ — دفتر**

```text
the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections
```

**`{BELL}` — پراپ — زنگ برنجی**

```text
the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a blue-painted steel door, green patina in the grooves, the clapper visible inside
```

**`{STONE}` — پراپ — سنگ قبر (تخت، روی زمین)**

```text
the GRAVE: an Iranian Muslim grave, a flat polished grey-white marble slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut stems of white stock flowers, dry ochre earth around it
```

**`{SCHOOL}` — لوکیشن — حیاط مدرسه**

```text
the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate
```

**`{CLASS}` — لوکیشن — کلاس درس**

```text
the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light
```

**`{HOME}` — لوکیشن — خانه**

```text
the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain
```

**`{CEM}` — لوکیشن — قبرستان تپه‌ای**

```text
the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky
```

**`{ALLEY}` — لوکیشن — کوچه**

```text
the ALLEY: a narrow alley of packed dirt and cracked asphalt between mud-brick and cement-block houses, blue-painted steel doors, an open water channel along one edge, one leaning concrete pole with tangled wires, dry plane-tree leaves blown against the walls
```

**`{NOW}` — گرید — جهانِ «حالا»**

```text
LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon
```

**`{MEM}` — گرید — جهانِ «خاطره»**

```text
LOOK-MEMORY: warm 16mm memory photography, honey-golden low sun, half a stop overexposed, soft bloom and heavy halation, visible film grain and faint gate weave, faded reds and creamy whites, dreamy shallow focus
```

---

## پرامپت شیت‌ها (آماده‌ی کپی)

همه‌ی توکن‌ها باز شده‌اند. نسخه‌ی `.txt` هرکدام در `out/SHEETS/` هم هست.


### کاراکترها

#### CS-01 · ترن‌اراند سه‌نما — خواننده (شیت پایه)

- **حالت:** Qwen-Image-2.1 · Image Edit (۳ تا ۶ عکس واقعی خواننده به عنوان رفرنس)
- **اندازه:** `2752x1536`
- **نکته:** این شیتِ مادرِ کل پروژه است. همه‌ی فریم‌های بعدی این تصویر را به‌عنوان رفرنس هویت می‌گیرند. عکس‌های ورودی: یک نمای روبه‌رو، یک سه‌رخ، یک نیم‌رخ ۹۰ درجه، یک تمام‌قد، و در صورت امکان یکی با همان لباسِ کلیپ. بدون عینک آفتابی، بدون فیلتر سنگین، نور یکنواخت.

```text
Character reference sheet of the exact same man shown in the reference photographs. Preserve his facial identity with absolute fidelity: bone structure, eye shape and spacing, nose bridge and tip, lip shape, hairline, beard density and growth pattern, skin tone and texture. Three-view turnaround on a flat neutral light-grey seamless background: full-body front view on the left, exact ninety-degree left profile in the centre, full back view on the right. All three figures at identical height, identical scale, identical neutral standing A-pose with arms relaxed at the sides and feet shoulder-width apart, neutral closed-mouth expression, eyes level to camera in the front view. Head to shoes fully visible in every view with even headroom. Even soft studio lighting from a large front-left octabox with a broad fill, no hard shadows, no rim light, no colour cast. He is the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns. Photorealistic, 85mm lens, sharp focus edge to edge, flat uniform background, no props, no text, no captions, no grid lines.
```

#### CS-02 · شیت حالات چهره — خواننده

- **حالت:** Qwen-Image-2.1 · Image Edit (ورودی: CS-01 + عکس‌های واقعی)
- **اندازه:** `2048x2048`
- **نکته:** برای انتخاب حالت درست در هر پلان. حالت‌ها عمداً درونی و کم‌اغراق‌اند؛ سوگ ایرانی داد نمی‌زند.

```text
A nine-panel expression sheet of the exact same man from the reference images, identical face, identical hair and beard, identical wardrobe wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns. A clean three-by-three grid of tight head-and-shoulders portraits on the same flat neutral light-grey background, identical framing, identical scale, identical soft even studio lighting in every panel. Row one: neutral resting face; eyes lowered, looking at the ground; a slow inhale before singing with the lips just parted. Row two: singing softly with the mouth half open; singing loudly with the jaw dropped and the neck tensed; the mouth closed with the jaw clenched and the chin dimpled. Row three: eyes closed, head tilted slightly back; eyes wet and glassy but no tears falling, staring straight to camera; the faintest bitter half-smile with sad eyes. Restrained, interior, non-theatrical emotion. Photorealistic, 85mm lens, sharp focus, no text, no labels, no borders.
```

#### CS-03 · شیت چرخش سر (۵ زاویه) — خواننده

- **حالت:** Qwen-Image-2.1 · Image Edit (ورودی: CS-01)
- **اندازه:** `2752x1536`
- **نکته:** برای قفل‌کردن هویت در کلوزآپ‌ها. هنگام ساخت فریم اولِ پلان‌های نزدیک، این شیت را کنار CS-01 به‌عنوان رفرنس بده.

```text
A five-angle head rotation sheet of the exact same man from the reference image, one continuous row of five head-and-shoulders portraits at identical height and scale on a flat neutral light-grey background: full front, forty-five degrees left, ninety-degree left profile, forty-five degrees right, ninety-degree right profile. Neutral closed-mouth expression in all five, eyes following the camera only in the front view. Identical soft even studio lighting across all five, no shadow shift between panels. He is the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders. Photorealistic, 85mm lens, high micro-detail in skin and beard, no text, no borders.
```

#### CS-04 · شیت لباس و پیوستگی — خواننده

- **حالت:** Qwen-Image-2.1 · Image Edit (ورودی: CS-01)
- **اندازه:** `2752x1536`
- **نکته:** دو لباسِ کل کلیپ. لباس B فقط در سکانس بریج (باران) استفاده می‌شود.

```text
A two-look wardrobe continuity sheet of the exact same man from the reference image on a flat neutral light-grey background. Left half: one full-body front view and one three-quarter view wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns, dry and neat. Right half: one full-body front view and one three-quarter view wearing wardrobe B: the same charcoal-grey collarless shirt, soaked through and clinging, sleeves down, no overshirt, black trousers dark with rain, hair wet and flattened, water running from the hem, hair flattened and dripping. All four figures at identical height and scale, identical neutral pose, identical soft even studio lighting. He is the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders. Photorealistic, 85mm lens, accurate fabric weight and weave, no text, no labels.
```

#### CS-05 · شیت نور و لوکیشن — خواننده (کلید پیوستگی ویدیو)

- **حالت:** Qwen-Image-2.1 · Image Edit (ورودی: CS-01 + شیت لوکیشن مربوطه)
- **اندازه:** `2752x1536`
- **نکته:** مهم‌ترین شیت بعد از CS-01. برای هر پلان، پنلی را که نورش با آن صحنه می‌خواند به مدل ویدیو بده تا چهره در نور جدید تغییر شکل ندهد.

```text
A five-panel lighting continuity sheet of the exact same man from the reference image, five identical head-and-shoulders portraits at the same scale and the same three-quarter angle, only the lighting and colour changing between panels. Panel one: flat soft overcast daylight in a school courtyard, cool grey, no direction. Panel two: hard side light through a dusty classroom window, warm slash across one cheek, deep falloff on the other side. Panel three: cold blue overcast light on a bare hillside, wind-lifted hair, no fill. Panel four: low golden late-afternoon sun from behind, warm rim on the beard and ear, the face in soft shadow. Panel five: night rain, dark cool ambient with a single distant sodium streetlamp, wet skin catching small speculars. Identical face, identical beard, identical wardrobe wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns. He is the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders. Photorealistic, 85mm lens, no text, no labels.
```

#### CS-06 · شیت کاراکتر — مادر (گل‌بانو)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** صورتش را در کلوزآپ‌های زیاد نشان نده؛ قدرتِ این کاراکتر در دست‌ها، پشتِ سر و سایه‌اش است.

```text
Character reference sheet of one woman on a flat neutral light-grey seamless background. Three-view turnaround: full-body front view, exact ninety-degree left profile, and back view, all at identical height, identical scale, identical neutral standing pose with the hands clasped low in front, a neutral tired expression. Beside them, two smaller inset panels: a tight portrait of her face, and a close study of her folded working hands. Even soft studio lighting, no hard shadows. She is the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk. Photorealistic, 85mm lens, sharp focus, documentary honesty, no beauty retouching, no text, no labels.
```

#### CS-07 · شیت کاراکتر — پسر (یاسین، ۹ ساله)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** پسر فقط در فلاش‌بک‌های گرم و در پلان پایانی دیده می‌شود؛ همیشه زنده، خندان و سالم. هرگز صحنه‌ی مرگ، جسد، تشییع یا آسیب نساز.

```text
Character reference sheet of one young boy on a flat neutral light-grey seamless background. Three-view turnaround: full-body front view, exact ninety-degree left profile, and back view, all at identical height, identical scale, identical relaxed standing pose with the schoolbag strap in one hand. Beside them, three smaller inset panels: a tight portrait with a neutral face, a tight portrait laughing with the eyes almost closed, and a close study of his hand holding a blue ballpoint pen. He is the BOY (Yasin, 9): an Iranian primary-school boy; a round face, large dark-brown eyes with long lashes, thick straight black hair with a stubborn cowlick at the crown, slightly large front teeth with a narrow gap, light olive skin, a healing scratch on the right knee; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile. The satchel is the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap. Even soft studio lighting, warm and alive, photorealistic, 85mm lens, sharp focus, no text, no labels.
```


### پراپ‌ها

#### PS-01 · شیت پراپ — کیف، دفتر، زنگ

- **حالت:** Qwen-Image-2.1 · Text to Image (خروجی RGBA برای کامپوزیت)
- **اندازه:** `2048x2048`
- **نکته:** خروجی شفاف بگیر تا بتوانی همین پراپ‌ها را در فریم‌های دیگر کامپوزیت کنی و شکلشان هرگز عوض نشود.

```text
A clean product-style prop reference sheet, three objects photographed separately on a transparent background with an alpha channel, arranged side by side at consistent scale: first the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap shown in a three-quarter view with the flap closed and again with the flap open; second the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections shown closed and again open flat on a page of handwriting seen from directly above but slightly out of focus so no letterform is legible; third the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a blue-painted steel door, green patina in the grooves, the clapper visible inside shown in a straight side view. Even soft studio lighting from above and slightly left, soft contact shadow only, accurate material response: stiff vinyl, cheap soft paper, aged brass. Photorealistic, macro clarity, 100mm lens, transparent background, no text, no captions, no branding.
```


### لوکیشن‌ها

#### LS-01 · شیت لوکیشن — حیاط مدرسه (۴ زاویه)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** این شیت را به‌عنوان رفرنس محیط به Seedance و H3 بده تا معماری حیاط بین پلان‌ها عوض نشود.

```text
A four-panel location reference sheet of a single consistent place, the same courtyard seen from four positions in a two-by-two grid: a high wide establishing view of the whole courtyard, an eye-level view from the gate towards the building, a reverse eye-level view from the building steps towards the gate, and a corner detail of the plane tree against the blue-painted wall. The place is the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate. Completely empty of people. Early morning, flat soft overcast light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Consistent architecture, consistent tile pattern, consistent paint wear across all four panels. Photorealistic, 24mm and 35mm lens looks, no text, no labels, no signage.
```

#### LS-02 · شیت لوکیشن — کلاس درس (۳ زاویه)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** جای نیمکتِ خالی را همین‌جا تثبیت کن: ردیف وسط، دومین نیمکت از عقب، صندلی سمت پنجره.

```text
A three-panel location reference sheet of a single consistent room seen from three positions in one row: a wide view from the back of the room towards the chalkboard, a reverse wide view from the chalkboard towards the back wall and windows, and a low three-quarter view along the middle row of desks. The room is the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light. Completely empty of people. One specific desk in the middle row, second from the back on the window side, is marked only by a small bunch of white stock flowers laid on its seat. Morning side light through the windows, visible dust in the beams, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Consistent desk count, consistent window count, consistent wall wear across all three panels. Photorealistic, 24mm and 35mm lens looks, no text on the chalkboard, no readable writing, no labels.
```

#### LS-03 · شیت لوکیشن — خانه و قبرستان

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** توجه: قبر ایرانی سنگِ تختِ روی زمین است، نه سنگ ایستاده. این را در نگتیو هم گذاشته‌ایم.

```text
A four-panel location reference sheet in a two-by-two grid, two places, two views each. Top row, the same room from two positions: a wide view from the doorway showing the whole room, and a low view across the kilim towards the window. The room is the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain. Bottom row, the same hillside from two positions: a wide establishing view across the rows of slabs towards the bare hills, and a low three-quarter view of one single newer slab in the foreground. The hillside is the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky and the slab is the GRAVE: an Iranian Muslim grave, a flat polished grey-white marble slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut stems of white stock flowers, dry ochre earth around it. Completely empty of people. Flat overcast light in both places, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Photorealistic, 24mm and 35mm lens looks, no text, no readable inscription, no upright headstones, no crosses.
```


### نگتیو پرامپت مشترک

```text
text, letters, words, watermark, logo, signature, caption, subtitles, ui, extra fingers, six fingers, deformed hands, fused fingers, extra limbs, distorted face, asymmetrical eyes, plastic skin, waxy skin, beauty retouching, oversharpened, hdr glow, oversaturated, neon, cartoon, anime, 3d render, cgi, video game, illustration, painting, sketch, blurry, low resolution, jpeg artifacts, duplicate people, cloned faces, upright headstones, western cemetery, crosses, church, pews, coffins, blood, injury, corpse, western school uniforms, blazers, ties, jeans with logos, modern sneakers, smartphones, lens flare, tilted horizon, fisheye, vignette overload
```
