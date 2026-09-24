# ۰۱ — شیت رفرنس کاراکتر، پراپ و لوکیشن

> این فایل **خودکار** ساخته می‌شود از `prompts.json` + `_partials/01-intro.md`.
> برای تغییر، یکی از آن دو را ویرایش کن و بعد اجرا کن: `python3 music-video/build_prompts.py`

---

## 🚨 دو چیزی که باید انجام بدهی

### ۱. عکس‌ها به دستم نرسیدند

پرتره و عکس لباس صورتی/سفید در ورک‌اسپیس نیامدند. دوباره پیوستشان کن.
تا آن موقع، بلوک `{S}` یک توصیفِ **جانشین** دارد که با یک جمله‌ی بزرگ علامت‌گذاری شده:

```
>>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<<
```

وقتی عکس‌ها را بفرستی، من این بلوک را با ویژگی‌های واقعیِ او بازنویسی می‌کنم و هر ۱۰ پلان خودکار به‌روز می‌شوند.

### ۲. سه عکسی که باید آماده کنی

| # | عکس | نقش در CS-01 |
|---|-----|--------------|
| ۱ | **پرتره‌ی او** — روبه‌رو، نور یکنواخت، بدون عینک و فیلتر | ورودی ۱ → قفلِ چهره |
| ۲ | **لباس سفید** — کامل و صاف، ترجیحاً روی خودش یا آویزان | ورودی ۲ → قفلِ لباس |
| ۳ | **عکس با لباس صورتی** — همان شخص، تمام‌قد | ورودی ۳ → فرم بدن و قد |

اگر عکس تمام‌قد نداری اشکالی ندارد — با همان پرتره کار می‌کند، فقط در پرامپت بنویس
`infer the full body proportions from the portrait, keep the face identical`.

---

## چرا اول شیت، بعد سناریو؟

مدل‌های ویدیو حافظه ندارند. هر رندر یک جهانِ نو است. تنها چیزی که چهره، لباسِ سفید و معماری را بین ۱۰ پلان یکی نگه می‌دارد، یک **بانک تصویرِ رفرنسِ ثابت** است.

```
پرتره‌ی او  +  عکس لباس سفید
        │
        ▼
 [Qwen-Image-2.1 · Edit]  ──►  ★ CS-01  ترن‌اراند سه‌نما با لباس سفید
        │                      ★ CS-02  حالت + نور (۶ پنل)
        │                        CS-03  پارچه و باد
        ▼
 [Qwen-Image-2.1 · T2I]   ──►    CS-04  پسر
                                 PS-01  پراپ‌ها (RGBA)
                                 LS-01/02  لوکیشن‌ها
        │
        ▼
 [Qwen-Image-2.1 · Edit]  ──►  ۱۰ فریمِ اول (+ ۱ فریم آخر)
        │
        ▼
 [H3 · Seedance 2.0 · LTX-2.5]  ──►  ۱۰ کلیپ · ۶۲ ثانیه
```

Qwen-Image-2.1 تا **۱۰ رفرنس** در یک درخواست می‌گیرد و نمونه‌های رسمیِ خودش شامل «ساختن یک لباس کامل از ۵ رفرنس جدا» و «virtual try-on» است — یعنی «این شخص + آن لباس» دقیقاً کاری است که مدل برایش ساخته شده.

**اگر بودجه‌ات خیلی تنگ است:** فقط **CS-01** و **CS-02** و **LS-01** را بساز. با همین سه شیت می‌شود هر ۱۰ پلان را زد.

---

## تنظیمات Qwen-Image-2.1

| پارامتر | مقدار |
|---------|-------|
| رزولوشن | `2752 x 1536` (۱۶:۹) · `2048 x 2048` (شیت مربعی) |
| Steps | ۴۰ |
| CFG | ۳.۰–۴.۰ (زیر ۱ اصلاً کار نمی‌کند) |
| Sampler | Euler + dynamic shifting (Flow Matching) |
| Seed | برای او ثابت: `71001` · پسر: `71003` |
| رفرنس | تصویر ۱ = سوژه‌ی هدف، بقیه رفرنس، تا ۱۰ تا |
| RGBA | فقط برای `PS-01` |

**اصلاح بدون خراب‌کردن بقیه‌ی فریم:** ماسک بده، نه پرامپتِ دوباره. Qwen-2.1 با `original + mask` به‌صورت دو ورودی، بقیه‌ی تصویر را دست‌نخورده نگه می‌دارد.

---

## هشدار: خط فارسی

