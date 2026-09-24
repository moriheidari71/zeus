# ۰۱ — شیت رفرنس کاراکتر، پراپ و لوکیشن

> این فایل **خودکار** ساخته می‌شود از `prompts.json` + `_partials/01-intro.md`.
> برای تغییر، یکی از آن دو را ویرایش کن و بعد اجرا کن: `python3 music-video/build_prompts.py`

---

## دو رفرنسی که فرستادی

| نام | چیست | نقش |
|-----|------|-----|
| **REF-01** | پرترهٔ او — روسری مشکی، چشم‌های سبز | 🔒 قفلِ **چهره** |
| **REF-02** | شیت ۶ پنلی Qwen — لباس شیری با شال مارونی | 🔒 قفلِ **لباس** |

این دو فایل را کنار پروژه نگه دار؛ ورودیِ همهٔ شیت‌ها هستند. (به فایل‌سیستم من نرسیدند، فقط دیدمشان — پس خودت باید به Qwen بدهی‌شان.)

### مشکلی که باید اول حل شود

شیتی که فرستادی **لباسش درست است ولی چهره‌اش او نیست** — چشم‌ها قهوه‌ای‌اند و ابروها فرق دارند.
پس اولین کاری که باید بکنی **CS-00** است: پیوندِ چهرهٔ REF-01 روی همان شیت، بدون دست‌زدن به لباس.

---

## چهار مشخصهٔ چهره که هرگز نباید گم شوند

از روی پرتره، اینها امضای صورت او هستند و هر چهار تا در بلوک `{S}` با حروف بزرگ شماره‌گذاری شده‌اند:

| # | مشخصه | چرا حیاتی است |
|---|-------|----------------|
| ۱ | **چشم‌های سبزِ خاکستری** با حلقهٔ تیرهٔ دور عنبیه | نادرترین ویژگی‌اش — مدل‌ها دائم قهوه‌ای‌اش می‌کنند |
| ۲ | **ابروهای خیلی پرپشت، صاف، تیره و پایین** | دومین چیزی که چهره‌اش را می‌سازد |
| ۳ | **لب‌های پر با کمانِ تیزِ بالای لب** | |
| ۴ | **بینیِ باریک و صاف با نوکِ گردِ کوچک** | |

`brown eyes, hazel eyes, thin eyebrows, plucked eyebrows, arched eyebrows` به ابتدای نگتیو پرامپت اضافه شده‌اند.

---

## ترتیب اجرا

```
REF-01 (پرتره)  +  REF-02 (شیت لباس)
        │
        ▼
 ★★ CS-00   پیوندِ چهره روی شیت لباس        ← اولین کار
        │
        ▼
 ★★ CS-01   ترن‌اراند سه‌نما، پس‌زمینهٔ خنثی  ← مادرِ کل پروژه
        │
        ├─► ★ CS-02   حالت + نور (۶ پنل)
        └─► ★ CS-03   شالِ روی سر + باد
        │
        ▼
 [Qwen T2I]  CS-04 پسر · PS-01 پراپ‌ها · LS-01/02 لوکیشن‌ها
        │
        ▼
 [Qwen Edit] ۱۰ فریمِ اول  →  [H3 · Seedance · LTX]  →  ۶۲ ثانیه
```

**اگر بودجه خیلی تنگ است:** فقط **CS-00 + CS-01 + LS-01** را بساز. با همین سه تا می‌شود هر ۱۰ پلان را زد.

---

## دو حالتِ لباس

| بلوک | کجا | توضیح |
|------|-----|-------|
| `{WA}` | S02 · S03 · S05 | شال مارونی روی شانه، موها باز — همان چیزی که در REF-02 است |
| `{WH}` | S07 · S09 | **شال مارونی روی سر کشیده شده** مثل روسری، زنجیر طلا از زیرش پیدا |

