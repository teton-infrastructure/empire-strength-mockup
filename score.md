# Website Score: Empire Strength and Fitness (empirestrengthandfitness.com)

Audited: Nov 19, 2026 (MST). Pages fetched with curl (home, /join, /join/paid-in-full, /passes, /training, /training/garet-butikofer, /events, /lift-where-you-stand, /thunderdome, /7-day-trial, /boxingwithparkinsons, sitemap) and screenshotted with headless Chrome (Playwright) at 1280px desktop and a 390px iPhone.

**Platform:** Wix (`<meta name="generator" content="Wix.com Website Builder">`). Member signups run through GymMaster (`empiresandf.gymmasteronline.com`) and the "Empire Idaho Falls" app (iOS + Google Play).

## Overall: **61 / 100**: great gym, strong copy and honest pricing, held back by a heavy Wix build, inconsistent offers and broken structured data

| Category | Score | Notes |
|---|---|---|
| Mobile & tap-to-call | 9 / 15 | Wix serves a separate mobile build locked to `<meta name="viewport" content="width=320">`, so everything is scaled on modern phones. `format-detection: telephone=no` is set. A cookie banner covers most of the first mobile screen. `tel:` links exist (footer, /join) but there's no sticky call/join bar. |
| Clear headline & offer | 10 / 15 | "IDAHO FALLS' 24/7 STRENGTH GYM" is a good H1. But the home page opens with passes before memberships, and the trial offer is told three ways: "3 Day Trial", "One Week to Try 3 days free", and an unlinked /7-day-trial page ("FREE FOR 7 DAYS", with "campaign office hours" Mon–Fri 10 am–8 pm vs. 10–5:30 everywhere else). The home page calls Family "Family of 5 people"; /join says "Two people in your household" plus kids. |
| Trust (reviews, awards, people) | 11 / 15 | Real strengths: Idaho's Best 2026 Gym and 2024/2025 Personal Training badges, 10 named trainers with specialties, owner bio. But the **4.9★ / 160+ Google reviews** line only appears on /join and /paid-in-full, not the home page, and no review text is shown anywhere. |
| Speed / tech | 4 / 10 | Edge is fast (TTFB ≈ 0.04 s), but the home page HTML alone is **1.45 MB desktop / 1.54 MB mobile** with **64 `<script>` tags** before images and video. In headless captures, the desktop pass cards and two other blocks rendered as empty white boxes until animations fire. |
| SEO / local basics | 7 / 15 | Good title ("Best Gym in Idaho Falls, ID"), meta description, og:image, canonical. Problems: the LocalBusiness JSON-LD has the **wrong phone (`2082240037` instead of 208-244-0037)** and "1539 Piper Street" vs. "1539 E Piper St" on the page; no hours, geo, `ExerciseGym` type, prices or rating in schema. **Six `<h1>` tags** on the home page (incl. "Our instagram is dope"). 9 images with empty alt. |
| Readable by Google AI / ChatGPT | 5 / 10 | Text is server-rendered, which helps, and /join has a good FAQ, but there's no FAQ schema and the home page doesn't state prices, hours and programs in one place an AI answer can quote. |
| Design | 7 / 10 | Strong brand (red/black, Empire logo) and good real facility photos. But fonts and styles shift section to section, the hero is crowded (badges + two buttons + a disciplines line), large white blocks break the dark theme, and the D&D campaign sits mid-home-page between training and amenities, which dilutes the "serious strength gym" message. |
| Calls to action | 8 / 10 | "JOIN · $60/MO" and "TRY A DAY · $20" in the footer are excellent. They just need to be the first thing you see, on every screen. |
| **Total** | **61 / 100** | |

### Top problems (with evidence)
1. **Schema has the wrong phone number.** `"telephone":"2082240037"` in the LocalBusiness JSON-LD; the real number is (208) 244-0037. Google and AI tools read this.
2. **Heavy, dated Wix build.** 1.45 MB of HTML, 64 scripts, fixed 320px mobile layout, cookie banner over the hero on phones.
3. **Mixed offers.** Three versions of the free trial, two different office-hour windows, two descriptions of the Family plan.
4. **Best proof is buried.** 4.9★ from 160+ Google reviews isn't on the home page.
5. **Stale / sloppy details.** The home page "Upcoming events" and /events still feature The Sinister Games (Oct 17, 2026, already past). The LWYS page calls the nonprofit a "503c" (should probably be 501(c)(3)). Six H1s.