هیچ‌کدام از این مدل‌ها خط فارسی را درست نمی‌نویسند — در مودبورد ببین، روی سنگ یک خطِ بی‌معنی حک شده.
پس در همه‌ی پرامپت‌ها `no text, no readable writing` گذاشته شده و هر نوشته‌ای (اسم روی سنگ، خطِ دفتر) **در پست کامپوزیت می‌شود**. روالش در `04-pipeline-post.md`.

---

## بلوک‌های هویت (متنِ خام)

اینها در `prompts.json` تعریف شده‌اند و در همه‌ی پرامپت‌ها با `{نام}` صدا زده می‌شوند. برای تغییر خواننده، لباس یا لوکیشن **فقط همین بلوک را ویرایش کن** — هر ۱۰ پلان خودکار به‌روز می‌شوند.

**`{S}` — خواننده / شخصیت اول — قفل هویت**

```text
the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared
```

**`{WA}` — لباس سفید**

```text
wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her
```

**`{K}` — پسر — ۹ ساله**

```text
the BOY (her son, 9): a southern Iranian primary-school boy; a round sun-browned face, large dark eyes with long lashes, close-cropped black hair, slightly large front teeth with a narrow gap; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile
```

**`{BAG}` — پراپ — کیف مدرسه**

```text
the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film
```

**`{NOTE}` — پراپ — دفتر**

```text
the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections
```

**`{BELL}` — پراپ — زنگ برنجی**

```text
the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a turquoise-painted steel door, green patina in the grooves, the clapper visible inside
```

**`{STONE}` — پراپ — سنگ قبر (تخت، روی زمین)**

```text
the GRAVE: an Iranian Muslim grave, a flat unpolished pale stone slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut white stems, salt-crusted bone-white earth around it
```

**`{SCHOOL}` — لوکیشن — حیاط مدرسه (جنوب)**

```text
the SCHOOL: a small school in a Persian Gulf coastal town, a courtyard of pale sand-coloured cement tiles bleached by the sun, low walls of coral stone rendered in flaking white and painted sun-faded turquoise to waist height, two tall date palms throwing hard ragged shadows across the yard, a single flagpole, a one-storey bone-white plastered building with steel-framed windows and a deep shaded arcade, and a wide turquoise-painted metal double gate
```

**`{HOME}` — لوکیشن — خانه (جنوب)**

```text
the HOME: a modest southern Iranian room, a woven palm-frond mat over a bare cement floor, whitewashed plaster walls, one deep shaded window opening with a thin cloth curtain lifting in the sea breeze, a low niche holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a large unglazed clay water jar in the corner
```

**`{CEM}` — لوکیشن — قبرستانِ نمکی**

```text
the CEMETERY: a graveyard on the salt flats at the edge of a Gulf coastal town, flat unpolished stone slabs laid directly onto pale bone-white salt-crusted earth in uneven rows, dry thorn scrub, one leaning half-dead date palm, a low broken wall, and the flat silver line of the sea far behind under a bleached hazy sky
```

**`{ALLEY}` — لوکیشن — کوچه**

```text
the ALLEY: a narrow lane in a Gulf coastal town between houses of coral stone rendered in flaking white and pale ochre, turquoise-painted steel doors, one low wind-catcher tower above the rooftops, hard palm-frond shadows striping the sand-dusted ground
```

**`{NOW}` — گرید — پالت جنوب**

```text
LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon
```

---

## پرامپت شیت‌ها (آماده‌ی کپی)

همه‌ی توکن‌ها باز شده‌اند. نسخه‌ی `.txt` هرکدام در `out/SHEETS/` هم هست.


### کاراکترها

#### CS-01 · ★ ترن‌اراند سه‌نما — خواننده با لباس سفید

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی ۱: پرتره‌ی او · ورودی ۲: عکس لباس سفید · ورودی ۳: عکس لباس صورتی (برای فرم بدن)
- **اندازه:** `2752x1536`
- **نکته:** ضروری‌ترین شیت. Qwen-2.1 رسماً برای همین ساخته شده: ترکیب یک نفر با لباسِ جدا از رفرنسِ دیگر (virtual try-on). اگر بودجه‌ات فقط به یک شیت می‌رسد، همین یکی را بساز.

```text
Character reference sheet. The woman is the exact person in reference image one — preserve her facial identity with absolute fidelity: bone structure, eye shape and spacing, nose, lip shape, brow shape, hairline, skin tone and texture. Dress her in the white garment shown in reference image two, reproducing its exact cut, fabric weight, drape and embroidery. Three-view turnaround on a flat neutral light-grey seamless background: full-body front view on the left, exact ninety-degree left profile in the centre, full back view on the right. All three figures at identical height, identical scale, identical neutral standing pose with the arms relaxed at the sides, feet together, a calm closed-mouth expression, eyes level to camera in the front view. Head to feet fully visible in every view with even headroom. Even soft studio lighting from a large front-left octabox with broad fill, no hard shadows, no rim light, no colour cast. She is the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her. Photorealistic, 85mm lens, sharp focus edge to edge, flat uniform background, no props, no text.
```

