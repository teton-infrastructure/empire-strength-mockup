import re, json, os, html as H
ROOT='/workspace/prospects/empire-strength'
src=open(f'{ROOT}/src-onepage.html').read()
SITE=f'{ROOT}/site'
L=src.split('\n')
def sec(cls):
    i=next(k for k,l in enumerate(L) if l.startswith(f'<section class="{cls}"'))
    j=next(k for k in range(i,len(L)) if L[k].startswith('</section>'))
    return '\n'.join(L[i:j+1])
S={c:sec(c) for c in ['hero','proof','inside','compare','manifesto','disciplines','coaching','start','memberships','hyrox','recovery','community','faq','visit']}
ld=re.findall(r'<script type="application/ld\+json">(.*?)</script>',src,re.S)
gym_ld=ld[0].strip()
faqs=re.findall(r'<details[^>]*><summary>(.*?)</summary><p>(.*?)</p></details>',S['faq'])
faq_by={q:a for q,a in faqs}

NAV=[('/','Home'),('/training/','Training'),('/coaches/','Coaches'),('/memberships/','Memberships'),('/amenities/','Amenities'),('/community/','Community'),('/contact/','Contact')]
LINKMAP={'#inside':'/training/#inside','#compare':'/memberships/#compare','#coaching':'/coaches/','#memberships':'/memberships/','#community':'/community/','#visit':'/contact/','#hyrox':'/training/#hyrox','#start':'/#start','#recovery':'/amenities/','#disciplines':'/training/#disciplines','#proof':'/#proof','#top':'#top'}

def fix(s, page):
    s=s.replace('src="img/','src="/img/').replace('srcset="img/','srcset="/img/').replace(', img/',', /img/').replace('href="img/','href="/img/')
    def r(m):
        a=m.group(1)
        t=LINKMAP.get(a,a)
        # same-page anchors stay local
        if t.startswith(page+'#') : t=t[len(page):]
        return f'href="{t}"'
    return re.sub(r'href="(#[a-z-]+)"',r,s)

def faq_html(qs, open_first=True):
    items=[]
    for k,q in enumerate(qs):
        items.append(f'      <details{" open" if (k==0 and open_first) else ""}><summary>{q}</summary><p>{faq_by[q]}</p></details>')
    return '\n'.join(items)
