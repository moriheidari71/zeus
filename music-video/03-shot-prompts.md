# ۰۳ — پرامپت پلان‌به‌پلان · «نَزنید زنگ»

> این فایل **به‌صورت خودکار** از `prompts.json` ساخته می‌شود.
> دست نزن؛ اگر خواستی چیزی عوض کنی `prompts.json` را ویرایش کن و دوباره اجرا کن:
> `python3 music-video/build_prompts.py`

- نسبت تصویر مستر: **16:9** · رزولوشن: **2K (2752x1536 برای Qwen / 2K برای H3)** · نرخ فریم: **24fps** · زمان هدف: **03:30**
- کات عمودی: 9:16 (کات عمودی برای ریلز)
- **نگتیو پرامپت مشترک** برای همه‌ی تصاویر در انتهای همین فایل و در `out/NEGATIVE.txt`.

## جدول خلاصه‌ی پلان‌ها

| # | تایم‌کد | ثانیه | دسته | عنوان | موتور پیشنهادی |
|---|---------|-------|------|-------|----------------|
| S01 | 00:00–00:08 | 8 | B | بوی کیف نو | LTX-2.5 Fast |
| S02 | 00:08–00:14 | 6 | B | دست‌های مادر | MiniMax H3 (i2v) |
| S03 | 00:14–00:22 | 8 | A | ورود خواننده | MiniMax H3 (reference-to-video) |
| S04 | 00:22–00:28 | 6 | B | دفتر نو | LTX-2.5 Fast |
| S05 | 00:28–00:38 | 10 | C | کوچه — خواننده در میان بچه‌ها | Seedance 2.0 |
| S06 | 00:38–00:46 | 8 | B | مادر پشت در | MiniMax H3 (i2v) |
| S07 | 00:46–00:58 | 12 | A | کلوزآپ اجرا — دیوار گچی | MiniMax H3 (ref2v, 2K) |
| S08 | 00:58–01:03 | 5 | B | دستِ سرایدار و طناب زنگ | LTX-2.5 Pro |
| S09 | 01:03–01:11 | 8 | B | مادر در حیاط خالی — «نزنید» | MiniMax H3 (i2v, 2K) |
| S10 | 01:11–01:17 | 6 | B | زنگ نیمه‌راه و پرواز گنجشک‌ها | LTX-2.5 Fast |
| S11 | 01:17–01:25 | 8 | C | خواننده روی پله‌ها، بچه‌ها محو | Seedance 2.0 |
| S12 | 01:25–01:35 | 10 | B | قبرستان تپه‌ای — نمای معرف | LTX-2.5 Fast (2K یا 4K) |
| S13 | 01:35–01:41 | 6 | B | قلمِ حکاکی روی سنگ | LTX-2.5 Pro |
| S14 | 01:41–01:51 | 10 | C | خواننده کنار سنگ — شستنِ سنگ | MiniMax H3 (ref2v, 2K) |
| S15 | 01:51–01:57 | 6 | B | کیف، کنار سنگ | LTX-2.5 Fast |
| S16 | 01:57–02:05 | 8 | B | دفتر، انگشتِ مادر، قطره | MiniMax H3 (i2v, 2K) |
| S17 | 02:05–02:13 | 8 | B | خاطره — پسر در حال نوشتن | MiniMax H3 (i2v) |
| S18 | 02:13–02:18 | 5 | B | خاطره — گرد گچ و خنده | LTX-2.5 Fast |
| S19 | 02:18–02:26 | 8 | A | کلوزآپ اجرا — چشم‌های خیس | MiniMax H3 (ref2v, 2K) |
| S20 | 02:26–02:36 | 10 | B | کلاس، نیمکت خالی | MiniMax H3 (2K) |
| S21 | 02:36–02:42 | 6 | B | دفتر حضور و غیاب | LTX-2.5 Pro |
| S22 | 02:42–02:50 | 8 | C | خواننده، انتهای کلاس | Seedance 2.0 |
| S23 | 02:50–03:00 | 10 | B | باران و قایق کاغذی | LTX-2.5 Fast |
| S24 | 03:00–03:10 | 10 | B | مادر روی پله‌های خیس | MiniMax H3 (2K) |
| S25 | 03:10–03:18 | 8 | A | خواننده زیر باران — نمای باز | MiniMax H3 (ref2v, 2K) |
| S26 | 03:18–03:22 | 4 | B | زنگ می‌خورد | MiniMax H3 |
| S27 | 03:22–03:34 | 12 | B | حیاط پر می‌شود — صف صبحگاه | Seedance 2.0 (multi-shot) |
| S28 | 03:34–03:44 | 10 | C | آخرین ردیف — پسر برمی‌گردد | MiniMax H3 (first & last frame) |
| S29 | 03:44–03:50 | 6 | B | پایان — دو گزینه | LTX-2.5 Pro |
| S30 | 03:50–04:00 | 10 | B | سنگ، غروب، گنجشک | LTX-2.5 Fast |

**جمع کل: 30 پلان · 240 ثانیه ≈ 4:00**

توزیع: 4 پلان [A] اجرای خواننده · 21 پلان [B] تصویرسازی محض · 5 پلان [C] خواننده داخل صحنه

---


## سکانس ۱ — اینترو / خانه، سحر

### S01 · بوی کیف نو  `00:00–00:08` · 8s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3 (i2v)
- **چرا:** پلان طولانی، بی‌چهره، با تغییر آرام نور — دقیقاً نقطه‌قوت LTX؛ ارزان و می‌شود ۸ تا ۱۲ ثانیه گرفت.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-03 (پنل خانه)
- **صدا:** آمبیانس سحر. زیر ملودی ساز مقدمه با حجم خیلی کم.
- **نکته:** با LTX می‌توانی فریم اول و آخر را هر دو بدهی تا حرکت نور دقیقاً کنترل شود (image + last_frame_image).

**۱) فریم اول — Qwen-Image-2.1**

```text
Extreme close-up in near-darkness. the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap stands upright on a bare concrete floor beside a folded school uniform, inside the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain. A single narrow blade of pale dawn light enters from a gap in the curtain and lies across the brass buckle and the stitched name tag. Dust motes hang in the beam. Everything outside the beam falls to deep blue-black. Macro 100mm lens, extremely shallow depth of field, focus on the buckle. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Locked-off macro shot, the camera does not move for the entire clip. Over eight seconds the narrow blade of dawn light creeps slowly across the satchel from the buckle towards the stitched name tag, widening by a few centimetres and warming very slightly from blue to pale amber. Dust motes drift lazily through the beam, some catching the light and flaring for an instant. Nothing else in the frame moves. No people, no hands. Preserve the exact shape, colour and stitching of the satchel. Soundscape: deep room tone, a distant rooster, a far-off motorcycle, a curtain breathing against a window frame. No music, no voices.
```

**۲ب) فریم پایانی برای اینترپولیشن (LTX `last_frame_image`)**

```text
The same macro frame, the light now fully across the name tag and warmer, the rest of the room still dark.
```

<sub>بلوک‌های استفاده‌شده: BAG, HOME, NOW</sub>

---
### S02 · دست‌های مادر  `00:08–00:14` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (i2v)  ·  **جایگزین:** LTX-2.5 Pro
- **چرا:** دستِ انسانی در حرکت آهسته؛ H3 در فیزیک دست و پارچه از بقیه پایدارتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-06، LS-03 (پنل خانه)
- **صدا:** صدای پارچه و یک نفسِ لرزان — زیر موسیقی نگه دار.
- **نکته:** قانون کلیپ: صورت مادر تا پلان S09 دیده نمی‌شود.

**۱) فریم اول — Qwen-Image-2.1**