#### CS-02 · ★ شیت ترکیبی حالت + نور (کلید پیوستگی)

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی: CS-01 + پرتره‌ی واقعی
- **اندازه:** `2752x1536`
- **نکته:** سه شیت را در یکی ادغام کرده‌ام تا هزینه پایین بماند: حالت چهره + نورهای واقعیِ هر لوکیشن. برای هر پلان، پنلی را که نورش می‌خواند به مدل ویدیو بده.

```text
A six-panel reference sheet of the exact same woman from the reference image, six head-and-shoulders portraits in two rows of three, identical scale, identical three-quarter angle, identical face, identical white shawl and dress. Only expression and lighting change. Top row, expressions under the same flat soft light: a neutral resting face with lowered eyes; singing softly with the mouth half open; the mouth closed with the jaw set and the chin lifted. Bottom row, the same neutral expression under three different lights: hazy bleached high sun in an open courtyard with deep shadow under the brow; hard raking low sun from the side on a salt flat with wind lifting her shawl; soft shaded window light from a deep dark interior with a bright doorway behind her. Restrained, interior, non-theatrical emotion throughout. She is the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her. Photorealistic, 85mm lens, no text, no labels, no borders.
```

#### CS-03 · شیت لباس — قفلِ پارچه و حرکت

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی: CS-01 + عکس لباس سفید
- **اندازه:** `2752x1536`
- **نکته:** بادِ جنوب بخشی از زبانِ بصریِ کلیپ است. این شیت به مدل ویدیو یاد می‌دهد پارچه چطور باید حرکت کند.

```text
A four-panel wardrobe and fabric study of the exact same woman from the reference image, four full-body views on a flat neutral light-grey background at identical height and scale: standing still with the fabric hanging straight; the same pose with a strong side wind lifting the shawl ends and pressing the dress against one leg; a three-quarter back view with the shawl blown forward over one shoulder; a close detail of the sleeve cuff and neckline embroidery filling the panel. Reproduce the garment's exact cut, weight, weave and embroidery from the reference. Even soft studio lighting in every panel. She is the WOMAN: the singer and the protagonist, one and the same person — a southern Iranian woman from the Persian Gulf coast, in her late thirties, of average height and slight build. >>> REPLACE THIS SENTENCE WITH HER REAL FEATURES FROM THE PORTRAIT PHOTO <<< warm bronze-olive sun-touched skin; an oval face with strong cheekbones and a softly defined jaw; large dark almond eyes with thick natural lashes and slightly heavy lids; dark well-defined eyebrows; a straight nose; full lips usually held closed; long dark wavy hair almost entirely covered by her shawl with a few strands loose at the temple; small thin gold hoop earrings; henna-darkened fingertips; a steady, direct, unflinching gaze; a very upright, grounded, still posture with the shoulders squared wearing wardrobe: a long loose ankle-length white southern Iranian dress in light cotton, wide falling sleeves that catch the wind, tone-on-tone white embroidery at the neckline and cuffs, worn over white wide-legged trousers with embroidered cuffs at the ankle, and a long soft off-white shawl draped over the head and shoulders with the ends hanging loose down the back; simple flat sandals; small thin gold hoop earrings and nothing else; no logos, no print, no bright colour anywhere on her. Photorealistic, 85mm and 100mm lens looks, accurate light cotton behaviour, no text, no labels.
```

#### CS-04 · شیت کاراکتر — پسر (۹ ساله)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2048x2048`
- **نکته:** پسر فقط در پلان آخر و برای یک ثانیه دیده می‌شود — همیشه زنده و خندان. هرگز صحنه‌ی مرگ، جسد یا تشییع نساز.

```text
Character reference sheet of one young boy on a flat neutral light-grey seamless background: a full-body front view and an exact ninety-degree left profile at identical height and scale in a relaxed standing pose, plus two smaller inset panels beside them, one tight neutral portrait and one tight portrait smiling openly at camera with a half-raised hand. He is the BOY (her son, 9): a southern Iranian primary-school boy; a round sun-browned face, large dark eyes with long lashes, close-cropped black hair, slightly large front teeth with a narrow gap; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile. Even soft studio lighting, warm and alive, photorealistic, 85mm lens, sharp focus, no text, no labels.
```


### پراپ‌ها

#### PS-01 · شیت پراپ — کیف، دفتر، زنگ