### What's good (honestly)
- Clear, transparent pricing with no contract, no sign-up fee, easy cancel, and a math-backed paid-in-full page.
- A real point of view: "Owned and operated by actual weight lifters", "We are not a CrossFit® gym", "Go forth and conquer."
- Real coach roster, real photos of the floor, real community programs (LWYS, Boxing with Parkinson's, Thunderdome).

## Business facts (from empirestrengthandfitness.com unless noted)
- **Name:** Empire Strength and Fitness (© Empire Strength and Fitness LLC)
- **Address:** 1539 E Piper St, Idaho Falls, ID 83401
- **Phone (call or text):** 208-244-0037 · **Email:** lift@empirestrengthandfitness.com
- **Hours:** gym 24/7 for members (app entry); office Mon–Fri 10 am–5:30 pm
- **Size:** 16,000 sq ft (/join)
- **Disciplines:** strongman, powerlifting, Olympic lifting, bodybuilding (posing room), functional training, official HYROX Training Club
- **Amenities:** saunas, cold tubs/ice baths, free kids area (The Thunderdome), on-site chiropractor (Chiro Shack), turf, outdoor area, "more free weights than any gym in the area", dog friendly
- **Pricing:** Single $60/mo; Family from $100/mo; Student $40; Solo Hero $35; Family Hero $70; Day pass $20; Week pass $40; 3-day free trial (locals, start in office); Paid in full Single $630/yr, Family $1,000/yr, Solo Hero $350/yr, Family Hero $700/yr; HYROX $80/mo (8 classes, Mon/Tue/Thu 6–7 am & 5:30–6:30 pm), $20 drop-in; D&D "Empire Mercenary Company" add-on $60/mo
- **Awards:** Idaho's Best 2026 Gold Winner – Best Gym; Idaho's Best (Eastern Idaho) Personal Training 2024 & 2025
- **People:** Garet Butikofer (co-owner, head trainer) plus trainers Ryan Coronado, Coleman & Ashley Moore, Sheena Daniels, Kendra Jensen, Crystal Hill, Preston Buckley, Morgan Quigg, Scott Larson, Grace Jack
- **Partners:** Bishop Barbell and Fitness Supply; Lift Where You Stand Inc. (nonprofit)
- **Social:** facebook.com/theempireofstrength, instagram.com/empirestrengthandfitness, youtube.com/@EmpireStrengthandFitness
- **Google rating:** 4.9★. The site says "160+ reviews"; Google-derived directories show 159 (exa.ai), 162 (Coldlytics, Oct 2026), 168 (D7). Google Maps itself couldn't be opened from the box.

### Mockup update (Nov 19, 2026): built from what's on the live site
- Added all 10 coach cards with real photos from /training (object-fit cover, top-aligned), titles, specialties and short bios from each trainer page; Grace Jack marked "Fully booked" as on her page.
- Added Chiro Shack (logo + Aperta Health booking link), posing room, Thunderdome details and the Thunderdome Guardians program.
- New Community section: Lift Where You Stand, Boxing with Parkinson's (Saturdays 1:30 pm, Keith Director), free community yoga with Sheena (from their Instagram feed on the home page), The Sinister Games, Battle for the Throne, and the D&D Empire Mercenary Company add-on (tucked into Community, not in the hero).
- Federation/partner logos as linked on their home page (Strongman Corporation, USA Weightlifting, USPA, APF to worldpowerliftingcongress.com) plus Bishop Barbell & Fitness Supply (text only; no logo on their site).
- Empire Idaho Falls app links (App Store, Google Play), Google review link, paid-in-full and hero yearly rates, family-plan example.
- Offers use the primary home/membership versions: 3-day free trial, office Mon–Fri 10 am–5:30 pm. The unlinked /7-day-trial campaign page was not used.
- Still no Google review quotes (none on their site). Garet's only site photo is the whiteboard shot; used as-is.