```text
Close shot from above, hands only, no face in frame. The weathered working hands of the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk smooth a folded pale blue-grey school shirt flat on a red-and-blue kilim inside the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain. Beside the shirt lies the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap. One hand rests flat on the fabric, the other has just turned back the collar to show a small hand-sewn name tag. Soft grey window light from the left. 50mm lens, shallow depth of field on the hands. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (i2v)**

```text
Static overhead shot, the camera holds absolutely still. Over six seconds the two hands smooth the folded shirt outward from the centre in one slow, repeated pressing motion, the fabric flattening under the palms. The right hand then lifts, hovers for a beat, and comes to rest on the collar without moving again. The fingers tremble very slightly at the end. No face enters the frame at any point. Preserve the exact colours of the kilim, the shirt and the satchel. Soundscape: the dry whisper of cotton under a palm, one deep unsteady breath, a ticking clock in another room. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: BAG, HOME, M, NOW</sub>

---
### S03 · ورود خواننده  `00:14–00:22` · 8s
**[A] اجرای خواننده — لب‌خوانی / حضور مستقیم**

- **موتور:** MiniMax H3 (reference-to-video)  ·  **جایگزین:** Seedance 2.0 (i2v)
- **چرا:** اولین بار که چهره‌ی خواننده را می‌بینیم — قفل هویت باید بیشترین دقت را داشته باشد. H3 تا ۹ تصویر رفرنس می‌گیرد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-03، CS-05 (پنل ۱)، LS-03 (پنل خانه)
- **صدا:** آخرین ضربِ سکوت قبل از شروع کلام.
- **نکته:** در H3 تصاویر رفرنس را با role=reference_image بفرست و در متن بنویس the man is the person in the reference images.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium wide shot. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns stands motionless in the open doorway of the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain, seen from inside the room. He is backlit by cold blue dawn light from the yard behind him so his figure reads as a dark silhouette with a thin rim on the shoulder and cheek, only enough bounce to hold his eyes. He looks down and to the left, towards the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap on the floor in the near foreground, out of focus. Shot from a low seated height. 35mm lens. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (reference-to-video)**

```text
A slow, almost imperceptible push in towards the man in the doorway over the full eight seconds, no more than a ten percent move. He does not walk in. He stands completely still, then takes one slow breath that lifts his shoulders, lowers his eyes further towards the floor, and closes them for a beat near the end. The light behind him brightens very slightly. Keep his face, beard, hair and clothing exactly as in the reference images. Preserve the doorway geometry and the silhouette. Soundscape: a distant street waking up, a metal door far away, wind in a courtyard. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: BAG, HOME, NOW, S, WA</sub>

---

## سکانس ۲ — بند اول / «بوی کیف و کتاب نو میاید»

### S04 · دفتر نو  `00:22–00:28` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3
- **چرا:** پلان شیء، بدون چهره؛ ارزان‌ترین و سریع‌ترین مسیر و کیفیت ماکرو عالی.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01
- **صدا:** صدای ورق — یکی از موتیف‌های صوتی کلیپ.
- **نکته:** خط فارسی را عمداً آف‌فوکوس نگه دار؛ هیچ مدلی خط فارسی را درست نمی‌نویسد. جزئیات در فایل ۰۴.

**۱) فریم اول — Qwen-Image-2.1**

```text
Macro shot, straight down onto the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections lying closed on a dark wooden surface, a brand-new blue ballpoint pen beside it. The cover is fresh and uncreased. A shaft of soft window light falls across the top corner. Faint paper fibres catch the light along the cut edge of the pages. 100mm macro lens, very shallow depth of field, focus on the near corner of the cover. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Locked-off overhead macro, no camera movement. Over six seconds the cover of the notebook lifts by itself as if breathed on, and the pages riffle open slowly from the first to the last, one after another, each page settling with a soft ripple. A fine puff of pale paper dust rises off the paper and drifts up through the light. The last page settles and holds. No hands enter the frame. Keep the handwriting soft and out of focus so no individual letter is legible. Soundscape: the dry flutter of turning paper, a soft intake of breath, distant sparrows. No music.
```

<sub>بلوک‌های استفاده‌شده: NOTE, NOW</sub>

---

## سکانس ۲ — بند اول

### S05 · کوچه — خواننده در میان بچه‌ها  `00:28–00:38` · 10s
**[C] خواننده داخل صحنه — شاهدِ خاموش**

- **موتور:** Seedance 2.0  ·  **جایگزین:** MiniMax H3 (ref2v)
- **چرا:** چندین آدم متحرک + قفل هویت یک نفر + امکان چندشات در یک رندر. این دقیقاً کاری است که Seedance 2.0 برایش ساخته شده.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01 → @Image1، LS-01 → @Image2، CS-05 پنل ۱ → @Image3
- **صدا:** همهمه‌ی بچه‌ها را در میکس فقط ۱۵٪ باز کن، بقیه موسیقی.
- **نکته:** قانون [C]: هیچ‌کس خواننده را نمی‌بیند. او شاهد است، نه شخصیت.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide shot down the ALLEY: a narrow alley of packed dirt and cracked asphalt between mud-brick and cement-block houses, blue-painted steel doors, an open water channel along one edge, one leaning concrete pole with tangled wires, dry plane-tree leaves blown against the walls at early morning. Eight to ten Iranian primary-school children in uniform, seen mostly from behind, walk away from camera towards a wide blue metal gate at the far end. In the exact centre of the alley, facing camera and perfectly still, stands the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns. The children flow past him on both sides without looking at him. Dry leaves on the ground, cold flat light, long alley perspective. 35mm lens, deep focus. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — Seedance 2.0**

```text
@Image1 is the man: keep his face, beard, hair and clothing identical to it. @Image2 is the location style. @Image3 is the lighting reference. Shot 1, zero to four seconds: a static wide down the alley, the children walking away from camera towards the blue gate, satchels swinging, one child skipping. The man stands motionless in the centre facing camera, the only still thing in the frame. Shot 2, four to seven seconds: cut to a low shot at child height passing the man's legs as the children stream by, his trousers and the hem of his overshirt still. Shot 3, seven to ten seconds: cut back to the wide, the last child reaching the gate, and the man slowly lifting his eyes to camera. Handheld is forbidden, all three shots are locked off. Cool overcast morning light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Audio: footsteps on gravel, children's voices far off and unintelligible, a distant gate, wind.
```

<sub>بلوک‌های استفاده‌شده: ALLEY, NOW, S, WA</sub>

---
### S06 · مادر پشت در  `00:38–00:46` · 8s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (i2v)  ·  **جایگزین:** LTX-2.5 Pro
- **چرا:** بازی بدنی ظریف یک شخصیت؛ H3 در میکرو-اکسپرشن و وزن بدن بهترین گزینه‌ی توست.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-06، PS-01
- **صدا:** باد — موتیف صوتی سکانس‌های بیرونی.
- **نکته:** اگر H3 صورتش را جوان کرد، در پرامپت تصویر «deep nasolabial folds, no retouching» را تکرار کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium shot from outside, looking into the open doorway of a village house on the ALLEY: a narrow alley of packed dirt and cracked asphalt between mud-brick and cement-block houses, blue-painted steel doors, an open water channel along one edge, one leaning concrete pole with tangled wires, dry plane-tree leaves blown against the walls. the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk stands just inside the threshold holding the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap flat against her chest with both arms. Her body is in the doorway's shadow, her face catching a little cold bounce from the alley. She looks off to the left, down the alley, not at camera. The door frame boxes her tightly. 50mm lens. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (i2v)**

```text
Static locked-off shot. Over eight seconds the woman stays in the doorway and does not step out. She tightens both arms around the satchel, shifts her weight once onto the other foot, and turns her head slowly to follow something moving down the alley from left to right. Near the end her chin lifts a little and her mouth presses closed. She does not cry. Her scarf edge moves faintly in the wind. Preserve her face, scarf pattern, dress colour and the satchel exactly. Soundscape: wind down a narrow alley, faint children far away, a plastic bag scraping across the ground. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: ALLEY, BAG, M, NOW</sub>

---
### S07 · کلوزآپ اجرا — دیوار گچی  `00:46–00:58` · 12s
**[A] اجرای خواننده — لب‌خوانی / حضور مستقیم**