**بیتِ لباس:** بین S06 و S07 — یعنی وقتی به سر قبر می‌رسد — شال را روی سرش می‌کشد. این تغییر خارج از قاب اتفاق می‌افتد. هم از نظر فرهنگی درست است، هم یک ریتمِ بصری به کلیپ می‌دهد، و هم کلوزآپ پایانی (S09) را قاب‌بندی می‌کند.

---

## تنظیمات Qwen-Image-2.1

| پارامتر | مقدار |
|---------|-------|
| رزولوشن | `2752 x 1536` (۱۶:۹) · `2048 x 2048` (مربعی) |
| Steps | ۴۰ |
| CFG | ۳.۵ معمولی · **۴.۵ برای CS-00** اگر چشم سبز درنیامد |
| Sampler | Euler + dynamic shifting (Flow Matching) |
| Seed | برای او ثابت: `71001` · پسر: `71003` |
| رفرنس | تصویر ۱ = سوژهٔ هدف، بقیه رفرنس، تا ۱۰ تا |

**ترفند CS-00:** پرترهٔ REF-01 را **دو بار** به‌عنوان ورودی ۲ و ۳ بده. تکرارِ یک رفرنس، وزنش را در توجه مدل بالا می‌برد و قفلِ چهره محسوس‌تر می‌شود.

**اصلاح بدون خراب‌کردن بقیهٔ فریم:** ماسک بده، نه پرامپتِ دوباره. Qwen-2.1 با `original + mask` به‌صورت دو ورودی، بقیهٔ تصویر را دست‌نخورده نگه می‌دارد. برای درست‌کردن فقط رنگ چشم، یک ماسک کوچک روی چشم‌ها بکش و بنویس `pale green-grey iris with a darker limbal ring`.

---

## هشدار: خط فارسی

هیچ‌کدام از این مدل‌ها خط فارسی را درست نمی‌نویسند. در همهٔ پرامپت‌ها `no text, no readable writing` گذاشته شده و هر نوشته‌ای (اسم روی سنگ، خطِ دفتر) **در پست کامپوزیت می‌شود**. روالش در `04-pipeline-post.md`.

---

## بلوک‌های هویت (متنِ خام)

اینها در `prompts.json` تعریف شده‌اند و در همهٔ پرامپت‌ها با `{نام}` صدا زده می‌شوند. برای تغییر چهره، لباس یا لوکیشن **فقط همین بلوک را ویرایش کن** — هر ۱۰ پلان خودکار به‌روز می‌شوند.

**`{S}` — خواننده / شخصیت اول — قفل هویت**

```text
the WOMAN: the singer and the protagonist, one and the same person — a young southern Iranian woman in her mid twenties. Her face must match the portrait reference exactly and is defined by four features that must never change: FIRST, pale green-grey eyes, large and almond-shaped, with a distinct darker limbal ring and long dark lashes — her eyes are green, never brown. SECOND, very thick, straight, dark, low-set eyebrows with only a slight arch, sitting close above the eyes. THIRD, full lips with a sharply defined cupid's bow, the lower lip fuller, natural rose colour. FOURTH, a narrow straight nose with a small defined rounded tip. Beyond those: a soft oval face tapering to a gently pointed chin, high rounded cheekbones with a natural warm flush, fair light-olive skin with fine visible texture and no blemishes, a long neck, and long thick dark brown-black wavy hair. Her expression is calm, level and unflinching; she holds very still, shoulders squared, and carries grief quietly rather than performing it
```

**`{WA}` — لباس سفید**

```text
wardrobe: a long loose ankle-length ivory-cream kurta of soft slubbed cotton-silk, wide elbow-length kimono sleeves with a gold-embroidered cuff band, a small V neckline framed by a diamond-shaped maroon-and-gold embroidered panel, and scattered small gold paisley motifs across the body, the hem finished with a gold embroidered border and cut longer at the sides; matching ivory straight trousers with a densely gold-embroidered panel at each ankle; a long deep-maroon chiffon shawl draped over the left shoulder with both ends hanging loose and floating in the wind; layered gold jewellery — a delicate gold head-chain across the forehead with small hanging gold leaves and a round central medallion, a long two-tier gold coin-and-pendant necklace over the chest; henna patterns on the backs of both hands; cream platform wedge sandals; her hair worn loose, long and wavy, uncovered
```