- **حالت:** Qwen-Image-2.1 · Text to Image (خروجی RGBA)
- **اندازه:** `2048x2048`
- **نکته:** خروجی شفاف بگیر تا همین پراپ‌ها را در فریم‌های دیگر کامپوزیت کنی و شکلشان هرگز عوض نشود.

```text
A clean prop reference sheet, three objects photographed separately on a transparent background with an alpha channel, side by side at consistent scale: first the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap — the only saturated warm colour allowed anywhere in the film in a three-quarter view with the flap closed and again with the flap open; second the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections closed and again open flat seen from directly above but slightly out of focus so no letterform is legible; third the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a turquoise-painted steel door, green patina in the grooves, the clapper visible inside in a straight side view. Even soft studio lighting from above and slightly left, soft contact shadow only, accurate material response for stiff vinyl, cheap soft paper and aged brass. Photorealistic, macro clarity, 100mm lens, transparent background, no text, no branding.
```


### لوکیشن‌ها

#### LS-01 · شیت لوکیشن — مدرسه، کوچه، خانه

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** این شیت را به‌عنوان رفرنس محیط به H3 و Seedance بده تا معماری بین پلان‌ها عوض نشود.

```text
A four-panel location reference sheet in a two-by-two grid, all completely empty of people. Panel one: a high wide view of the whole courtyard. Panel two: an eye-level view from the gate towards the shaded arcade of the building. The place in both is the SCHOOL: a small school in a Persian Gulf coastal town, a courtyard of pale sand-coloured cement tiles bleached by the sun, low walls of coral stone rendered in flaking white and painted sun-faded turquoise to waist height, two tall date palms throwing hard ragged shadows across the yard, a single flagpole, a one-storey bone-white plastered building with steel-framed windows and a deep shaded arcade, and a wide turquoise-painted metal double gate. Panel three: a wide view down the lane, which is the ALLEY: a narrow lane in a Gulf coastal town between houses of coral stone rendered in flaking white and pale ochre, turquoise-painted steel doors, one low wind-catcher tower above the rooftops, hard palm-frond shadows striping the sand-dusted ground. Panel four: a wide view from the doorway into the room, which is the HOME: a modest southern Iranian room, a woven palm-frond mat over a bare cement floor, whitewashed plaster walls, one deep shaded window opening with a thin cloth curtain lifting in the sea breeze, a low niche holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a large unglazed clay water jar in the corner. Consistent architecture, consistent render and paint wear, consistent palm shadows. Late morning, LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon. Photorealistic, 24mm and 35mm lens looks, no text, no signage, no labels.
```

#### LS-02 · شیت لوکیشن — قبرستان و سنگ

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2752x1536`
- **نکته:** توجه: قبر ایرانی سنگِ تختِ روی زمین است، نه سنگ ایستاده. در نگتیو هم گذاشته شده.

```text
A two-panel location reference sheet, one row, both completely empty of people. Panel one: a very wide establishing view across the rows of flat slabs towards the distant silver line of the sea. Panel two: a low three-quarter view of one single newer, paler slab in the foreground. The place is the CEMETERY: a graveyard on the salt flats at the edge of a Gulf coastal town, flat unpolished stone slabs laid directly onto pale bone-white salt-crusted earth in uneven rows, dry thorn scrub, one leaning half-dead date palm, a low broken wall, and the flat silver line of the sea far behind under a bleached hazy sky and the slab is the GRAVE: an Iranian Muslim grave, a flat unpolished pale stone slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut white stems, salt-crusted bone-white earth around it. Bleached hazy midday light, LOOK: cinematic 35mm photography, hazy bleached Persian Gulf daylight, high hard sun diffused through salt haze, a pale palette of bone white, sun-faded turquoise, sand ochre and date-palm green, desaturated by about thirty percent, bright sky against deep crushed shadows, fine film grain, gentle halation, natural unretouched skin tones, no lens flare, level horizon. Photorealistic, 24mm and 35mm lens looks, no text, no readable inscription, no upright headstones, no crosses.
```


### نگتیو پرامپت مشترک

```text
text, letters, words, arabic script, persian script, watermark, logo, signature, caption, subtitles, ui, extra fingers, six fingers, deformed hands, fused fingers, extra limbs, distorted face, asymmetrical eyes, plastic skin, waxy skin, beauty retouching, smoothed skin, oversharpened, hdr glow, oversaturated, neon, cartoon, anime, 3d render, cgi, video game, illustration, painting, sketch, blurry, low resolution, jpeg artifacts, duplicate people, cloned faces, upright headstones, western cemetery, crosses, church, coffins, blood, injury, corpse, western school uniforms, blazers, ties, jeans with logos, modern sneakers, smartphones, lens flare, tilted horizon, fisheye, heavy vignette, snow, forest, skyscrapers
```