- **موتور:** MiniMax H3 (ref2v, 2K)  ·  **جایگزین:** Seedance 2.0 (i2v)
- **چرا:** لب‌خوانی کلوزآپ. H3 در ۲K با رفرنس چندتایی بالاترین وفاداری چهره را می‌دهد. برای ۱۲ ثانیه یک‌جا رندر کن.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل «singing softly»)، CS-03، CS-05 (پنل ۲)
- **صدا:** کاملاً میوت. فقط تصویر روی آهنگ اصلی.
- **نکته:** برای لب‌خوانی: پلان را بدون صدای مدل بگیر و در تدوین روی آهنگ سینک کن. اگر سینک لب دقیق می‌خواهی، در Seedance 2.0 فایل صوتیِ همان مصرع را به‌عنوان @Audio1 بده.

**۱) فریم اول — Qwen-Image-2.1**

```text
Tight close-up, head and shoulders. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns stands against a rough whitewashed wall smeared with chalk ghosting, slightly off centre in the frame with negative space to the right. A hard slash of dusty window light crosses his cheekbone and leaves the other half of his face in soft shadow. Fine chalk dust hangs in the light. He looks just past the lens, not into it. 85mm lens, shallow depth of field, the wall softly out of focus. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (ref2v, 2K)**

```text
Extremely slow push in over twelve seconds, no more than an eight percent move, ending on a tighter close-up. He sings quietly and steadily, the mouth opening and closing with clear natural articulation, the jaw moving, the throat working, small breaths between phrases. His eyes stay just off-lens and lower once towards the end, then lift again. Chalk dust drifts continuously through the light beam behind and in front of him. No head turn, no gesture, no hand enters the frame. Keep his face, beard, hair and clothing exactly as in the reference images. Soundscape: a quiet interior room tone and faint chalk-dry air. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: NOW, S, WA</sub>

---

## سکانس ۳ — کُرس اول / «نزنید زنگ و تا بچم بیاید»

### S08 · دستِ سرایدار و طناب زنگ  `00:58–01:03` · 5s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Pro  ·  **جایگزین:** MiniMax H3
- **چرا:** پلان کوتاه و پرجزئیات با یک حرکت مکانیکی ساده؛ Pro کیفیت و پایداری بالاتری در ۵ ثانیه می‌دهد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01
- **صدا:** سکوتِ عمدی. زنگ نباید به صدا دربیاید.
- **نکته:** این پلان و S10 با هم یک جمله‌ی بصری‌اند: «نزنید».

**۱) فریم اول — Qwen-Image-2.1**

```text
Tight shot. the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a blue-painted steel door, green patina in the grooves, the clapper visible inside hangs from its hemp rope beside a blue-painted steel door in the corner of the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate. An old man's weathered hand, sleeve of a grey work jacket, enters from the right edge of frame and reaches for the rope, the fingers not yet closed around it. Cold flat overcast light. Green patina and brass highlights. 85mm lens, shallow focus on the bell, the hand slightly soft. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Pro**

```text
Static locked-off shot. Over five seconds the weathered hand moves the last few centimetres towards the hemp rope and the fingers begin to close around it, slowing as they touch, and the clip ends exactly at the moment of contact before any pull. The rope sways a millimetre from the touch. The bell itself does not ring and does not swing. Nothing else moves. Preserve the exact shape, patina and rope of the bell. Soundscape: an empty courtyard, wind, the creak of rope fibre. Absolutely no bell sound.
```

<sub>بلوک‌های استفاده‌شده: BELL, NOW, SCHOOL</sub>

---

## سکانس ۳ — کُرس اول

### S09 · مادر در حیاط خالی — «نزنید»  `01:03–01:11` · 8s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (i2v, 2K)  ·  **جایگزین:** Seedance 2.0
- **چرا:** اوج احساسی بند. حرکت کاملِ بدن در فضای باز + یک ژست مشخص؛ H3 بهترین کنترل بدن را دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-06، LS-01 (پنل high wide)
- **صدا:** اکو قدم‌ها در حیاط خالی — بعد سکوت.
- **نکته:** خالی‌بودن حیاط مهم است. اگر مدل آدم اضافه کرد، در پرامپت تصویر «completely empty, no other people, no children» را تکرار کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
High wide shot from a second-floor window looking down into the completely empty courtyard of the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate. the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk is small in the centre of the grey hexagonal tiles, alone, caught mid-stride running towards the corner where the bell hangs, one arm raised high with the palm open in a stop gesture, the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap still clutched in the other hand. The vast empty tiled courtyard surrounds her on all sides. Flat cold overcast light, no shadows. 24mm lens, deep focus. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (i2v, 2K)**

```text
The camera holds high and static for the whole clip. Over eight seconds the woman runs four or five heavy, unathletic steps towards the far corner, her raised arm staying up, her dress and scarf trailing. She slows, stumbles half a step, and stops dead in the middle of the empty courtyard, the raised arm slowly falling to her side. She stands there, very small in the frame, and does not move again. Keep her exactly as in the reference image. Preserve the tile pattern and the courtyard architecture. Soundscape: running footsteps echoing off courtyard walls, one sharp breath, then wind and total emptiness. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: BAG, M, NOW, SCHOOL</sub>

---
### S10 · زنگ نیمه‌راه و پرواز گنجشک‌ها  `01:11–01:17` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3
- **چرا:** حرکت سریع پرنده‌ها روی یک شیء ساکن — LTX دیکودر جدیدش موشن پرنده را تمیزتر می‌دهد و می‌توانی ۴۸fps بگیری و در تدوین اسلوموشن کنی.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01 (پنل درخت چنار)
- **صدا:** انفجارِ بال‌ها — نقطه‌ی اوج صوتی. اگر ریتم آهنگ اجازه داد، روی ضرب بیفتد.
- **نکته:** با fps=48 رندر کن و در تدوین روی ۲۴ پخش کن تا اسلوموشن نرم بگیری.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium shot. the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a blue-painted steel door, green patina in the grooves, the clapper visible inside hangs frozen at the top of its swing, tilted, the clapper resting against the inside of the brass without contact. Behind it and slightly out of focus, the mottled trunk and lower branches of the old plane tree in the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, thick with sparrows. Cold overcast sky between the branches. 85mm lens, focus on the bell, the tree soft. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Static locked-off shot. For the first two seconds the bell holds absolutely still at the top of its tilt, unnaturally still. Then all the sparrows burst out of the plane tree at once, thirty small birds scattering upward and out of frame in every direction, a chaos of wings across the soft background. The bell still does not move or ring. As the last bird leaves, a few dry leaves fall through the frame. Preserve the bell's exact shape and patina. Soundscape: two seconds of dead silence, then a violent rush of wings and one sharp collective chirp, then wind and falling leaves. No bell sound at any point.
```

<sub>بلوک‌های استفاده‌شده: BELL, NOW, SCHOOL</sub>

---
### S11 · خواننده روی پله‌ها، بچه‌ها محو  `01:17–01:25` · 8s
**[C] خواننده داخل صحنه — شاهدِ خاموش**

- **موتور:** Seedance 2.0  ·  **جایگزین:** MiniMax H3 (ref2v)
- **چرا:** تضادِ سوژه‌ی تیز و پس‌زمینه‌ی موشن‌بلور با چند فیگور متحرک — Seedance در صحنه‌های چندسوژه‌ای پایدارتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01 → @Image1، LS-01 → @Image2
- **صدا:** همهمه‌ی محو و کمی کشیده — صدای خاطره، نه واقعیت.
- **نکته:** اگر موشن‌بلور کافی نشد، پلان را ۴۸fps بگیر و در تدوین با Frame Blending سرعت را دوبرابر کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium wide shot at eye level. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns sits on the three worn concrete steps of the school building in the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, elbows on knees, hands loose, looking down. Around and in front of him children in uniform run past in both directions, rendered as soft motion blur streaks. He alone is razor sharp. Cold overcast light, the blue-painted wall behind him. 35mm lens, long exposure look, subject sharp, everything moving blurred. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — Seedance 2.0**

```text
@Image1 is the man: keep his face, beard, hair and clothing identical to it. @Image2 is the location. One continuous static shot, the camera never moves. The man on the steps stays almost perfectly still for the full eight seconds, only breathing and once slowly closing and opening his eyes. Around him children run past continuously in both directions, close to camera and far, rendered as smeared motion-blurred streaks with no readable faces, as if shot on a long shutter. The contrast between his stillness and their blur must be extreme. Nobody looks at him, nobody touches him. Cool overcast light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Audio: a wash of playground noise pitched slightly low and blurred, footsteps, no individual voice clear.
```

<sub>بلوک‌های استفاده‌شده: NOW, S, SCHOOL, WA</sub>

---

## سکانس ۴ — بند دوم / «نوشتن اسمتو بر روی سنگت»

### S12 · قبرستان تپه‌ای — نمای معرف  `01:25–01:35` · 10s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast (2K یا 4K)  ·  **جایگزین:** MiniMax H3 (2K)
- **چرا:** پلان منظره‌ی طولانی و آرام، بدون چهره — LTX تا ۲۰ ثانیه و تا ۴K می‌دهد و اینجا ارزان‌ترین کیفیت بالا را می‌گیری.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-03 (پنل قبرستان)
- **صدا:** باد خالص. این پلان نقطه‌ی «تنفس» کلیپ است.
- **نکته:** با 4K/2160p بگیر تا بتوانی در تدوین یک پوش-این دیجیتال نرم روی آن بگذاری.

**۱) فریم اول — Qwen-Image-2.1**

```text
Very wide static landscape shot of the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky. Rows of flat marble slabs recede across the dry ochre hillside towards bare brown hills and a flat pewter sky. In the lower third, slightly left of centre, one slab is newer and paler than all the others. No people anywhere. Wind-bent thorn bushes. 24mm lens, deep focus, level horizon. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast (2K یا 4K)**