**`{K}` — پسر — ۹ ساله**

```text
the BOY (her son, 7, a first-grader): a southern Iranian child on his first year of school; a small round sun-browned face, large dark eyes with long lashes, close-cropped black hair, two slightly large front teeth with a narrow gap, a scattering of tiny freckles across the nose; the Iranian primary-school uniform worn slightly too big for him: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile
```

**`{BAG}` — پراپ — کیف مدرسه**

```text
the SCHOOLBAG: a first-grader's rectangular Iranian school satchel in exactly the same deep maroon as her chiffon shawl, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, small enough for a seven-year-old, with a hand-sewn white cotton name tag stitched inside the flap — her shawl and this satchel are the only two warm saturated things in the entire film and they are the same red
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

**`{WH}` — WH**

```text
wardrobe, shawl-up variant: exactly the same ivory-cream embroidered kurta, ivory trousers with gold ankle panels, gold head-chain, gold coin necklace and henna hands, but the deep-maroon chiffon shawl is now pulled up over her head like a veil, framing her face, the gold head-chain still visible at her forehead beneath it, both ends of the shawl hanging down her front and lifting in the wind; a few strands of her dark hair escaping at the temples
```

---

## پرامپت شیت‌ها (آماده‌ی کپی)

همه‌ی توکن‌ها باز شده‌اند. نسخه‌ی `.txt` هرکدام در `out/SHEETS/` هم هست.


### کاراکترها

#### CS-00 · ★★ پیوندِ چهره روی شیت لباس — اولین کاری که باید بکنی

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی ۱: REF-02 (شیت ۶ پنلی لباس) · ورودی ۲ و ۳: REF-01 (پرتره‌ی او)
- **اندازه:** `2752x1536`
- **نکته:** شیتی که فرستادی لباس درست را دارد ولی چهره‌ی او نیست. این پرامپت فقط چهره را عوض می‌کند و لباس، ژست، ترکیب‌بندی و نور را دست نمی‌زند. پرتره را دو بار به‌عنوان ورودی بده (۲ و ۳) — تکرار رفرنس، قفلِ چهره را محسوس‌تر می‌کند. اگر رنگ چشم سبز درنیامد، CFG را به ۴.۵ ببر و دوباره بزن.

```text
Take image one exactly as it is and change only the woman's face and hair colour. Replace her face in every single panel with the exact face of the woman in image two, matching her identity precisely: her pale green-grey almond eyes with the darker limbal ring, her very thick straight dark low-set eyebrows, her full lips with the sharp cupid's bow, her narrow straight nose with a small rounded tip, her soft oval face and gently pointed chin, her high rounded cheekbones and fair light-olive skin. Her eyes must be clearly green, not brown. Keep absolutely everything else in image one untouched and pixel-identical: the same six panels in the same layout, the same numbering, the same white background, the same poses, the same camera angles, the same lighting and shadows, the same ivory-cream embroidered kurta, the same deep-maroon chiffon shawl and the way it falls, the same gold head-chain, the same gold coin necklace, the same henna on the hands, the same trousers, the same shoes, the same hair length and wave pattern. Do not restyle, do not recompose, do not change the garment in any way. Photorealistic, high detail in the eyes and skin texture, visible pores, no beauty retouching, no smoothing.
```

#### CS-01 · ★★ ترن‌اراند سه‌نما — پاک، روی پس‌زمینه‌ی خنثی

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی ۱: CS-00 · ورودی ۲: REF-01 (پرتره)
- **اندازه:** `2752x1536`
- **نکته:** مادرِ کل پروژه. شیت CS-00 پس‌زمینه‌ی سفیدِ محصولی دارد؛ این نسخه روی خاکستریِ خنثی و با ژست کاملاً یکسان است که برای رفرنس‌دادن به مدل‌های ویدیو بهتر جواب می‌دهد.

```text
Character reference sheet of the exact same woman shown in the reference images, preserving her facial identity with absolute fidelity, especially her pale green-grey eyes, her very thick straight dark eyebrows and her full lips. Three-view turnaround on a flat neutral light-grey seamless background: full-body front view on the left, exact ninety-degree left profile in the centre, full back view on the right. All three figures at identical height, identical scale, identical neutral standing pose with the arms relaxed at the sides and the feet together, a calm closed-mouth expression, eyes level to camera in the front view. Head to feet fully visible in every view with even headroom. Even soft studio lighting from a large front-left octabox with broad fill, no hard shadows, no rim light, no colour cast. She is the WOMAN: the singer and the protagonist, one and the same person — a young southern Iranian woman in her mid twenties. Her face must match the portrait reference exactly and is defined by four features that must never change: FIRST, pale green-grey eyes, large and almond-shaped, with a distinct darker limbal ring and long dark lashes — her eyes are green, never brown. SECOND, very thick, straight, dark, low-set eyebrows with only a slight arch, sitting close above the eyes. THIRD, full lips with a sharply defined cupid's bow, the lower lip fuller, natural rose colour. FOURTH, a narrow straight nose with a small defined rounded tip. Beyond those: a soft oval face tapering to a gently pointed chin, high rounded cheekbones with a natural warm flush, fair light-olive skin with fine visible texture and no blemishes, a long neck, and long thick dark brown-black wavy hair. Her expression is calm, level and unflinching; she holds very still, shoulders squared, and carries grief quietly rather than performing it wearing wardrobe: a long loose ankle-length ivory-cream kurta of soft slubbed cotton-silk, wide elbow-length kimono sleeves with a gold-embroidered cuff band, a small V neckline framed by a diamond-shaped maroon-and-gold embroidered panel, and scattered small gold paisley motifs across the body, the hem finished with a gold embroidered border and cut longer at the sides; matching ivory straight trousers with a densely gold-embroidered panel at each ankle; a long deep-maroon chiffon shawl draped over the left shoulder with both ends hanging loose and floating in the wind; layered gold jewellery — a delicate gold head-chain across the forehead with small hanging gold leaves and a round central medallion, a long two-tier gold coin-and-pendant necklace over the chest; henna patterns on the backs of both hands; cream platform wedge sandals; her hair worn loose, long and wavy, uncovered. Reproduce the garment's exact cut, embroidery placement, drape and colour from the reference. Photorealistic, 85mm lens, sharp focus edge to edge, flat uniform background, no props, no text, no panel numbers.
```

#### CS-02 · ★ شیت ترکیبی حالت + نور (کلید پیوستگی)

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی ۱: CS-01 · ورودی ۲: REF-01
- **اندازه:** `2752x1536`
- **نکته:** سه شیت در یکی، برای کم‌کردن هزینه. برای هر پلان، پنلی را که نورش با آن صحنه می‌خواند به مدل ویدیو بده.

```text
A six-panel reference sheet of the exact same woman from the reference images, six head-and-shoulders portraits in two rows of three, identical scale, identical three-quarter angle, identical face with pale green-grey eyes and very thick straight dark eyebrows, identical gold head-chain and ivory embroidered neckline. Only expression and lighting change. Top row, three expressions under the same flat soft light: a neutral resting face with lowered eyes; singing softly with the mouth half open and the jaw moving; the mouth closed with the jaw set and the chin lifted. Bottom row, the same neutral expression under three different lights: hazy bleached high sun in an open courtyard with deep shadow under the brow; hard raking low sun from the side on a salt flat with wind lifting the maroon shawl; soft shaded light from a dark interior with a blown-out bright doorway behind her. Restrained, interior, non-theatrical emotion throughout. She is the WOMAN: the singer and the protagonist, one and the same person — a young southern Iranian woman in her mid twenties. Her face must match the portrait reference exactly and is defined by four features that must never change: FIRST, pale green-grey eyes, large and almond-shaped, with a distinct darker limbal ring and long dark lashes — her eyes are green, never brown. SECOND, very thick, straight, dark, low-set eyebrows with only a slight arch, sitting close above the eyes. THIRD, full lips with a sharply defined cupid's bow, the lower lip fuller, natural rose colour. FOURTH, a narrow straight nose with a small defined rounded tip. Beyond those: a soft oval face tapering to a gently pointed chin, high rounded cheekbones with a natural warm flush, fair light-olive skin with fine visible texture and no blemishes, a long neck, and long thick dark brown-black wavy hair. Her expression is calm, level and unflinching; she holds very still, shoulders squared, and carries grief quietly rather than performing it wearing wardrobe: a long loose ankle-length ivory-cream kurta of soft slubbed cotton-silk, wide elbow-length kimono sleeves with a gold-embroidered cuff band, a small V neckline framed by a diamond-shaped maroon-and-gold embroidered panel, and scattered small gold paisley motifs across the body, the hem finished with a gold embroidered border and cut longer at the sides; matching ivory straight trousers with a densely gold-embroidered panel at each ankle; a long deep-maroon chiffon shawl draped over the left shoulder with both ends hanging loose and floating in the wind; layered gold jewellery — a delicate gold head-chain across the forehead with small hanging gold leaves and a round central medallion, a long two-tier gold coin-and-pendant necklace over the chest; henna patterns on the backs of both hands; cream platform wedge sandals; her hair worn loose, long and wavy, uncovered. Photorealistic, 85mm lens, visible skin texture, no retouching, no text, no labels, no borders.
```

#### CS-03 · ★ شیت شالِ روی سر + حرکت پارچه

- **حالت:** Qwen-Image-2.1 · Image Edit — ورودی ۱: CS-01 · ورودی ۲: REF-01
- **اندازه:** `2752x1536`
- **نکته:** حالت دوم لباس، مخصوص پلان‌های قبرستان (S07 و S09). بادِ جنوب امضای بصری کلیپ است — این شیت به مدل ویدیو یاد می‌دهد پارچه چطور باید حرکت کند.

```text
A four-panel wardrobe study of the exact same woman from the reference images on a flat neutral light-grey background, four views at identical height and scale, her face identical in all four with pale green-grey eyes and very thick straight dark eyebrows. Panel one: a full-body front view wearing wardrobe, shawl-up variant: exactly the same ivory-cream embroidered kurta, ivory trousers with gold ankle panels, gold head-chain, gold coin necklace and henna hands, but the deep-maroon chiffon shawl is now pulled up over her head like a veil, framing her face, the gold head-chain still visible at her forehead beneath it, both ends of the shawl hanging down her front and lifting in the wind; a few strands of her dark hair escaping at the temples, standing still, the shawl hanging straight. Panel two: the same, with a strong side wind lifting the shawl away from her face and pressing the kurta against one leg. Panel three: a three-quarter view from behind showing how the maroon shawl sits over the back of her head and shoulders. Panel four: a tight close-up of her face framed by the maroon shawl with the gold head-chain visible at her forehead beneath it. Even soft studio lighting in every panel. She is the WOMAN: the singer and the protagonist, one and the same person — a young southern Iranian woman in her mid twenties. Her face must match the portrait reference exactly and is defined by four features that must never change: FIRST, pale green-grey eyes, large and almond-shaped, with a distinct darker limbal ring and long dark lashes — her eyes are green, never brown. SECOND, very thick, straight, dark, low-set eyebrows with only a slight arch, sitting close above the eyes. THIRD, full lips with a sharply defined cupid's bow, the lower lip fuller, natural rose colour. FOURTH, a narrow straight nose with a small defined rounded tip. Beyond those: a soft oval face tapering to a gently pointed chin, high rounded cheekbones with a natural warm flush, fair light-olive skin with fine visible texture and no blemishes, a long neck, and long thick dark brown-black wavy hair. Her expression is calm, level and unflinching; she holds very still, shoulders squared, and carries grief quietly rather than performing it. Photorealistic, 85mm and 100mm lens looks, accurate lightweight chiffon behaviour, no text, no labels.
```

#### CS-04 · شیت کاراکتر — پسر (۹ ساله)

- **حالت:** Qwen-Image-2.1 · Text to Image
- **اندازه:** `2048x2048`
- **نکته:** پسر فقط در پلان آخر و برای یک ثانیه دیده می‌شود — همیشه زنده و خندان. هرگز صحنه‌ی مرگ، جسد یا تشییع نساز.

```text
Character reference sheet of one young boy on a flat neutral light-grey seamless background: a full-body front view and an exact ninety-degree left profile at identical height and scale in a relaxed standing pose, plus two smaller inset panels beside them, one tight neutral portrait and one tight portrait smiling openly at camera with a half-raised hand. He is the BOY (her son, 7, a first-grader): a southern Iranian child on his first year of school; a small round sun-browned face, large dark eyes with long lashes, close-cropped black hair, two slightly large front teeth with a narrow gap, a scattering of tiny freckles across the nose; the Iranian primary-school uniform worn slightly too big for him: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile. Even soft studio lighting, warm and alive, photorealistic, 85mm lens, sharp focus, no text, no labels.
```


### پراپ‌ها

#### PS-01 · شیت پراپ — کیف، دفتر، زنگ

- **حالت:** Qwen-Image-2.1 · Text to Image (خروجی RGBA)
- **اندازه:** `2048x2048`
- **نکته:** خروجی شفاف بگیر تا همین پراپ‌ها را در فریم‌های دیگر کامپوزیت کنی و شکلشان هرگز عوض نشود.

```text
A clean prop reference sheet, three objects photographed separately on a transparent background with an alpha channel, side by side at consistent scale: first the SCHOOLBAG: a first-grader's rectangular Iranian school satchel in exactly the same deep maroon as her chiffon shawl, stiff vinyl with a single brass buckle and one flat front pocket, brand-new and unscuffed, small enough for a seven-year-old, with a hand-sewn white cotton name tag stitched inside the flap — her shawl and this satchel are the only two warm saturated things in the entire film and they are the same red in a three-quarter view with the flap closed and again with the flap open; second the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections closed and again open flat seen from directly above but slightly out of focus so no letterform is legible; third the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a turquoise-painted steel door, green patina in the grooves, the clapper visible inside in a straight side view. Even soft studio lighting from above and slightly left, soft contact shadow only, accurate material response for stiff vinyl, cheap soft paper and aged brass. Photorealistic, macro clarity, 100mm lens, transparent background, no text, no branding.
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
brown eyes, hazel eyes, dark eyes, thin eyebrows, plucked eyebrows, arched eyebrows, changed face, different woman, aged face, wrinkles, text, letters, words, arabic script, persian script, watermark, logo, signature, caption, subtitles, ui, extra fingers, six fingers, deformed hands, fused fingers, extra limbs, distorted face, asymmetrical eyes, plastic skin, waxy skin, beauty retouching, smoothed skin, oversharpened, hdr glow, oversaturated, neon, cartoon, anime, 3d render, cgi, video game, illustration, painting, sketch, blurry, low resolution, jpeg artifacts, duplicate people, cloned faces, upright headstones, western cemetery, crosses, church, coffins, blood, injury, corpse, western school uniforms, blazers, ties, jeans with logos, modern sneakers, smartphones, lens flare, tilted horizon, fisheye, heavy vignette, snow, forest, skyscrapers
```