def faq_ld(qs):
    def plain(x): return H.unescape(re.sub('<[^>]+>','',x))
    d={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":plain(q),"acceptedAnswer":{"@type":"Answer","text":plain(faq_by[q])}} for q in qs]}
    return json.dumps(d,ensure_ascii=False,indent=1)

def page_hero(eyebrow,h1,lede,img,alt):
    return f'''<section class="page-hero">
  <picture class="ph-bg"><img src="/img/{img}-1600.webp" srcset="/img/{img}-800.webp 800w, /img/{img}-1600.webp 1600w" sizes="100vw" alt="{alt}" width="1600" height="900" fetchpriority="high"></picture>
  <div class="wrap ph-inner">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="ph-lede">{lede}</p>
  </div>
</section>'''

CTA='''<section class="cta-band">
  <div class="wrap cta-row">
    <div>
      <p class="cta-kicker">Idaho Falls locals new to Empire</p>
      <h2 class="display">Your first 3 days<br>are on us.</h2>
      <p>Start your free trial in the office, Mon–Fri 10 am–5:30 pm, or join online today. $60 a month, no contract, $0 sign-up.</p>
    </div>
    <div class="cta-btns">
      <a class="btn btn-dark btn-lg" href="/memberships/#trial">Start your free trial</a>
      <a class="btn btn-outline-w btn-lg" href="https://www.empirestrengthandfitness.com/join">Join · $60/mo</a>
      <a class="cta-phone" href="sms:+12082440037">Or text 208-244-0037</a>
    </div>
  </div>
</section>'''

def layout(path,title,desc,body,extra_ld=(),preload=None):
    nav='\n'.join(f'      <a href="{u}"{" aria-current=\"page\"" if u==path else ""}>{t}</a>' for u,t in NAV)
    lds=''.join(f'<script type="application/ld+json">\n{x}\n</script>\n' for x in extra_ld)
    pre=f'<link rel="preload" as="image" href="/img/{preload}-1600.webp" imagesrcset="/img/{preload}-800.webp 800w, /img/{preload}-1600.webp 1600w" imagesizes="100vw">\n' if preload else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/img/og.jpg">
<meta name="theme-color" content="#0b0b0c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{pre}<link rel="stylesheet" href="/styles.css">
{lds}</head>
<body>

<div class="preview-banner" role="note">Concept preview prepared for <strong>Empire Strength &amp; Fitness</strong> · not the live site</div>

<header class="site-header" id="top">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="Empire Strength and Fitness home">
      <img src="/img/logo.webp" width="88" height="53" alt="Empire Strength and Fitness logo">
    </a>
    <nav class="nav" id="nav" aria-label="Main">
{nav}
    </nav>
    <div class="header-cta">
      <a class="btn btn-ghost btn-sm hide-md" href="tel:+12082440037">208-244-0037</a>
      <a class="btn btn-red btn-sm" href="/memberships/#trial">Free trial</a>
      <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
    </div>
  </div>
</header>

<main>
{body}
</main>

<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div><img src="/img/logo.webp" width="88" height="53" alt="Empire Strength and Fitness" loading="lazy"><p>Idaho Falls' 24/7 strength gym. Open to all.</p></div>
      <div><p class="ft-h">Visit</p><p><a href="https://www.google.com/maps/dir/?api=1&amp;destination=Empire+Strength+and+Fitness%2C+1539+E+Piper+St%2C+Idaho+Falls%2C+ID+83401" rel="noopener">1539 E Piper St<br>Idaho Falls, ID 83401</a></p><p>Gym 24/7 for members<br>Office Mon–Fri 10–5:30</p></div>
      <div><p class="ft-h">Contact</p><p><a href="tel:+12082440037">Call or text 208-244-0037</a><br><a href="mailto:lift@empirestrengthandfitness.com">lift@empirestrengthandfitness.com</a></p></div>
      <div><p class="ft-h">Explore</p><p class="ft-links">{" ".join(f'<a href="{u}">{t}</a>' for u,t in NAV[1:])}</p></div>
    </div>
    <div class="footer-row">
      <p>© 2026 Empire Strength and Fitness LLC</p>
      <nav aria-label="Social"><a href="https://www.instagram.com/empirestrengthandfitness" rel="noopener">Instagram</a><a href="https://www.facebook.com/theempireofstrength" rel="noopener">Facebook</a><a href="https://www.youtube.com/@EmpireStrengthandFitness" rel="noopener">YouTube</a><a href="https://g.page/r/Cc7J6oxTKd-LEBM/review" rel="noopener">Leave a Google review</a></nav>
      <p class="muted">Concept by Teton Infrastructure. Photos from empirestrengthandfitness.com.</p>
    </div>
  </div>
</footer>

<nav class="mobile-bar" aria-label="Quick actions">
  <a href="tel:+12082440037">Call</a>
  <a href="sms:+12082440037">Text</a>
  <a class="mb-join" href="https://www.empirestrengthandfitness.com/join">Join $60/mo</a>
</nav>

<script src="/app.js" defer></script>
</body>
</html>
'''

def write(path,content):
    d=SITE+path
    os.makedirs(d,exist_ok=True)
    open(d+'index.html','w').write(fix(content,path))

# ---------- HOME ----------
hero=S['hero'].replace('href="#inside">See the gym ↓','href="/training/">See the gym →')
inside_teaser=f'''<section class="inside" id="inside">
  <div class="wrap inside-head">
    <div><p class="eyebrow">Look inside</p><h2 class="display">What's inside<br>16,000 sq ft.</h2></div>
    <div><p class="inside-sum">Power racks and platforms, strongman gear and specialty bars, more free weights than any gym in the area, turf and sleds, a posing room, saunas and cold tubs.</p>
    <a class="btn btn-ghost" href="/training/#inside">See the full facility</a></div>
  </div>
  <div class="teaser-gal">
    <figure><img src="img/racks-800.webp" alt="A long row of racks with platforms" loading="lazy" width="800" height="450"><figcaption>The rack row</figcaption></figure>
    <figure><img src="img/machines-800.webp" alt="Red plate-loaded strength machines" loading="lazy" width="800" height="450"><figcaption>Plate-loaded machines</figcaption></figure>
    <figure><img src="img/turf-800.webp" alt="Turf lane with sleds and boxes under an American flag" loading="lazy" width="800" height="450"><figcaption>Turf &amp; sleds</figcaption></figure>
    <figure><img src="img/coldtub-800.webp" alt="Cold tub in the recovery area" loading="lazy" width="800" height="533"><figcaption>Cold tubs</figcaption></figure>
  </div>
</section>'''
# condensed compare: keep head + contract, fees, strength gear, recovery, price rows
cmp=S['compare']
rows=re.findall(r'      <div class="cmp-row[^"]*" role="row">.*?</div>\n',cmp)
keep=[r for r in rows if any(k in r for k in ['cmp-head','>Contract<','>Fees<','>Strength gear<','>Recovery<','cmp-price'])]
cmp_short=re.sub(r'(<div class="cmp" [^>]*>\n)(.*?)(    </div>\n    <div class="cmp-cta">)',lambda m:m.group(1)+''.join(keep)+m.group(3),cmp,flags=re.S)
cmp_short=cmp_short.replace('<a class="btn btn-ghost" href="#memberships">See all plans</a>','<a class="btn btn-ghost" href="/memberships/#compare">See the full comparison</a>').replace('<a class="btn btn-red" href="#start">Start your free trial</a>','<a class="btn btn-red" href="/memberships/">See memberships</a>')
cards=[('/training/','Training','Six ways to get strong, the full facility and HYROX.','platforms'),
       ('/coaches/','Coaches','Ten coaching teams, from first lift to competition stage.','racks'),
       ('/memberships/','Memberships','$60/mo, family plans, hero rates and paid-in-full savings.','hero'),
       ('/amenities/','Amenities','Saunas, cold tubs, posing room, Chiro Shack and the Thunderdome.','coldtub'),
       ('/community/','Community','Lift Where You Stand, Boxing with Parkinson\'s, meets and events.','turf'),
       ('/contact/','Visit','1539 E Piper St. Gym 24/7, office Mon–Fri 10–5:30.','conditioning')]
explore='''<section class="explore">
  <div class="wrap">
    <p class="eyebrow">Explore Empire</p>
    <h2 class="display">Find your fit.</h2>
    <div class="explore-grid">
'''+'\n'.join(f'''      <a class="ex-card" href="{u}"><img src="img/{im}-800.webp" alt="" loading="lazy" width="800" height="450"><span class="ex-body"><b>{t}</b><span>{d}</span><i aria-hidden="true">→</i></span></a>''' for u,t,d,im in cards)+'''
    </div>
  </div>
</section>'''
home_body='\n\n'.join([hero,S['proof'],inside_teaser,cmp_short,S['start'],explore,CTA])
write('/', layout('/',"Empire Strength &amp; Fitness | Idaho Falls' 24/7 Strength Gym",
  "Idaho Falls' 24/7 strength gym, open to every level. 16,000 sq ft of racks, platforms and strongman gear. $60/month, no contract, no sign-up fee. Idaho's Best Gym 2026.",
  home_body, extra_ld=[gym_ld], preload='hero'))

# ---------- discipline ids + coach cross-links ----------
DISC_IDS={'Powerlifting':'powerlifting','Strongman':'strongman','Olympic lifting':'olympic-lifting','Bodybuilding':'bodybuilding','Functional training':'functional-training','HYROX':'hyrox-club'}
for name,i in DISC_IDS.items():
    S['disciplines']=S['disciplines'].replace(f'<article class="disc"><span class="num">',f'<article class="disc" id="{i}"><span class="num">',1) if False else S['disciplines']
def add_disc_ids(t):
    def r(m):
        name=m.group(2)
        return f'<article class="disc" id="{DISC_IDS[name]}">{m.group(1)}<h3>{name}</h3>'
    return re.sub(r'<article class="disc">(<span class="num">\d+</span>)<h3>(.*?)</h3>',r,t)
S['disciplines']=add_disc_ids(S['disciplines'])
SPEC_LINK={'strongman':'strongman','bodybuilding':'bodybuilding','posing':'bodybuilding','olympic lifting':'olympic-lifting','powerlifting':'powerlifting','hyrox':'hyrox','hiit':'functional-training','strength &amp; athletics':'functional-training','kettlebells':'functional-training'}
def link_spec(m):
    parts=m.group(1).split(' · ')
    out=[]
    for pt in parts:
        k=pt.strip().lower()
        out.append(f'<a href="/training/#{SPEC_LINK[k]}">{pt}</a>' if k in SPEC_LINK else pt)
    return '<p class="coach-spec">'+' · '.join(out)+'</p>'
def coach_cards(t):
    # unwrap whole-card link so specialty links are valid; keep photo/name linked to live bio
    def card(m):
        href=m.group(1); inner=m.group(2)
        inner=re.sub(r'(<div class="coach-img">.*?</div>)',lambda x:f'<a class="coach-photo" href="{href}" rel="noopener">{x.group(1)}</a>',inner,count=1,flags=re.S)
        inner=re.sub(r'<h3>(.*?)</h3>',lambda x:f'<h3><a href="{href}" rel="noopener">{x.group(1)}</a></h3>',inner,count=1)
        inner=re.sub(r'<p class="coach-spec">(.*?)</p>',link_spec,inner)
        return f'<li class="coach">\n        <div class="coach-in">{inner}<a class="coach-more" href="{href}" rel="noopener">Full bio →</a></div>\n      </li>'
    return re.sub(r'<li class="coach">\s*<a href="([^"]+)" rel="noopener">(.*?)</a>\s*</li>',card,t,flags=re.S)
S['coaching']=coach_cards(S['coaching'])
# ---------- TRAINING ----------
STRIP=[('garet','Garet Butikofer','Strongman','strongman'),('scott','Scott Larson','Powerlifting','powerlifting'),('grace','Grace Jack','Olympic lifting','olympic-lifting'),('ryan','Ryan Coronado','Bodybuilding','bodybuilding'),('kendra','Kendra Jensen','HIIT &amp; HYROX','hyrox')]
COACH_STRIP='''<section class="coach-strip">
  <div class="wrap">
    <div class="section-head">
      <div><p class="eyebrow">Coached by lifters</p><h2 class="display">Meet the coaches.</h2></div>
      <a class="btn btn-red" href="/coaches/">See all 10 coaching teams</a>
    </div>
    <ul class="strip-grid">
'''+'\n'.join(f'''      <li><a href="/coaches/"><img src="/img/coach-{k}.webp" alt="{n}" width="480" height="480" loading="lazy"><b>{n}</b><span>{sp}</span></a></li>''' for k,n,sp,_ in STRIP)+'''
    </ul>
  </div>
</section>'''

inside_full=S['inside'].replace('<p class="eyebrow">Look inside</p>','<p class="eyebrow">The facility</p>')
tr_body='\n\n'.join([page_hero('Training · Idaho Falls','Train for <span class="red">strength.</span>',"Powerlifting, strongman, Olympic lifting, bodybuilding, functional training and HYROX, all under one roof in 16,000 square feet.",'platforms','Power racks and lifting platforms'),
   S['manifesto'],S['disciplines'],COACH_STRIP,inside_full,S['hyrox'],CTA])
write('/training/', layout('/training/',"Training: Powerlifting, Strongman, Olympic Lifting &amp; HYROX | Empire Strength &amp; Fitness",
  "Powerlifting, strongman, Olympic lifting, bodybuilding, functional training and an official HYROX Training Club in 16,000 sq ft in Idaho Falls. See the facility.",tr_body,preload='platforms'))

# ---------- COACHES ----------
coach=S['coaching'].replace('<h2 class="display">Your goals. Your coach.<br>Your next level.</h2>','<h2 class="display">Your goals. Your coach.<br>Your next level.</h2>')
PROG='''<section class="prog-band">
  <div class="wrap prog-row">
    <div><p class="eyebrow">Programs</p><h2 class="display">See what you'll train.</h2><p>Powerlifting, strongman, Olympic lifting, bodybuilding, functional training and HYROX, plus a look around the 16,000 sq ft floor.</p></div>
    <a class="btn btn-ghost btn-lg" href="/training/">Explore training programs</a>
  </div>
</section>'''
co_body='\n\n'.join([page_hero('Coaches · Idaho Falls','Meet your <span class="red">coach.</span>',"Idaho's Best Personal Training winner in 2024 and 2025. First-time lifter or competitor, find your fit.",'racks','A long row of racks with platforms'),coach,PROG,CTA])
write('/coaches/', layout('/coaches/',"Personal Trainers &amp; Coaches in Idaho Falls | Empire Strength &amp; Fitness",
  "Meet Empire's coaches: IFBB Pro Ryan Coronado, USAW Level 2 coach Grace Jack, head trainer Garet Butikofer and more. Idaho's Best Personal Training 2024 and 2025.",co_body,preload='racks'))

# ---------- MEMBERSHIPS ----------
mem=S['memberships'].replace('<div><b>3 days free</b>','<div id="trial"><b>3 days free</b>').replace('href="#hyrox">Details','href="/training/#hyrox">Details')
mem_faqs=['Is there a contract?','Why do discounts have to be set up in person?','Can I try it first?','What happens after a paid-in-full year?']
faq_m=f'''<section class="faq">
  <div class="wrap faq-grid">
    <div><p class="eyebrow">Before you join</p><h2 class="display">Membership<br>questions.</h2></div>
    <div class="faq-list">
{faq_html(mem_faqs)}
    </div>
  </div>
</section>'''
cmp_full=S['compare'].replace('<a class="btn btn-ghost" href="#memberships">See all plans</a>','<a class="btn btn-ghost" href="https://www.empirestrengthandfitness.com/join">Join · $60/mo</a>').replace('<a class="btn btn-red" href="#start">Start your free trial</a>','<a class="btn btn-red" href="#trial">Start your free trial</a>')
me_body='\n\n'.join([page_hero('Memberships · No contract','Pick your <span class="red">plan.</span>',"24/7 access to every rack, platform, sauna and cold tub. No contract, no sign-up fee, easy to cancel.",'hero','Rows of squat racks on the Empire training floor'),
   mem,cmp_full,faq_m,CTA])
write('/memberships/', layout('/memberships/',"Gym Membership Prices in Idaho Falls | $60/mo, No Contract | Empire",
  "Empire memberships: Single $60/mo, Family from $100/mo, Student $40, Hero from $35. Paid in full from $630/yr. 3-day free trial, $20 day pass, $40 week pass. No contract.",me_body,extra_ld=[faq_ld(mem_faqs)],preload='hero'))

# ---------- AMENITIES ----------
am_body='\n\n'.join([page_hero('Amenities','Recover. <span class="red">Bring the family.</span>',"Saunas and cold tubs in every membership, a posing room, an on-site chiropractor and a free kids area.",'coldtub','Cold tub in the recovery area'),S['recovery'].replace('<h2 class="display">Recover. Bring the family.</h2>','<h2 class="display">More than<br>the iron.</h2>'),CTA])
write('/amenities/', layout('/amenities/',"Saunas, Cold Tubs, Kids Area &amp; Chiropractor | Empire Strength &amp; Fitness",
  "Every Empire membership includes saunas, cold tubs and the posing room. Plus Chiro Shack on site and the Thunderdome, a free kids area for members.",am_body,preload='coldtub'))

# ---------- COMMUNITY ----------
cm_body='\n\n'.join([page_hero('Community','Grow the Empire. <span class="red">Lift the Empire.</span>',"Free community programs, annual meets and a crew that shows up for each other.",'turf','Turf lane with sleds and boxes under an American flag'),S['community'],CTA])
write('/community/', layout('/community/',"Community, Events &amp; Programs | Empire Strength &amp; Fitness Idaho Falls",
  "Lift Where You Stand, free Boxing with Parkinson's, community yoga, The Sinister Games strongman show, Battle for the Throne and more at Empire in Idaho Falls.",cm_body,preload='turf'))

# ---------- CONTACT ----------
gen_faqs=['When is someone at the gym?','Can I bring my kids?','Do I need lifting experience to join?']
faq_g=f'''<section class="faq">
  <div class="wrap faq-grid">
    <div><p class="eyebrow">Good to know</p><h2 class="display">Questions.</h2></div>
    <div class="faq-list">
{faq_html(gen_faqs)}
    </div>
  </div>
</section>'''
visit=S['visit'].replace('<p class="eyebrow">Visit</p>\n      <h2 class="display">Go forth<br>and conquer.</h2>','<p class="eyebrow">Find us</p>\n      <h2 class="display">Go forth<br>and conquer.</h2>\n      <p class="visit-sub">Members train 24/7 with the Empire app. Stop by the office Monday to Friday, 10 am to 5:30 pm, for a look around, to start a free trial or to set up a student or hero rate.</p>')
visit=visit.replace('<div class="hero-ctas">','<div class="hero-ctas">\n        <a class="btn btn-ghost" href="https://www.google.com/maps/dir/?api=1&amp;destination=Empire+Strength+and+Fitness%2C+1539+E+Piper+St%2C+Idaho+Falls%2C+ID+83401" target="_blank" rel="noopener">Get directions</a>',1)
ct_body='\n\n'.join([page_hero('Visit · Idaho Falls','Come see <span class="red">the Empire.</span>',"1539 E Piper St, Idaho Falls. Open 24/7 for members. Call or text 208-244-0037.",'conditioning','Conditioning bikes and rowers by the garage door'),visit,faq_g,CTA])
write('/contact/', layout('/contact/',"Visit Empire Strength &amp; Fitness | 1539 E Piper St, Idaho Falls | 208-244-0037",
  "Empire Strength & Fitness, 1539 E Piper St, Idaho Falls, ID 83401. Gym open 24/7 for members; office Mon–Fri 10 am–5:30 pm. Call or text 208-244-0037.".replace('&','&amp;'),ct_body,extra_ld=[gym_ld,faq_ld(gen_faqs)],preload='conditioning'))

open(SITE+'/app.js','w').write('''const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
if(b&&n){b.addEventListener('click',()=>{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Close menu':'Open menu')});
n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('open');b.setAttribute('aria-expanded',false)}));}
const sec=document.getElementById('memberships');
if(sec){sec.querySelectorAll('.tg').forEach(t=>t.addEventListener('click',()=>{sec.dataset.bill=t.dataset.bill;sec.querySelectorAll('.tg').forEach(x=>{const on=x===t;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on)})}));}
''')
print('built')