```text
Locked-off wide landscape shot, the camera does not move at all for ten seconds. Only the wind is alive: the thorn bushes bend and spring back in gusts, loose dust lifts off the bare earth and travels across the frame from right to left, a few dry leaves tumble between the slabs, and the light shifts almost imperceptibly as a thin cloud passes. No people, no animals, no vehicles enter the frame. The graves must stay flat slabs lying on the ground, never upright headstones. Soundscape: open hillside wind, one distant crow, nothing else. No music.
```

<sub>بلوک‌های استفاده‌شده: CEM, NOW</sub>

---

## سکانس ۴ — بند دوم

### S13 · قلمِ حکاکی روی سنگ  `01:35–01:41` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Pro  ·  **جایگزین:** MiniMax H3
- **چرا:** ماکروی صنعتی با گرد و غبار ریز — Pro در جزئیات و پایداری بافت بهتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-03 (پنل سنگ)
- **صدا:** سه ضربِ خشکِ فلز روی سنگ — می‌تواند روی ضرب آهنگ بیفتد.
- **نکته:** هرگز اجازه نده حرف کامل فارسی حک شود. نوشته‌ی واقعی را در پست روی همین سنگ کامپوزیت کن (راهنما در فایل ۰۴).

**۱) فریم اول — Qwen-Image-2.1**

```text
Extreme macro, almost abstract. The polished grey-white surface of a marble slab fills the frame at a steep raking angle. A steel engraving chisel tip rests in a freshly cut groove, a curl of white marble dust gathered beside it. The cut is only a fragment of a stroke, no letter is complete or legible. Hard low side light rakes across the surface making the groove read as a deep black line. 100mm macro lens, razor-thin depth of field. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Pro**

```text
Locked-off extreme macro, no camera movement. Over six seconds the chisel tip pushes forward along the groove in three short controlled strokes, each one throwing a fine spray of white marble dust up into the raking light. The groove lengthens slightly with each stroke but never forms a complete or readable letter. Dust settles slowly into the cut. The chisel lifts away at the end and the frame holds on the fresh groove. Soundscape: the dry metallic scrape of steel on stone, three times, and fine dust falling. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: NOW</sub>

---
### S14 · خواننده کنار سنگ — شستنِ سنگ  `01:41–01:51` · 10s
**[C] خواننده داخل صحنه — شاهدِ خاموش**

- **موتور:** MiniMax H3 (ref2v, 2K)  ·  **جایگزین:** Seedance 2.0
- **چرا:** تعامل فیزیکی با آب + قفل چهره. H3 هم فیزیک مایع و هم هویت را با هم نگه می‌دارد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-05 (پنل ۳)، LS-03 (پنل سنگ)
- **صدا:** صدای آب روی سنگ — خیلی نزدیک و خیس. یکی از بهترین لایه‌های صوتی کلیپ.
- **نکته:** قوطی آبپاش پلاستیکی سبز یک نشانه‌ی کاملاً ایرانی است؛ حذفش نکن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Medium shot, low camera almost at ground level. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns kneels on one knee beside the GRAVE: an Iranian Muslim grave, a flat polished grey-white marble slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut stems of white stock flowers, dry ochre earth around it on the hillside of the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky, seen in three-quarter profile. He holds a small green plastic watering can and is tipping it over the slab, a thin ribbon of water just beginning to fall. His other palm is flat on the stone. His sleeve is already dark with water. Cold flat overcast light, wind lifting his hair. 35mm lens, shallow focus on him, the rows of slabs soft behind. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (ref2v, 2K)**

```text
Static low shot, the camera does not move. Over ten seconds he pours the water slowly across the marble slab, the thin stream spreading into a bright sheet that runs into the carved border and darkens the stone, then he sets the can down and wipes the wet surface with his flat palm in two slow passes, front to back, the way you would wipe a child's face. He stays kneeling. Near the end he stops with his hand flat on the stone and lowers his head. He does not speak and does not look at camera. Keep his face, beard, hair and clothing exactly as in the reference images. The grave must remain a flat slab on the ground. Soundscape: water poured onto stone, a wet palm dragging across marble, hillside wind, one distant crow. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: CEM, NOW, S, STONE, WA</sub>

---
### S15 · کیف، کنار سنگ  `01:51–01:57` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3
- **چرا:** شیء + باد؛ ساده و ارزان.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-03 (پنل سنگ)
- **صدا:** باد که بلند می‌شود و می‌خوابد — تنفس.
- **نکته:** اسم روی برچسب را در پست بگذار، نه در مدل.

**۱) فریم اول — Qwen-Image-2.1**

```text
Close low shot. the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap stands upright on the dry ochre earth immediately beside the wet edge of the GRAVE: an Iranian Muslim grave, a flat polished grey-white marble slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut stems of white stock flowers, dry ochre earth around it, brand-new and out of place against the dust. The flap is closed. Wind-bent grass at the frame edge. Cold overcast light. 50mm lens, shallow depth of field, the slab wet and dark behind it. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Locked-off close shot, no camera movement. Over six seconds a gust of wind rises, lifts the satchel's flap and holds it open, showing the small white hand-sewn name tag stitched inside, then the gust drops and the flap falls slowly closed again. Dust and a single dry leaf blow past. The satchel itself does not tip over. Keep the satchel's exact colour, shape, buckle and stitching. Soundscape: a rising gust, stiff vinyl flexing, grit across stone. No music.
```

<sub>بلوک‌های استفاده‌شده: BAG, NOW, STONE</sub>

---

## سکانس ۵ — «دلوم تنگه واسه خط قشنگت»

### S16 · دفتر، انگشتِ مادر، قطره  `01:57–02:05` · 8s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (i2v, 2K)  ·  **جایگزین:** LTX-2.5 Pro
- **چرا:** فیزیک قطره و جذب جوهر در کاغذ — H3 در شبیه‌سازی فیزیکی از بقیه جلوتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، CS-06، LS-03 (پنل خانه)
- **صدا:** نفسِ بریده — بسیار کم، فقط یک لایه.
- **نکته:** پلانِ کلیدی مصرع «خط قشنگت». اگر خط واقعی می‌خواهی: خطِ یک بچه‌ی واقعی را اسکن کن و در پست روی کاغذ کامپوزیت کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Overhead macro. the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections lies open on a kilim inside the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain, both pages covered in rows of childish handwriting, deliberately soft and out of focus so no word is legible. One weathered index finger of the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk rests at the start of a line, about to trace it. Soft grey window light from the left, a warm pool of lamplight at the top edge of frame. 100mm macro lens, shallow depth of field, focus on the fingertip and the paper texture. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (i2v, 2K)**

```text
Locked-off overhead macro, no camera movement. Over eight seconds the fingertip travels very slowly along one line of writing from right to left, barely touching the paper, and stops halfway. It hovers, trembling. Then a single tear drops onto the page beside the finger and the paper darkens in a slowly spreading circle, the blue ink at its edge blooming and feathering outward into the wet fibres. The finger does not move again. No face enters the frame. Keep the handwriting soft and unreadable throughout. Soundscape: a single unsteady breath, the faintest rustle of paper, a clock in another room. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: HOME, M, NOTE, NOW</sub>

---

## سکانس ۵ — «دلوم تنگه واسه خط قشنگت» / خاطره

### S17 · خاطره — پسر در حال نوشتن  `02:05–02:13` · 8s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (i2v)  ·  **جایگزین:** Seedance 2.0
- **چرا:** بازیِ کودک با جزئیات صورت؛ H3 در میکرو-اکسپرشن کودک طبیعی‌تر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-07، LS-03 (پنل خانه)، PS-01
- **صدا:** صدای خودکار روی کاغذ — گرم و نزدیک.
- **نکته:** دنیای خاطره همیشه گرم، کمی اوورکسپوز و با گرین بیشتر. در گرید جدا نگهش دار.

**۱) فریم اول — Qwen-Image-2.1**

```text
Warm intimate medium close-up. the BOY (Yasin, 9): an Iranian primary-school boy; a round face, large dark-brown eyes with long lashes, thick straight black hair with a stubborn cowlick at the crown, slightly large front teeth with a narrow gap, light olive skin, a healing scratch on the right knee; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile lies on his stomach on the kilim in the HOME: a modest Iranian village room, a red-and-blue kilim over a bare concrete floor, a folded cloth sofreh in the corner, whitewashed plaster alcove shelves holding a Quran and one framed photograph turned face-down, a single bare hanging bulb, a small enamel gas heater, and a window with a thin lace curtain, propped on his elbows, writing in the NOTEBOOK: a thin Iranian forty-page school notebook with a pale mint-green cover, soft cheap paper, lined pages covered in careful right-to-left childish handwriting in blue ballpoint, the letters round, even and slightly too large, with a few erased corrections with a blue ballpoint, the tip of his tongue caught at the corner of his mouth in concentration. Eraser crumbs and a curl of pencil shaving beside the notebook. A single bare bulb above spills honey-gold light onto his hair and the page. Everything else falls into warm shadow. 50mm lens, shallow depth of field on his eyes. LOOK-MEMORY: warm 16mm memory photography, honey-golden low sun, half a stop overexposed, soft bloom and heavy halation, visible film grain and faint gate weave, faded reds and creamy whites, dreamy shallow focus.
```

**۲) ویدیو — MiniMax H3 (i2v)**

```text
Very slow drift in from the side, no more than five percent, or hold completely static. Over eight seconds the boy writes steadily, his hand moving right to left across the page in small careful strokes, his head tilting with the line, his tongue still at the corner of his mouth. He pauses, frowns at what he wrote, rubs it out with a small eraser and blows the crumbs off the page, then glances up and off-camera with a quick open smile as if someone spoke to him, and goes straight back to writing. Warm golden lamplight, soft bloom, LOOK-MEMORY: warm 16mm memory photography, honey-golden low sun, half a stop overexposed, soft bloom and heavy halation, visible film grain and faint gate weave, faded reds and creamy whites, dreamy shallow focus. Keep his face, hair and uniform exactly as in the reference image. Soundscape: a ballpoint scratching on cheap paper, an eraser, a short puff of breath, a kettle somewhere far away. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: HOME, K, MEM, NOTE</sub>

---

## سکانس ۵ — خاطره

### S18 · خاطره — گرد گچ و خنده  `02:13–02:18` · 5s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3
- **چرا:** حرکت ذرات و کات به سفید — LTX در پارتیکل و بلوم تمیز است و برای ۵ ثانیه ارزان.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-07، LS-02
- **صدا:** خنده‌ی بچه که ناگهان بریده می‌شود — بی‌رحم‌ترین کاتِ کلیپ.
- **نکته:** خروجیِ سفیدِ آخر، ترنزیشن به S19 است. در تدوین از همان سفید کات بزن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Close-up, low angle. the BOY (Yasin, 9): an Iranian primary-school boy; a round face, large dark-brown eyes with long lashes, thick straight black hair with a stubborn cowlick at the crown, slightly large front teeth with a narrow gap, light olive skin, a healing scratch on the right knee; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile stands at the green chalkboard in the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light, holding a chalkboard eraser thick with chalk dust up in front of his mouth, cheeks puffed, eyes bright and already laughing, about to blow. A shaft of warm golden window light comes from behind him and lights the dust already floating around his head. 50mm lens, shallow focus on his eyes. LOOK-MEMORY: warm 16mm memory photography, honey-golden low sun, half a stop overexposed, soft bloom and heavy halation, visible film grain and faint gate weave, faded reds and creamy whites, dreamy shallow focus.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Static close-up. Over five seconds the boy blows hard across the eraser and a thick cloud of white chalk dust explodes towards camera, filling the frame from the centre outward. Through the cloud he throws his head back laughing, only briefly visible. The dust keeps expanding until it whites out the entire frame by the final half second. Warm backlight through the dust, heavy bloom, LOOK-MEMORY: warm 16mm memory photography, honey-golden low sun, half a stop overexposed, soft bloom and heavy halation, visible film grain and faint gate weave, faded reds and creamy whites, dreamy shallow focus. Keep his face and hair exactly as in the reference image. Soundscape: one sharp puff of breath and a bright child's laugh cut short. No music.
```

<sub>بلوک‌های استفاده‌شده: CLASS, K, MEM</sub>

---

## سکانس ۵ — «دلوم تنگه واسه خط قشنگت»

### S19 · کلوزآپ اجرا — چشم‌های خیس  `02:18–02:26` · 8s
**[A] اجرای خواننده — لب‌خوانی / حضور مستقیم**

- **موتور:** MiniMax H3 (ref2v, 2K)  ·  **جایگزین:** Seedance 2.0 (i2v + @Audio)
- **چرا:** نزدیک‌ترین پلان کلیپ به چهره‌ی خواننده. فقط H3 با ۴ رفرنس هم‌زمان.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-02 (پنل «eyes wet, staring to camera»)، CS-03، CS-05 (پنل ۳)
- **صدا:** میوت. آهنگ اصلی روی تصویر.
- **نکته:** اگر مدل صورت را بیش‌ازحد صاف کرد: «visible pores, unretouched skin, fine wrinkles» را در پرامپت تصویر تکرار کن و CFG را کمی بالا ببر.

**۱) فریم اول — Qwen-Image-2.1**

```text
Very tight close-up, the face filling the frame from the brow to just below the chin, slightly off centre. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns stands outdoors on the bare hillside of the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky, wind moving single strands of his hair. His eyes are wet and glassy with the light catching the film of moisture, but no tear has fallen. He looks directly into the lens for the first time in the film. Flat cold overcast light, no fill, the bare hills a soft grey wash behind. 85mm lens, extremely shallow depth of field, the eyes tack sharp. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (ref2v, 2K)**

```text
Locked-off extreme close-up, the camera holds absolutely still for eight seconds. He sings the line straight into the lens, the mouth articulating clearly and naturally, the jaw and throat moving. A single tear leaves the left eye and runs down the cheek into the beard, unwiped, while he keeps singing without breaking. He blinks slowly once. The wind keeps moving a few strands of hair across his forehead. No head turn, no hand, no other movement. Keep his face, beard, hair and clothing exactly as in the reference images. Soundscape: only hillside wind and breath. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: CEM, NOW, S, WA</sub>

---

## سکانس ۶ — کُرس دوم

### S20 · کلاس، نیمکت خالی  `02:26–02:36` · 10s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (2K)  ·  **جایگزین:** LTX-2.5 Pro
- **چرا:** چند بچه‌ی نشسته با حرکات ریز + پوش-این آرام. H3 در کنترل جمعیتِ کم‌حرکت پایدارتر است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-02، CS-07 (فقط برای استایل یونیفرم)
- **صدا:** صدای کلاس — بسیار کم، فقط برای عمق.
- **نکته:** قانون: هیچ‌کس به نیمکت خالی نگاه نمی‌کند. سکوتِ جمعی مؤثرتر از سوگِ نمایشی است.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide shot from the back of the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light looking towards the green chalkboard, the camera dead centre in the aisle. Twenty-three boys in pale blue-grey uniforms sit at the double desks, seen from behind, heads down over their books. In the middle row, second desk from the back on the window side, one seat is empty and a small bunch of white stock flowers lies on it. Hard morning side light through the tall windows, thick dust in the beams. 24mm lens, deep focus. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — MiniMax H3 (2K)**

```text
A very slow push in straight down the centre aisle over the full ten seconds, moving no more than two desks' distance, ending framed on the empty seat with the flowers. The seated children move only slightly: heads bending, a shoulder shifting, one boy scratching the back of his neck, pages turning here and there. Nobody stands up, nobody turns around, nobody looks at the empty desk. Dust drifts continuously through the window beams. The empty seat and its white flowers stay exactly in the centre of the frame as the camera advances. Preserve the desk layout, the window count and the chalkboard exactly. Soundscape: pencils on paper, a cough, a chair creak, a page turning, distant traffic. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: CLASS, NOW</sub>

---
### S21 · دفتر حضور و غیاب  `02:36–02:42` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Pro  ·  **جایگزین:** MiniMax H3
- **چرا:** ماکروی ساده با یک حرکت دست.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-02
- **صدا:** سکوتِ نگه‌داشته.
- **نکته:** اگر نام واقعی می‌خواهی روی دفتر بیفتد، در پست اضافه کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Overhead macro of an open school attendance register on a wooden teacher's desk in the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light, the ruled columns and rows of names deliberately soft and illegible. A woman's hand holding a red pen hovers above one particular row, the pen tip a centimetre off the paper, not touching. Soft window light from the left, the grain of the old desk visible at the frame edge. 100mm macro lens, shallow depth of field on the pen tip. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon.
```

**۲) ویدیو — LTX-2.5 Pro**

```text
Locked-off overhead macro, no camera movement. Over six seconds the hand holding the red pen lowers towards one row, stops a few millimetres above the paper, and holds there, trembling very slightly, for three full seconds. Then it lifts away and withdraws out of the top of frame without ever marking the page. The page is left untouched. Keep all writing soft and unreadable. Soundscape: a room going quiet, one breath held, a distant chair scraping. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: CLASS, NOW</sub>

---
### S22 · خواننده، انتهای کلاس  `02:42–02:50` · 8s
**[C] خواننده داخل صحنه — شاهدِ خاموش**

- **موتور:** Seedance 2.0  ·  **جایگزین:** MiniMax H3 (ref2v)
- **چرا:** قفل هویت + بچه‌های متحرک در یک قاب؛ و می‌شود دو شات را در یک رندر گرفت.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01 → @Image1، LS-02 → @Image2، CS-05 پنل ۲ → @Image3
- **صدا:** همان آمبیانس کلاس، ادامه از S20.
- **نکته:** او را همیشه در سایه و در عمقِ قاب بگذار؛ حضورش نباید توجیهِ منطقی بخواهد.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide shot from the front of the CLASSROOM: an Iranian primary classroom, twelve double desks of scratched wood and grey steel in three rows, a large green chalkboard with chalk ghosting, a wooden teacher's desk, a faded wall map, tall steel-framed windows with peeling white paint, chalk dust hanging in the light, from beside the chalkboard, looking back down the aisle towards the rear wall. The seated children are in the foreground with their backs to us, heads down. At the very back of the room, standing against the rear wall in the corner shadow, is the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns, hands at his sides, watching. The empty desk with the white flowers is between him and camera. Hard dusty side light from the windows, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. 35mm lens, deep focus.
```

**۲) ویدیو — Seedance 2.0**

```text
@Image1 is the man at the back of the room: keep his face, beard, hair and clothing identical to it. @Image2 is the classroom. @Image3 is the lighting reference. Shot 1, zero to five seconds: a static wide down the aisle, the children working at their desks with small idle movements, the man standing motionless against the back wall, nobody turning towards him, nobody aware of him. Shot 2, five to eight seconds: cut to a slow static medium on the man alone at the back wall as he lowers his eyes to the empty desk and lets out one long breath. The camera never moves in either shot. Hard dusty window side light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. Audio: pencils, paper, a cough, room tone. No dialogue, no music.
```

<sub>بلوک‌های استفاده‌شده: CLASS, NOW, S, WA</sub>

---

## سکانس ۷ — بریج / باران

### S23 · باران و قایق کاغذی  `02:50–03:00` · 10s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** Seedance 2.0
- **چرا:** آب جاری + شیء شناور در ۱۰ ثانیه — LTX سرعت و کیفیت آب را خوب می‌دهد و ارزان است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-01، PS-01
- **صدا:** باران کامل باز — این تنها جایی است که آمبیانس اجازه دارد بلند باشد.
- **نکته:** قایقِ کاغذی از برگِ همان دفتر ساخته شده؛ این پیوندِ بصری با S16 را در تدوین با یک کات مستقیم برجسته کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Low close shot, camera almost on the ground. Rain falls hard onto the grey hexagonal tiles of the courtyard in the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, water running in a fast sheet towards the drain channel at the edge. A small paper boat folded from a torn lined notebook page floats into frame on the current, the blue ink of the handwriting already bleeding and blurred by the water. The blue school gate is a soft shape in the deep background. Cold rainy daylight, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. 35mm lens, shallow focus on the boat.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Locked-off low shot, no camera movement. Over ten seconds the paper boat travels across the frame left to right on the running water, spinning slowly once as it passes over a crack in the tiles, rain hammering into the water all around it and throwing up small crowns of splash. The ink on the visible page bleeds further and further until it is only blue smears. Near the end the boat catches on the edge of the drain channel, tips, and begins to take on water, still afloat as the clip ends. Keep the writing illegible at all times. Soundscape: heavy rain on stone, running water, the paper hull knocking against tile. No music.
```

<sub>بلوک‌های استفاده‌شده: NOW, SCHOOL</sub>

---
### S24 · مادر روی پله‌های خیس  `03:00–03:10` · 10s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3 (2K)  ·  **جایگزین:** LTX-2.5 Pro
- **چرا:** بدن انسان در باران با پارچه‌ی خیس؛ فیزیک پارچه‌ی H3 بهترین است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-06، LS-01، PS-01
- **صدا:** باران روی پارچه — لایه‌ی نزدیک و خفه.
- **نکته:** تکان خوردنِ گهواره‌ای مهم‌ترین دیتیل بازیگری کل کلیپ است؛ در پرامپت حذفش نکن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide shot, slightly high, from across the courtyard. the MOTHER (Golbanoo, 52): an Iranian village woman; a round soft face with deep nasolabial folds, weathered olive skin, tired hazel-brown eyes with red-rimmed lower lids and puffy underlids; grey-streaked dark hair almost entirely hidden; a white cotton headscarf with a small faded blue floral print knotted under the chin; a long dark-green velvet Lori dress over black trousers and a black cardigan; strong working hands, short unpolished nails, one thin worn gold band; a slight forward stoop and a slow, careful walk sits alone on the wet concrete steps of the school building in the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, hunched forward, holding the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap tight against her chest with both arms, her head bent over it. Rain falls steadily, the whole courtyard reflecting the pewter sky. Her scarf and dress are soaked dark. Nobody else is anywhere in frame. Cold rainy light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. 35mm lens, deep focus.
```

**۲) ویدیو — MiniMax H3 (2K)**

```text
The camera holds a static wide for the full ten seconds. The woman rocks forward and back very slightly, four or five times, the way you rock a baby, her head still bent over the satchel. Rain runs off her scarf in a thin continuous stream and hammers into the flooded tiles around her, throwing up a low mist. She does not look up and does not speak. Near the end her rocking slows and stops, and she simply holds still in the rain. Keep her exactly as in the reference image, and keep the satchel's colour and shape exact. Soundscape: heavy rain on concrete and on fabric, water running off a roof edge, no voices. No music.
```

<sub>بلوک‌های استفاده‌شده: BAG, M, NOW, SCHOOL</sub>

---
### S25 · خواننده زیر باران — نمای باز  `03:10–03:18` · 8s
**[A] اجرای خواننده — لب‌خوانی / حضور مستقیم**

- **موتور:** MiniMax H3 (ref2v, 2K)  ·  **جایگزین:** Seedance 2.0
- **چرا:** تمام‌قد در باران با قفل چهره — رفرنس چندتایی H3 لازم است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-04 (پنل لباس B)، CS-05 (پنل ۵)، LS-01
- **صدا:** رعد دور — یک بار، در ثانیه‌ی آخر.
- **نکته:** تنها پلانی که خواننده تمام‌قد و در مرکز قاب است. جای اوج بریج.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide full-body shot, camera at chest height, dead centre. the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe B: the same charcoal-grey collarless shirt, soaked through and clinging, sleeves down, no overshirt, black trousers dark with rain, hair wet and flattened stands alone in the exact middle of the flooded empty courtyard of the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, arms hanging at his sides, palms slightly open, head tipped back and face up into the rain, eyes closed. Water sheets off him. The blue gate is closed behind him. A single distant sodium lamp puts a cold warm-edged glow into the rain. Night-for-dusk, cold blue, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon. 35mm lens, deep focus.
```

**۲) ویدیو — MiniMax H3 (ref2v, 2K)**

```text
Locked-off wide, the camera does not move for eight seconds. He stands with his head tipped back into the rain and does not move for the first four seconds, water running over his face and off his chin and fingertips. Then his shoulders drop, his head comes slowly down and level, and he opens his eyes and looks straight ahead past the camera. His hands stay open at his sides. He never covers his face and never wipes the water away. Rain falls steadily across the whole frame and bounces off the flooded tiles around his feet. Keep his face, beard, hair and soaked clothing exactly as in the reference images. Soundscape: heavy rain on stone and water, wind, a distant thunder roll. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: NOW, S, SCHOOL, WB</sub>

---

## سکانس ۸ — کُرس پایانی

### S26 · زنگ می‌خورد  `03:18–03:22` · 4s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** MiniMax H3  ·  **جایگزین:** LTX-2.5 Fast
- **چرا:** پلان کوتاه ۴ ثانیه‌ای — H3 حداقل ۴ ثانیه می‌دهد و صدای زنگِ هم‌زمان می‌سازد.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** PS-01، LS-01
- **صدا:** صدای زنگ را نگه دار — تنها آمبیانسی که باید در میکس واضح شنیده شود.
- **نکته:** بعد از دو پلانِ «زنگ نزنید»، حالا زنگ می‌خورد. این چرخشِ معناییِ کلیپ است.

**۱) فریم اول — Qwen-Image-2.1**

```text
Tight shot, low angle against a brightening sky. the BELL: an old brass hand bell with a worn dark wooden handle, hanging from a fraying hemp rope on a nail beside a blue-painted steel door, green patina in the grooves, the clapper visible inside hangs by its rope beside the blue steel door in the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate, and the old man's hand has just closed hard around the rope and pulled, the bell caught at the start of its swing, the clapper leaving the brass. The rain has stopped. First warm light is breaking on the wet blue-painted wall behind. 85mm lens, shallow focus on the bell. Warm, hopeful, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming towards gold.
```

**۲) ویدیو — MiniMax H3**

```text
Locked-off tight shot. Over four seconds the bell swings hard twice, the clapper striking the inside of the brass on each swing, water droplets flying off the rim and catching the new warm light. The hemp rope jerks taut and slack. The light on the wall behind warms visibly from grey to gold across the clip. Keep the bell's exact shape and patina. Soundscape: two loud clear brass bell strikes with a long ring-out, water dripping, birds starting up. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: BELL, NOW, SCHOOL</sub>

---
### S27 · حیاط پر می‌شود — صف صبحگاه  `03:22–03:34` · 12s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** Seedance 2.0 (multi-shot)  ·  **جایگزین:** MiniMax H3 (2K)
- **چرا:** جمعیت زیاد + سه شات پشت‌سرهم در یک رندر + سینک با ضربِ آهنگ. این نقطه‌ی قوتِ منحصربه‌فرد Seedance 2.0 است.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-01 → @Image1، CS-07 → @Image2 (استایل یونیفرم)
- **صدا:** همهمه‌ای که بالا می‌آید و ناگهان آرام می‌شود — پل به پلان آخر.
- **نکته:** در Seedance حتماً بنویس «camera locked off in every shot»، وگرنه خودش دوربین را حرکت می‌دهد.

**۱) فریم اول — Qwen-Image-2.1**

```text
Wide high shot looking down into the courtyard of the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate through the open blue gate. A crowd of primary-school children in pale blue-grey uniforms pours in through the gate and spreads across the wet grey hexagonal tiles, satchels swinging. Warm low sun breaks through the breaking cloud and lays a long bar of gold across the wet tiles. Steam rises from the drying stone. 24mm lens, deep focus, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming to gold.
```

**۲) ویدیو — Seedance 2.0 (multi-shot)**

```text
@Image1 is the courtyard, keep its architecture, tile pattern and tree exactly. @Image2 is the uniform style. Shot 1, zero to four seconds: a high wide from above the gate as dozens of children flood into the wet courtyard, running and fanning out across the tiles, satchels swinging, breath visible in the cold morning air. Shot 2, four to eight seconds: cut to a low shot at child height in the middle of the crowd as they rush past the camera on both sides, feet splashing through shallow water, warm sun flaring between the moving bodies. Shot 3, eight to twelve seconds: cut back to the high wide as the running resolves into four straight lines for morning assembly, the noise settling, the long bar of golden light crossing the whole courtyard and the steam rising off the drying tiles. Camera locked off in every shot, no handheld. Warm breaking-cloud light, LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming to gold. Audio: a rush of children's voices and running feet building, then settling into a hush as the lines form. No music.
```

<sub>بلوک‌های استفاده‌شده: NOW, SCHOOL</sub>

---
### S28 · آخرین ردیف — پسر برمی‌گردد  `03:34–03:44` · 10s
**[C] خواننده داخل صحنه — شاهدِ خاموش**

- **موتور:** MiniMax H3 (first & last frame)  ·  **جایگزین:** Seedance 2.0
- **چرا:** مهم‌ترین پلانِ کلیپ. با دادن فریم اول و فریم آخر، ظاهر شدنِ پسر را کاملاً کنترل می‌کنی و به شانس نمی‌سپاری.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** CS-01، CS-07، LS-01
- **صدا:** تقریباً سکوت. فقط آهنگ.
- **نکته:** هر دو فریم را با Qwen بساز، بعد در H3 با role=first_frame و role=last_frame بفرست. تفاوت دو فریم فقط باید همان یک بچه باشد — بقیه‌ی قاب مو‌به‌مو یکسان.

**۱) فریم اول — Qwen-Image-2.1**

```text
FIRST FRAME. Medium wide shot from behind, at adult shoulder height, looking along the last row of the morning assembly lines in the courtyard of the SCHOOL: a small Iranian provincial primary school, a rectangular courtyard paved in grey hexagonal cement tiles, a low whitewashed wall painted sky-blue up to waist height, one tall old plane tree with mottled peeling bark in the corner, a rusted backboard with no net, a single flagpole, a two-storey building in pale ochre plaster with steel-framed windows, and a wide blue-painted metal double gate. Twenty children stand in line with their backs to us, still and straight, in warm low golden sun, long shadows across the wet tiles. At the far end of the frame, beyond the line, the SINGER: a 38-year-old Iranian man of Lur descent, 178 cm, lean build with slightly narrow shoulders; an oval face with high flat cheekbones and a straight, slightly aquiline nose; deep-set warm dark-brown eyes with heavy upper lids and fine sun lines at the outer corners; thick dark eyebrows with a small natural gap between them; short black hair combed loosely back, a few grey strands at the temples, a receding corner at the left temple; a short, dense, neatly trimmed black beard with a patch of grey on the chin, and a moustache that just touches the upper lip; olive-tan skin with visible pores, a small flat mole on the left cheekbone two centimetres below the eye; a calm, heavy, grief-worn gaze, mouth naturally closed and slightly downturned; very still posture, low relaxed shoulders wearing wardrobe A: a plain charcoal-grey collarless mandarin shirt buttoned to the throat, sleeves rolled once above the wrist; a dark indigo unlined wool overshirt worn open; black straight trousers; scuffed brown leather shoes; a thin black prayer-bead strand wound twice around the left wrist; no watch, no rings, no logos, no patterns stands just inside the open blue gate, small, watching. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming to gold. 50mm lens, shallow focus on the line, the man soft in the background.
```

**۱ب) فریم آخر — Qwen-Image-2.1**

```text
LAST FRAME. The identical framing, identical light, identical line of children. One boy near the end of the last row, the BOY (Yasin, 9): an Iranian primary-school boy; a round face, large dark-brown eyes with long lashes, thick straight black hair with a stubborn cowlick at the crown, slightly large front teeth with a narrow gap, light olive skin, a healing scratch on the right knee; the Iranian primary-school uniform: a pale blue-grey short-sleeve shirt over a white undershirt, navy trousers, white canvas shoes; a bright, open, unguarded smile, has turned around and is looking straight into the lens with a small open smile, his hand half raised. Everyone else is unchanged and still facing forward. At the gate, the man's face has lifted, his eyes on the boy. Identical lens, identical colour, identical shadows.
```

**۲) ویدیو — MiniMax H3 (first & last frame)**

```text
Locked-off shot, the camera does not move for ten seconds. For the first six seconds the line of children stands still with their backs to camera, only small idle movements, a satchel strap shifting, hair lifting in the breeze, while the man at the gate watches. Then one single boy near the end of the last row turns around, slowly and naturally, and looks straight into the lens with a small open smile, raising one hand halfway. No other child turns or reacts. The man at the gate lifts his face towards the boy. The light stays warm and steady. The clip ends holding on the boy looking at camera. Keep both faces exactly as in the reference images. Soundscape: a schoolyard gone quiet, a single sparrow, wind, breath. No music, no dialogue.
```

<sub>بلوک‌های استفاده‌شده: NOW, S, SCHOOL, WA</sub>

---
### S29 · پایان — دو گزینه  `03:44–03:50` · 6s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Pro  ·  **جایگزین:** MiniMax H3
- **چرا:** پلان کوتاه و ساکن با تغییر نور؛ کیفیت Pro برای پلان آخر.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-01، LS-02
- **صدا:** سکوت.
- **نکته:** گزینه A پایانِ آشتی است، گزینه B پایانِ صادق. پیشنهاد من: B. تلخ‌تر اما ماندگارتر — و با متنِ ترانه صادق‌تر است.

**۱) فریم اول — Qwen-Image-2.1**

```text
OPTION A, the merciful ending. Reverse wide of the assembly lines from the front, the rows complete and unbroken, every place filled, warm golden light across all the faces. OPTION B, the honest ending. The same empty classroom as before, the desks now full of working children, but the one seat in the middle row second from the back is still empty, and the long bar of golden sun has moved across the room and now lands precisely and only on that empty seat and its white flowers. Choose one. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming to gold. 35mm lens.
```

**۲) ویدیو — LTX-2.5 Pro**

```text
Locked-off shot, no camera movement, six seconds. OPTION A: the complete lines of children stand still in the golden light, only breathing and the smallest idle movements, and one by one a few of them slowly lift their eyes. OPTION B: the classroom is quiet and working, and over the six seconds the bar of golden sunlight creeps a few centimetres further across the empty seat until it fully covers the white flowers on it, and then holds. Nothing else changes in either option. Soundscape: a schoolyard hush, or a classroom room tone with pencils. No music, no voices.
```

<sub>بلوک‌های استفاده‌شده: NOW</sub>

---

## سکانس ۹ — اوترو

### S30 · سنگ، غروب، گنجشک  `03:50–04:00` · 10s
**[B] تصویرسازی محض — بدون خواننده**

- **موتور:** LTX-2.5 Fast  ·  **جایگزین:** MiniMax H3
- **چرا:** پلان پایانی طولانی و آرام با یک اتفاق کوچک؛ LTX تا ۲۰ ثانیه می‌دهد و می‌توانی دنباله‌ی بلندتر برای تیتراژ بگیری.
- **نسبت:** 16:9  ·  **رفرنس‌ها:** LS-03 (پنل سنگ)، PS-01
- **صدا:** محو شدن همه‌چیز در باد.
- **نکته:** روی این پلان تیتراژ و تقدیم‌نامه بگذار. ۵ ثانیه‌ی آخر را در پست به سیاهی فید کن.

**۱) فریم اول — Qwen-Image-2.1**

```text
Low wide shot at ground level on the hillside of the CEMETERY: a bare hillside graveyard outside a Zagros town, flat marble slabs in uneven rows set directly into dry ochre earth, sparse thorn bushes, a crumbling low stone wall, treeless brown hills beyond, a flat pewter overcast sky at last light. the GRAVE: an Iranian Muslim grave, a flat polished grey-white marble slab laid horizontally flush with the ground, no upright headstone and no cross, a shallow carved border frame, a small dented copper water vessel at the head, a few cut stems of white stock flowers, dry ochre earth around it lies in the foreground, still faintly wet, the low orange sun raking across the polished marble and picking out the carved border. the SCHOOLBAG: a dark maroon rectangular Iranian primary-school satchel, stiff vinyl with a single brass buckle and one flat front pocket, brand-new, unscuffed, with a small hand-sewn white cotton name tag stitched inside the flap stands beside it. The bare hills beyond are deep blue in shadow, the sky above them warm amber. No people. 35mm lens, deep focus, level horizon. LOOK-NOW: cinematic 35mm anamorphic photography, ARRI Alexa colour science, a desaturated cool palette of slate blue-grey, chalk white and dusty ochre, soft overcast toplight, fine natural film grain, gentle halation on highlights, shallow depth of field, natural unretouched skin tones, no lens flare, level horizon warming to a deep golden dusk.
```

**۲) ویدیو — LTX-2.5 Fast**

```text
Locked-off low wide, the camera does not move for ten seconds. The last orange light creeps slowly across the marble slab and fades as the sun drops, the stone cooling from gold to blue over the clip. Wind moves the dry grass at the frame edge. At around the sixth second a single sparrow drops into frame and lands on the edge of the slab, hops twice, turns its head once towards camera, then flies out of the top of frame, and the frame holds empty on the stone as the light dies. No people at any point. The grave must stay a flat slab lying on the ground. Soundscape: evening hillside wind, one small bird call and a flutter of wings, then nothing. No music.
```

<sub>بلوک‌های استفاده‌شده: BAG, CEM, NOW, STONE</sub>

---

## نگتیو پرامپت مشترک (همه‌ی تصاویر Qwen)

```text
text, letters, words, watermark, logo, signature, caption, subtitles, ui, extra fingers, six fingers, deformed hands, fused fingers, extra limbs, distorted face, asymmetrical eyes, plastic skin, waxy skin, beauty retouching, oversharpened, hdr glow, oversaturated, neon, cartoon, anime, 3d render, cgi, video game, illustration, painting, sketch, blurry, low resolution, jpeg artifacts, duplicate people, cloned faces, upright headstones, western cemetery, crosses, church, pews, coffins, blood, injury, corpse, western school uniforms, blazers, ties, jeans with logos, modern sneakers, smartphones, lens flare, tilted horizon, fisheye, vignette overload
```
