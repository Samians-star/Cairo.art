#!/usr/bin/env python3
"""
Build script for the Cairo School of Art & Calligraphy public website.
Regenerate all HTML pages after editing COURSES / page copy below:
    python3 scripts/build.py
"""
import os, json, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_NAME = "Cairo School of Art & Calligraphy"
TAGLINE = "Rule the world with the power of your personality"
PHONE_DISPLAY = "0301 1151116"
PHONE_TEL = "+923011151116"
WA_DISPLAY = "0339 3338224"
WA_INTL = "923393338224"
INSTAGRAM = "https://www.instagram.com/cairo.artstudio/"
SITE_URL = "https://YOUR-USERNAME.github.io/cairo-school-website"  # update after deploying

DURATIONS = ["2 Weeks", "4 Weeks", "6 Weeks", "8 Weeks", "3 Months", "6 Months"]

FAVICON_SVG = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
               "<rect width='100' height='100' fill='#15120F'/>"
               "<text x='50' y='71' font-size='58' font-family='Georgia,serif' "
               "font-style='italic' fill='#B08D46' text-anchor='middle'>C</text></svg>")
FAVICON_HREF = "data:image/svg+xml," + urllib.parse.quote(FAVICON_SVG)

STROKE_SVG = """<svg class="hero__stroke" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path d="M8,42 C55,8 95,58 145,28 C180,6 215,50 255,26 C285,8 320,40 345,20 C352,15 358,22 350,26"/>
</svg>"""

ORNAMENT_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">'
                '<rect x="4" y="4" width="16" height="16"/>'
                '<rect x="4" y="4" width="16" height="16" transform="rotate(45 12 12)"/></svg>')

# --------------------------------------------------------------------------
# COURSE DATA — single source of truth. Edit here, then re-run this script.
# --------------------------------------------------------------------------

def suggest_pricing(fee8):
    """8-week fee is the only confirmed price. Everything else is a clearly
    labelled suggestion an admin should confirm — never assumed proportional."""
    if fee8 is None:
        return {d: None for d in DURATIONS}
    pw = fee8 / 8
    raw = {
        "2 Weeks": pw * 2 * 1.1,
        "4 Weeks": pw * 4,
        "6 Weeks": pw * 6,
        "8 Weeks": fee8,
        "3 Months": pw * 11,
        "6 Months": pw * 20,
    }
    out = {}
    for d, v in raw.items():
        out[d] = fee8 if d == "8 Weeks" else int(round(v / 500) * 500)
    return out

COURSES = [
    dict(slug="calligraphy", name="Calligraphy", fee8=29000,
         description="Foundational and advanced calligraphy training across scripts, from pen control to full decorative compositions.",
         who_for="Complete beginners through to students refining a personal hand for professional or exhibition work.",
         requirements="No prior experience needed. Bring your own dedication — tools list is provided at enrolment.",
         outcomes=["Confident control of pen, ink and pressure", "Correct letterform structure and proportion",
                    "Fluent word and line composition", "A finished, presentation-ready calligraphy piece"],
         materials=["Calligraphy pens / nibs", "Ink", "Practice sheets", "Sketchbook"],
         curriculum=["Tools, materials, posture and foundational strokes", "Letter structure and proportion",
                      "Connecting letters and word construction", "Script development and composition",
                      "Advanced forms and spacing", "Composition and layout", "Decorative technique and artwork development",
                      "Final calligraphy project and presentation"],
         faq=[("Which scripts are covered?", "Your teacher tailors script focus (English, Urdu or Arabic hands) to your goals during enrolment."),
               ("Do I need my own tools?", "A starter tool list is shared after enrolment — nothing to buy before your first class.")]),

    dict(slug="handwriting", name="Handwriting", fee8=5000,
         description="A focused, practical programme to make everyday handwriting clearer, faster and more consistent.",
         who_for="Students and professionals who want neater, more legible handwriting for daily use.",
         requirements="No prior experience needed.",
         outcomes=["Consistent letter size and spacing", "Improved speed without losing legibility", "Reduced fatigue and better pen grip"],
         materials=["Pen or pencil", "Ruled notebook"],
         curriculum=["Posture, grip and paper positioning", "Letter formation fundamentals", "Consistent sizing and spacing",
                      "Joining letters and cursive basics", "Speed and fluency drills", "Correcting common errors",
                      "Personal style development", "Final handwriting sample and assessment"],
         faq=[("Is this for children or adults?", "Both — classes are grouped by age and current handwriting level."),
               ("How is this different from Calligraphy?", "Handwriting focuses on everyday legibility and speed; Calligraphy is an artistic script discipline.")]),

    dict(slug="english-handwriting", name="English Handwriting", fee8=12000,
         description="A dedicated hand-improvement track for English script — print and cursive — built around steady, guided repetition.",
         who_for="Students wanting a polished, professional English handwriting style.",
         requirements="No prior experience needed.",
         outcomes=["Clean print and cursive English letterforms", "Even spacing across words and paragraphs", "A personal, legible everyday style"],
         materials=["Pen", "Ruled notebook", "Practice worksheets"],
         curriculum=["English alphabet forms in print", "Cursive English fundamentals", "Word and sentence spacing",
                      "Joins and ligatures", "Paragraph writing practice", "Speed writing exercises",
                      "Personal style refinement", "Final showcase piece"],
         faq=[("Will this help with exams?", "Yes — many students join to write faster and more legibly under exam conditions.")]),

    dict(slug="urdu-handwriting", name="Urdu Handwriting", fee8=12000,
         description="Structured Nastaliq-based handwriting training for clear, confident everyday Urdu writing.",
         who_for="Students and professionals wanting a neater, more consistent Urdu hand.",
         requirements="Basic familiarity with Urdu letters is helpful but not required.",
         outcomes=["Correct letterform shapes across positions", "Confident joining (rabt) of letters", "Even, legible paragraph writing"],
         materials=["Pen", "Practice notebook"],
         curriculum=["Urdu script basics, grip and Nastaliq introduction", "Individual letterforms (huroof)",
                      "Joining letters (rabt)", "Word formation and diacritics", "Sentence structure and spacing",
                      "Paragraph practice", "Stylistic refinement", "Final composition piece"],
         faq=[("Is this the same as the Calligraphy course?", "No — this focuses on clear everyday handwriting rather than decorative calligraphic art.")]),

    dict(slug="arabic-handwriting", name="Arabic Handwriting", fee8=12000,
         description="Focused Arabic script handwriting practice, from individual letterforms to fluent connected writing.",
         who_for="Students wanting clear, correct, everyday Arabic handwriting.",
         requirements="Basic familiarity with the Arabic alphabet is helpful but not required.",
         outcomes=["Correct letterforms by position (initial, medial, final)", "Confident joining and ligatures", "Fluent sentence and paragraph writing"],
         materials=["Pen", "Practice notebook"],
         curriculum=["Arabic script fundamentals and letter shapes by position", "Initial, medial and final letterforms",
                      "Joining rules and ligatures", "Diacritical marks (tashkeel)", "Word and sentence construction",
                      "Paragraph practice", "Style refinement", "Final composition piece"],
         faq=[("Do you teach diacritics (tashkeel)?", "Yes, covered in week four as part of accurate, readable writing.")]),

    dict(slug="drawing", name="Drawing", fee8=29000,
         description="A complete observational drawing foundation — line, form, light and composition — building toward confident original work.",
         who_for="Beginners building a foundation, and intermediate students sharpening technique.",
         requirements="No prior experience needed.",
         outcomes=["Accurate observational line work", "Understanding of proportion and perspective", "Confident shading and light control",
                    "A finished, original composition"],
         materials=["Graphite pencils (HB–6B)", "Eraser", "Sketchbook", "Blending tools"],
         curriculum=["Observational drawing and line fundamentals", "Shape and form studies", "Proportion and measurement technique",
                      "Perspective (one- and two-point)", "Light, shadow and shading technique", "Still life composition",
                      "Portrait and figure drawing basics", "Final composition and critique"],
         faq=[("Do I need drawing experience to join?", "No — the first weeks are built for complete beginners.")]),

    dict(slug="painting", name="Painting", fee8=39000,
         description="A hands-on painting programme covering colour theory, mixing and composition across still life and landscape work.",
         who_for="Students moving from drawing into colour, and painters refining technique.",
         requirements="Basic drawing familiarity is helpful but not required.",
         outcomes=["Confident colour mixing and value control", "Working knowledge of composition principles", "A finished original painting"],
         materials=["Acrylic or watercolour paints", "Brush set", "Palette", "Canvas or paper"],
         curriculum=["Colour theory and material handling", "Mixing and value studies", "Composition principles",
                      "Still life painting", "Landscape technique", "Layering and texture building",
                      "Personal style exploration", "Final painting and presentation"],
         faq=[("Which medium do you teach?", "Acrylic by default; watercolour or oil can be arranged with your teacher.")]),

    dict(slug="photography", name="Photography", fee8=30000,
         description="Camera fundamentals through to a finished personal shoot — exposure, composition, lighting and basic editing.",
         who_for="Beginners with any camera (including phone cameras) wanting to shoot with real intention.",
         requirements="A camera or a smartphone with manual/pro camera controls.",
         outcomes=["Full control of exposure (aperture, shutter, ISO)", "Strong compositional instincts", "Basic lighting and editing skills",
                    "A personal photo portfolio piece"],
         materials=["Camera or smartphone", "(Optional) tripod"],
         curriculum=["Camera fundamentals and the exposure triangle", "Composition and framing", "Lighting technique, natural and artificial",
                      "Portrait photography", "Editorial and product photography basics", "Editing and post-processing fundamentals",
                      "Personal project shoot", "Portfolio review and final presentation"],
         faq=[("Do I need a DSLR?", "No — the course is built to work with phone cameras too.")]),

    dict(slug="graphic-design", name="Graphic Design", fee8=28000,
         description="Core design thinking — typography, layout and branding — applied through a real personal design project.",
         who_for="Beginners and self-taught designers wanting formal design fundamentals.",
         requirements="No prior software experience required; guidance on tools provided in class.",
         outcomes=["Strong grasp of layout, contrast and hierarchy", "Typography fundamentals", "A basic personal branding project"],
         materials=["Laptop (design software guidance provided in class)"],
         curriculum=["Design principles: balance, contrast, hierarchy", "Typography fundamentals", "Colour theory for design",
                      "Layout and grid systems", "Branding and logo design basics", "Digital tools workflow",
                      "Personal branding project", "Portfolio piece and presentation"],
         faq=[("Which software do you use?", "Confirmed with your teacher based on what's available to you — guidance is provided either way.")]),

    dict(slug="miniature", name="Miniature Painting", fee8=38000,
         description="Traditional miniature painting technique — fine detail brushwork, motifs and layered colour — built week by week into a finished piece.",
         who_for="Students drawn to detailed, traditional South Asian and Persianate miniature art.",
         requirements="Basic drawing familiarity is helpful.",
         outcomes=["Fine detail brush control", "Traditional motif and pattern work", "A finished miniature composition"],
         materials=["Fine detail brushes", "Miniature paints", "Prepared board or wasli paper"],
         curriculum=["History and materials of miniature art", "Fine detail brush control", "Traditional motifs and patterns",
                      "Colour layering technique", "Figure and border work", "Gold leaf and illumination basics",
                      "Composing a full miniature piece", "Final miniature artwork and presentation"],
         faq=[("Is gold leaf work included?", "Yes, introduced in week six as part of traditional illumination technique.")]),

    dict(slug="sculpture", name="Sculpture", fee8=39000,
         description="Hands-on three-dimensional form-building, from material fundamentals to a finished sculptural piece.",
         who_for="Students wanting to work in three dimensions for the first time, or refine existing sculpting skills.",
         requirements="No prior experience needed.",
         outcomes=["Confident handling of sculpting materials", "Understanding of form, volume and structure", "A finished sculptural piece"],
         materials=["Modelling clay", "Sculpting tools", "Armature wire"],
         curriculum=["Material fundamentals (clay and modelling basics)", "Form and volume studies", "Armature and structural basics",
                      "Surface texture technique", "Figure or object study", "Refining detail and proportion",
                      "Finishing technique", "Final sculpture piece and presentation"],
         faq=[("What material do we sculpt with?", "Modelling clay by default; other media can be discussed with your teacher.")]),

    dict(slug="texture-painting", name="Texture Painting", fee8=37000,
         description="Large-scale, tactile mixed-media painting — building texture through layered mediums, palette knife work and metallic accents.",
         who_for="Painters wanting to move beyond flat colour into dimensional, textural work.",
         requirements="Basic painting familiarity is helpful but not required.",
         outcomes=["Confident use of texture mediums and tools", "Understanding of organic and abstract composition", "A finished large-scale textured piece"],
         materials=["Palette knives", "Texture medium / gesso", "Acrylic paints, including metallics"],
         curriculum=["Texture materials and tools", "Building base texture layers", "Colour and texture interplay",
                      "Organic and abstract composition technique", "Metallic and mixed-media accents", "Large-scale composition planning",
                      "Full canvas execution", "Final piece and presentation"],
         faq=[("Do you cover metallic finishes?", "Yes — week five is dedicated to metallic and mixed-media accents.")]),

    dict(slug="film-tv", name="Multimedia / Film & TV", fee8=39000,
         description="A practical introduction to film and video production — from pre-production planning to a final edited piece.",
         who_for="Students interested in filmmaking, video content or on-set production work.",
         requirements="A camera or smartphone capable of recording video.",
         outcomes=["Pre-production planning (concept, script, storyboard)", "Camera operation and shot composition",
                    "Basic editing and colour/audio workflow", "A finished short project"],
         materials=["Camera or smartphone", "(Optional) basic microphone"],
         curriculum=["Pre-production fundamentals: concept, scripting, storyboarding", "Camera operation and shot composition",
                      "Lighting and sound basics", "Interview and documentary technique", "Editing software fundamentals",
                      "Colour grading and audio mixing basics", "Short project production", "Final cut and screening"],
         faq=[("Do we produce a real short project?", "Yes — the final two weeks are dedicated to shooting and editing your own piece.")]),

    dict(slug="fashion-design", name="Fashion Design", fee8=None,
         description="An introduction to fashion design — sketching, textiles and garment construction — building toward a small personal collection concept.",
         who_for="Students exploring fashion illustration and design fundamentals for the first time.",
         requirements="No prior experience needed.",
         outcomes=["Fashion sketching and proportion (croquis)", "Understanding of textile and garment basics", "A final look presentation"],
         materials=["Sketchbook", "Fashion markers or coloured pencils", "Fabric swatches (provided in class)"],
         curriculum=["Fashion sketching fundamentals (croquis, proportions)", "Textile and fabric basics", "Garment construction principles",
                      "Colour and pattern in fashion", "Draping and pattern-making basics", "Developing a mini collection concept",
                      "Illustration and presentation technique", "Final look presentation"],
         faq=[("Why is the fee not listed yet?", "Fashion Design pricing is being finalised — contact us and our team will confirm current fees.")]),

    dict(slug="spoken-english", name="Spoken English", fee8=39000,
         description="A confidence-first spoken English programme covering pronunciation, conversation and presentation skills.",
         who_for="Students and professionals who want to speak English more fluently and confidently.",
         requirements="No prior fluency required.",
         outcomes=["Clearer pronunciation and improved confidence", "Fluent everyday conversation", "Presentation and interview-ready communication"],
         materials=["Notebook"],
         curriculum=["Pronunciation and confidence-building fundamentals", "Everyday conversation practice", "Grammar in spoken context",
                      "Vocabulary building and idioms", "Public speaking basics", "Presentation skills",
                      "Interview and professional communication practice", "Final presentation and assessment"],
         faq=[("Is this a grammar course?", "Grammar is covered only as it supports speaking — the focus throughout is spoken fluency.")]),
]

for c in COURSES:
    c["pricing"] = suggest_pricing(c["fee8"])

TESTIMONIALS = [
    dict(name="Calligraphy student", quote="I came in only knowing how to hold a pen properly. By week eight I had a finished piece I was genuinely proud to frame."),
    dict(name="Painting student", quote="The studio pushed me past copying references and into actually composing my own work — that shift was the whole point, looking back."),
    dict(name="Parent of a Drawing student", quote="My daughter's observation skills and patience with detail have both grown noticeably since she started."),
]

WORKSHOPS = [
    dict(title="Introduction to Islamic Geometric Pattern", kind="Workshop", note="Schedule to be confirmed"),
    dict(title="Weekend Calligraphy Masterclass", kind="Masterclass", note="Schedule to be confirmed"),
    dict(title="Portrait Drawing Open Studio", kind="Open Studio", note="Schedule to be confirmed"),
    dict(title="Student Exhibition Evening", kind="Exhibition", note="Schedule to be confirmed"),
]

GALLERY_ITEMS = [
    ("Calligraphy", "Nastaliq study"), ("Calligraphy", "Thuluth composition"),
    ("Drawing", "Portrait study"), ("Drawing", "Still life, graphite"),
    ("Painting", "Landscape in acrylic"), ("Painting", "Colour study"),
    ("Texture Painting", "Gold-on-black canvas"), ("Photography", "Editorial portrait"),
    ("Student Projects", "Final calligraphy piece"), ("Student Projects", "Final drawing composition"),
    ("Miniature", "Traditional motif study"), ("Sculpture", "Form study, clay"),
]

FAQS = [
    ("What courses does Cairo School of Art & Calligraphy offer?",
     "Calligraphy, Handwriting (English, Urdu and Arabic), Drawing, Painting, Photography, Graphic Design, Miniature Painting, Sculpture, Texture Painting, Multimedia/Film &amp; TV, Fashion Design and Spoken English. See the Courses page for details on each."),
    ("Do I need prior art experience to enrol?",
     "No. Most programmes are built for complete beginners, and teachers adjust pace for students with existing experience."),
    ("What learning modalities are available?",
     "Online, in-person at our studios, home tutoring, or a hybrid of online and in-person."),
    ("Where are your studios located?",
     "Lahore and Islamabad. Exact studio addresses are confirmed directly when you enquire."),
    ("How long are the courses?",
     "8 weeks is the standard programme length. Shorter (2, 4 or 6 week) and longer (3 or 6 month) options are available for most courses."),
    ("What payment methods do you accept?",
     "Easypaisa, JazzCash, NayaPay, bank transfer and cash. Details are confirmed when you enrol."),
    ("Can I pay my course fee in installments?",
     "Yes, installment plans can be arranged — speak with our team when you apply."),
    ("Do you offer a certificate on completion?",
     "Yes, a Certificate of Completion is issued at the end of each programme."),
]

# --------------------------------------------------------------------------
# NAV / TEMPLATES
# --------------------------------------------------------------------------

NAV_ITEMS = [
    ("home", "Home", "index.html"),
    ("about", "About", "about.html"),
    ("courses", "Courses", "courses.html"),
    ("admissions", "Admissions", "admissions.html"),
    ("gallery", "Gallery", "gallery.html"),
    ("workshops", "Workshops", "workshops.html"),
    ("contact", "Contact", "contact.html"),
]

def fmt_fee(v):
    return f"PKR {v:,}" if v is not None else "To be announced"

def head_html(title, description, prefix, canonical_path, extra_head=""):
    canonical = f"{SITE_URL}/{canonical_path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {SITE_NAME}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title} · {SITE_NAME}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#15120F">
<link rel="icon" href="{FAVICON_HREF}">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
{extra_head}</head>
<body>
"""

def header_html(prefix, active):
    def link_class(key):
        return "nav__link is-active" if key == active else "nav__link"
    links = "\n".join(
        f'<li><a href="{prefix}{href}" class="{link_class(key)}">{label}</a></li>'
        for key, label, href in NAV_ITEMS
    )
    mobile_links = "\n".join(
        f'<a href="{prefix}{href}" class="mobile-nav__link">{label}</a>'
        for key, label, href in NAV_ITEMS
    )
    return f"""<header class="site-header">
  <div class="container">
    <a href="{prefix}index.html" class="brand">
      <span class="brand__name">Cairo</span>
      <span class="brand__sub">School of Art &amp; Calligraphy</span>
    </a>
    <nav class="nav" aria-label="Primary">
      <ul class="nav__list">
        {links}
      </ul>
      <div class="header-actions">
        <a href="{prefix}portal.html" class="btn btn--outline btn--sm" style="border-color:#D3B679;color:#EDE7DA;">Portal</a>
      </div>
      <button class="nav__toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
        <span></span><span></span><span></span>
      </button>
    </nav>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav">
  <div class="mobile-nav__list">
    {mobile_links}
  </div>
  <div class="mobile-nav__foot">
    <a href="{prefix}admissions.html" class="btn btn--oxblood btn--block">Apply Now</a>
    <a href="{prefix}portal.html" class="btn btn--outline btn--block">Portal</a>
  </div>
</div>
"""

def footer_html(prefix):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <div class="brand">
          <span class="brand__name">Cairo</span>
          <span class="brand__sub">School of Art &amp; Calligraphy</span>
        </div>
        <p class="footer__tag">{TAGLINE}.</p>
        <p style="font-size:.75rem;opacity:.6;margin-top:1rem;">In collaboration with Al Azhar Fine Art Studio</p>
      </div>
      <div class="footer__col">
        <h4>Explore</h4>
        <ul class="footer__list">
          <li><a href="{prefix}courses.html">Courses</a></li>
          <li><a href="{prefix}admissions.html">Admissions</a></li>
          <li><a href="{prefix}gallery.html">Gallery</a></li>
          <li><a href="{prefix}workshops.html">Workshops &amp; Events</a></li>
          <li><a href="{prefix}testimonials.html">Testimonials</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Studio</h4>
        <ul class="footer__list">
          <li><a href="{prefix}about.html">About</a></li>
          <li><a href="{prefix}teachers.html">Teachers</a></li>
          <li><a href="{prefix}faq.html">FAQs</a></li>
          <li><a href="{prefix}portal.html">Student &amp; Admin Portal</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Contact</h4>
        <ul class="footer__list">
          <li>Lahore &amp; Islamabad</li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="https://wa.me/{WA_INTL}" target="_blank" rel="noopener">WhatsApp: {WA_DISPLAY}</a></li>
          <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">@cairo.artstudio</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year></span> {SITE_NAME}. All rights reserved.</span>
      <span>Easypaisa · JazzCash · NayaPay · Bank Transfer · Cash</span>
    </div>
  </div>
</footer>
"""

def page_shell(title, description, prefix, canonical_path, content, active="", extra_head="", extra_scripts=""):
    return (head_html(title, description, prefix, canonical_path, extra_head)
            + header_html(prefix, active)
            + f'<main>{content}</main>'
            + footer_html(prefix)
            + f'<script src="{prefix}assets/js/main.js"></script>'
            + extra_scripts
            + "\n</body>\n</html>\n")

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def feature_block(title, text):
    return f"""<div class="feature reveal">
      <svg class="feature__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="12" cy="12" r="9"/><path d="M8 12l2.5 2.5L16 9"/></svg>
      <div class="feature__title">{title}</div>
      <p class="feature__text">{text}</p>
    </div>"""

# --------------------------------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------------------------------

def home_content():
    featured = [c for c in COURSES if c["slug"] in ("calligraphy", "drawing", "painting", "photography")]
    featured_cards = "\n".join(f"""
      <div class="card course-card reveal">
        <span class="card__eyebrow">{c['name']}</span>
        <h3 class="card__title">{c['name']}</h3>
        <p style="font-size:.9rem;opacity:.8;">{c['description']}</p>
        <div class="card__meta"><span>8 weeks (default)</span><span class="card__price">{fmt_fee(c['fee8'])}</span></div>
        <div class="card__foot"><a href="courses/{c['slug']}/" class="btn btn--outline btn--sm">View Course</a></div>
      </div>""" for c in featured)

    gallery_tiles = "\n".join(f"""
      <div class="art-tile reveal"><div class="art-tile__label"><div class="art-tile__cat">{cat}</div><div class="art-tile__title">{title}</div></div></div>"""
      for cat, title in GALLERY_ITEMS[:6])

    workshop_cards = "\n".join(f"""
      <div class="card reveal">
        <span class="badge badge--demo">Demo content</span>
        <h3 class="card__title">{w['title']}</h3>
        <p style="font-size:.85rem;opacity:.75;">{w['kind']} · {w['note']}</p>
      </div>""" for w in WORKSHOPS[:3])

    testimonial_cards = "\n".join(f"""
      <div class="testimonial reveal">
        <p>&ldquo;{t['quote']}&rdquo;</p>
        <cite>{t['name']} <span class="badge badge--demo" style="margin-left:.5rem;">Demo</span></cite>
      </div>""" for t in TESTIMONIALS)

    return f"""
<section class="hero">
  <div class="container hero__inner">
    <p class="hero__collab">In collaboration with Al Azhar Fine Art Studio</p>
    <h1 class="hero__title">CAIRO<small>School of Art &amp; Calligraphy</small></h1>
    {STROKE_SVG}
    <p class="hero__tagline">&ldquo;{TAGLINE}&rdquo;</p>
    <div class="btn-row hero__cta">
      <a href="courses.html" class="btn btn--gold">Explore Courses</a>
      <a href="admissions.html" class="btn btn--oxblood">Apply Now</a>
      <a href="contact.html" class="btn btn--outline" style="border-color:#D3B679;">Contact Us</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--2" style="align-items:center;">
      <div class="reveal">
        <p class="eyebrow">About the school</p>
        <h2>A studio built for serious, unhurried craft</h2>
        <p class="lede">Cairo School of Art &amp; Calligraphy, in collaboration with Al Azhar Fine Art Studio, teaches calligraphy, drawing, painting, photography, design and more &mdash; in Lahore and Islamabad, online and in person.</p>
        <div style="margin-top:1.5rem;"><a href="about.html" class="btn btn--ghost">Discover Our Story &rarr;</a></div>
      </div>
      <div class="art-tile reveal" style="--tile-bg:linear-gradient(155deg,#7A2331,#15120F);">
        <div class="art-tile__label"><div class="art-tile__cat">Est. 2018</div><div class="art-tile__title">Cairo Art Studio</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Programmes</p>
      <h2>Featured Courses</h2>
      <p class="lede">A selection from our full catalogue of fifteen disciplines.</p>
    </div>
    <div class="grid grid--4">
      {featured_cards}
    </div>
    <div class="text-center" style="margin-top:2.5rem;"><a href="courses.html" class="btn btn--outline">View All Courses</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Why Cairo School of Art</p>
      <h2>Built around real practice, not shortcuts</h2>
    </div>
    <div class="grid grid--4">
      {feature_block("Professional Art Education", "Structured, discipline-specific curricula, not generic craft classes.")}
      {feature_block("Experienced Instructors", "Practising artists and calligraphers lead every programme.")}
      {feature_block("Flexible Learning", "Online, in-person, home tutor or hybrid &mdash; you choose.")}
      {feature_block("Portfolio Development", "Every course ends in a finished, presentation-ready piece.")}
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Learning modalities</p>
      <h2>Learn the way that fits your life</h2>
    </div>
    <div class="grid grid--4">
      <div class="modality-card reveal" style="background:var(--ink-soft);border-color:rgba(176,141,70,.3);">
        <div class="modality-card__title">Online</div><p style="font-size:.9rem;opacity:.8;">Learn remotely from anywhere.</p>
      </div>
      <div class="modality-card reveal" style="background:var(--ink-soft);border-color:rgba(176,141,70,.3);">
        <div class="modality-card__title">In-Person</div><p style="font-size:.9rem;opacity:.8;">Learn physically at the studio.</p>
      </div>
      <div class="modality-card reveal" style="background:var(--ink-soft);border-color:rgba(176,141,70,.3);">
        <div class="modality-card__title">Home Tutor</div><p style="font-size:.9rem;opacity:.8;">Professional learning at home.</p>
      </div>
      <div class="modality-card reveal" style="background:var(--ink-soft);border-color:rgba(176,141,70,.3);">
        <div class="modality-card__title">Hybrid</div><p style="font-size:.9rem;opacity:.8;">Combine online and in-person learning.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Locations</p>
    <h2>Lahore &amp; Islamabad</h2>
    <p class="lede" style="margin:0 auto;">Studio addresses are confirmed directly when you enquire &mdash; <a href="contact.html" style="color:var(--oxblood);font-weight:600;">get in touch</a> for the nearest location.</p>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Student artwork</p>
      <h2>From the studio</h2>
    </div>
    <div class="grid grid--3">
      {gallery_tiles}
    </div>
    <div class="text-center" style="margin-top:2.5rem;"><a href="gallery.html" class="btn btn--outline">View Full Gallery</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Workshops &amp; events</p>
      <h2>Beyond the core programmes</h2>
    </div>
    <div class="grid grid--3">
      {workshop_cards}
    </div>
    <div class="text-center" style="margin-top:2.5rem;"><a href="workshops.html" class="btn btn--outline">See All Workshops &amp; Events</a></div>
  </div>
</section>

<section class="section section--olive">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Testimonials</p>
      <h2 style="color:#fff;">What students say</h2>
    </div>
    <div class="grid grid--3">
      {testimonial_cards}
    </div>
  </div>
</section>

<section class="section section--ink text-center">
  <div class="container reveal">
    <h2 style="color:#fff;max-width:16ch;margin:0 auto;">Your creativity deserves a place to grow.</h2>
    <div class="btn-row" style="justify-content:center;margin-top:2rem;">
      <a href="admissions.html" class="btn btn--gold">Start Your Journey</a>
    </div>
  </div>
</section>
"""

def about_content():
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">About the school</p>
    <h1 style="color:#fff;">Cairo School of Art &amp; Calligraphy</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">In collaboration with Al Azhar Fine Art Studio</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid--2" style="align-items:center;">
    <div class="reveal">
      <p class="eyebrow">Our story</p>
      <h2>Founded on the belief that craft still matters</h2>
      <p class="lede">Cairo Art Studio was founded in 2018 as a home for serious, hands-on art education &mdash; calligraphy, drawing, painting, photography, design and more. Cairo School of Art &amp; Calligraphy carries that same practice forward, in collaboration with Al Azhar Fine Art Studio, across Lahore and Islamabad.</p>
      <p class="lede" style="margin-top:1rem;">Every programme is built the same way: real technique, real feedback, and a finished piece to show for it.</p>
    </div>
    <div class="art-tile reveal" style="--tile-bg:linear-gradient(155deg,#5B5F35,#15120F);">
      <div class="art-tile__label"><div class="art-tile__cat">Since 2018</div><div class="art-tile__title">Cairo Art Studio</div></div>
    </div>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">What we teach</p>
      <h2>Fifteen disciplines, one standard</h2>
      <p class="lede" style="margin:0 auto;">Calligraphy, Handwriting (English, Urdu, Arabic), Drawing, Painting, Photography, Graphic Design, Miniature Painting, Sculpture, Texture Painting, Multimedia/Film &amp; TV, Fashion Design and Spoken English.</p>
    </div>
    <div class="text-center"><a href="courses.html" class="btn btn--oxblood">Browse the Full Catalogue</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">How you can learn</p>
      <h2>Online, in-person, home tutor or hybrid</h2>
    </div>
    <div class="grid grid--4">
      <div class="modality-card reveal"><div class="modality-card__title">Online</div><p style="font-size:.9rem;opacity:.75;">Learn remotely from anywhere.</p></div>
      <div class="modality-card reveal"><div class="modality-card__title">In-Person</div><p style="font-size:.9rem;opacity:.75;">Learn physically at the studio.</p></div>
      <div class="modality-card reveal"><div class="modality-card__title">Home Tutor</div><p style="font-size:.9rem;opacity:.75;">Professional learning at home.</p></div>
      <div class="modality-card reveal"><div class="modality-card__title">Hybrid</div><p style="font-size:.9rem;opacity:.75;">Combine online and in-person learning.</p></div>
    </div>
  </div>
</section>

<section class="section section--olive text-center">
  <div class="container reveal">
    <h2 style="color:#fff;">&ldquo;{TAGLINE}.&rdquo;</h2>
    <div style="margin-top:1.5rem;"><a href="admissions.html" class="btn btn--gold">Start Your Journey</a></div>
  </div>
</section>
"""

def courses_listing_content():
    rows = "\n".join(f"""<tr>
      <td><a href="courses/{c['slug']}/" style="font-weight:600;">{c['name']}</a></td>
      <td class="num">{fmt_fee(c['fee8'])}</td>
      <td>8 weeks (default)</td>
      <td><a href="courses/{c['slug']}/" class="btn btn--sm btn--outline">View</a></td>
    </tr>""" for c in COURSES)

    cards = "\n".join(f"""
      <div class="card course-card reveal">
        <span class="card__eyebrow">{'Fee to be announced' if c['fee8'] is None else '8-Week Programme'}</span>
        <h3 class="card__title">{c['name']}</h3>
        <p style="font-size:.9rem;opacity:.8;">{c['description']}</p>
        <div class="card__meta"><span>2&ndash;8 wks / 3&ndash;6 mo</span><span class="card__price">{fmt_fee(c['fee8'])}</span></div>
        <div class="card__foot"><a href="courses/{c['slug']}/" class="btn btn--outline btn--sm">View Course</a></div>
      </div>""" for c in COURSES)

    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Programmes</p>
    <h1 style="color:#fff;">Courses</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">Fifteen disciplines. The 8-week fee is confirmed &mdash; every other duration shown is a suggested starting price for the team to confirm at enrolment.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid--3">
      {cards}
    </div>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">8-week fees</p>
      <h2>Full fee table</h2>
      <p class="lede">2, 4 and 6-week, and 3 and 6-month pricing is shown on each course page &mdash; longer programmes may carry a package discount, confirmed at enrolment.</p>
    </div>
    <div class="table-wrap reveal">
      <table class="fee-table">
        <thead><tr><th>Course</th><th>8-Week Fee</th><th>Default Schedule</th><th></th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>
"""

def course_detail_content(c, prefix):
    outcomes = "\n".join(f"<li>{o}</li>" for o in c["outcomes"])
    materials = ", ".join(c["materials"])
    curriculum_rows = "\n".join(
        f'<div class="curriculum__row"><div class="curriculum__wk">Week {i+1}</div><div>{w}</div></div>'
        for i, w in enumerate(c["curriculum"])
    )
    pricing_rows = "\n".join(
        f"""<tr><td>{d}</td><td class="num">{fmt_fee(c['pricing'][d])}</td>
        <td>{'Confirmed' if d == '8 Weeks' else ('&mdash;' if c['pricing'][d] is None else 'Suggested &mdash; admin to confirm')}</td></tr>"""
        for d in DURATIONS
    )
    faq_html = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in c["faq"])
    tbd_note = "" if c["fee8"] is not None else '<p class="badge badge--tbd" style="margin-top:.75rem;">Fee to be announced &mdash; contact us</p>'

    return f"""
<section class="section section--ink">
  <div class="container reveal">
    <p class="eyebrow">Course</p>
    <h1 style="color:#fff;">{c['name']}</h1>
    <p class="lede" style="color:var(--bone);opacity:.85;">{c['description']}</p>
    {tbd_note}
    <div class="btn-row" style="margin-top:1.5rem;">
      <a href="{prefix}admissions.html" class="btn btn--gold">Apply for This Course</a>
      <a href="{prefix}courses.html" class="btn btn--outline" style="border-color:#D3B679;">&larr; All Courses</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid grid--2">
    <div class="reveal">
      <h2>Who it's for</h2>
      <p class="lede">{c['who_for']}</p>
      <h3 style="margin-top:2rem;">Requirements</h3>
      <p class="lede">{c['requirements']}</p>
      <h3 style="margin-top:2rem;">Materials</h3>
      <p class="lede">{materials}.</p>
    </div>
    <div class="reveal">
      <h2>What you'll learn</h2>
      <ul class="flow" style="opacity:.85;list-style:none;padding:0;">{outcomes}</ul>
      <p style="margin-top:1.5rem;font-size:.9rem;opacity:.7;">A Certificate of Completion is issued once you finish the programme.</p>
    </div>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Curriculum</p>
      <h2>8-Week Programme Outline</h2>
      <p class="lede">A proposed starting structure &mdash; your teacher may adapt pacing to the class.</p>
    </div>
    <div class="curriculum reveal">{curriculum_rows}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Duration &amp; fees</p>
      <h2>Choose your pace</h2>
    </div>
    <div class="table-wrap reveal">
      <table class="fee-table">
        <thead><tr><th>Duration</th><th>Fee</th><th>Status</th></tr></thead>
        <tbody>{pricing_rows}</tbody>
      </table>
    </div>
    <p style="font-size:.85rem;opacity:.65;margin-top:1rem;">Available online, in-person, home tutor or hybrid. Weekday and weekend scheduling both offered.</p>
  </div>
</section>

<section class="section section--parchment-deep">
  <div class="container" style="max-width:760px;">
    <div class="section-head reveal"><p class="eyebrow">FAQ</p><h2>Course Questions</h2></div>
    <div class="reveal">{faq_html}</div>
  </div>
</section>

<section class="section section--ink text-center">
  <div class="container reveal">
    <h2 style="color:#fff;">Ready to start {c['name']}?</h2>
    <div style="margin-top:1.5rem;"><a href="{prefix}admissions.html" class="btn btn--gold">Apply Now</a></div>
  </div>
</section>
"""

def admissions_content():
    course_options = "\n".join(f'<option value="{c["slug"]}">{c["name"]}</option>' for c in COURSES)
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Admissions</p>
    <h1 style="color:#fff;">Apply to Cairo School of Art</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">Seven short steps. Nothing is sent anywhere until you review and confirm at the end.</p>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px;">

    <div class="progress-steps" id="progress-steps">
      <div class="progress-steps__item is-active" data-n="1"><span class="progress-steps__label">Personal</span></div>
      <div class="progress-steps__item" data-n="2"><span class="progress-steps__label">Education</span></div>
      <div class="progress-steps__item" data-n="3"><span class="progress-steps__label">Course</span></div>
      <div class="progress-steps__item" data-n="4"><span class="progress-steps__label">Documents</span></div>
      <div class="progress-steps__item" data-n="5"><span class="progress-steps__label">More</span></div>
      <div class="progress-steps__item" data-n="6"><span class="progress-steps__label">Review</span></div>
      <div class="progress-steps__item" data-n="7"><span class="progress-steps__label">Done</span></div>
    </div>

    <form id="admission-form" novalidate>

      <div class="form-step is-active" data-step="1">
        <h2>Personal Information</h2>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Full Name <span class="req">*</span></label>
            <input type="text" class="form-input" data-field="Full Name" required></div>
          <div class="form-group"><label class="form-label">Father / Guardian Name <span class="req">*</span></label>
            <input type="text" class="form-input" data-field="Father / Guardian Name" required></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Date of Birth <span class="req">*</span></label>
            <input type="date" class="form-input" data-field="Date of Birth" required></div>
          <div class="form-group"><label class="form-label">Gender <span class="req">*</span></label>
            <select class="form-select" data-field="Gender" required>
              <option value="">Select</option><option>Female</option><option>Male</option><option>Prefer not to say</option>
            </select></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">CNIC / B-Form</label>
            <input type="text" class="form-input" data-field="CNIC / B-Form" placeholder="XXXXX-XXXXXXX-X"></div>
          <div class="form-group"><label class="form-label">Phone <span class="req">*</span></label>
            <input type="tel" class="form-input" data-field="Phone" required></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">WhatsApp</label>
            <input type="tel" class="form-input" data-field="WhatsApp"></div>
          <div class="form-group"><label class="form-label">Email</label>
            <input type="email" class="form-input" data-field="Email"></div>
        </div>
        <div class="form-group"><label class="form-label">Address</label>
          <input type="text" class="form-input" data-field="Address"></div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">City</label><input type="text" class="form-input" data-field="City"></div>
          <div class="form-group"><label class="form-label">Country</label><input type="text" class="form-input" data-field="Country" value="Pakistan"></div>
        </div>
      </div>

      <div class="form-step" data-step="2">
        <h2>Education</h2>
        <div class="form-group"><label class="form-label">Highest Qualification</label>
          <input type="text" class="form-input" data-field="Highest Qualification"></div>
        <div class="form-group"><label class="form-label">Institution</label>
          <input type="text" class="form-input" data-field="Institution"></div>
        <div class="form-group"><label class="form-label">Previous Art Education</label>
          <textarea class="form-textarea" data-field="Previous Art Education"></textarea></div>
        <div class="form-group"><label class="form-label">Previous Experience</label>
          <textarea class="form-textarea" data-field="Previous Experience"></textarea></div>
        <div class="form-group"><label class="form-label">Current Occupation</label>
          <input type="text" class="form-input" data-field="Current Occupation"></div>
      </div>

      <div class="form-step" data-step="3">
        <h2>Course Selection</h2>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Course <span class="req">*</span></label>
            <select id="f-course" class="form-select" data-field="Course" required>
              <option value="">Select a course</option>
              {course_options}
            </select></div>
          <div class="form-group"><label class="form-label">Duration <span class="req">*</span></label>
            <select id="f-duration" class="form-select" data-field="Duration" required>
              <option value="">Select a course first</option>
            </select></div>
        </div>
        <p class="form-hint" id="fee-preview"></p>
        <div class="form-row" style="margin-top:1rem;">
          <div class="form-group"><label class="form-label">Modality <span class="req">*</span></label>
            <select class="form-select" data-field="Modality" required>
              <option value="">Select</option><option>Online</option><option>In-Person</option><option>Home Tutor</option><option>Hybrid</option>
            </select></div>
          <div class="form-group"><label class="form-label">Schedule</label>
            <select class="form-select" data-field="Schedule Preference">
              <option value="">Select</option><option>Weekday</option><option>Weekend</option><option>Flexible</option>
            </select></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Preferred Days</label>
            <input type="text" class="form-input" data-field="Preferred Days" placeholder="e.g. Mon, Wed, Fri"></div>
          <div class="form-group"><label class="form-label">Preferred Time</label>
            <input type="text" class="form-input" data-field="Preferred Time" placeholder="e.g. Evenings"></div>
        </div>
        <div class="form-group"><label class="form-label">Teacher Preference</label>
          <input type="text" class="form-input" data-field="Teacher Preference" placeholder="No preference"></div>
      </div>

      <div class="form-step" data-step="4">
        <h2>Documents</h2>
        <p class="form-hint" style="margin-bottom:1.25rem;">Online document storage isn't live yet &mdash; select files here to confirm what you have ready, then send them via WhatsApp after you submit this form.</p>
        <div class="form-group"><label class="form-label">Profile Photograph</label><div class="form-file"><input type="file" accept="image/*"></div></div>
        <div class="form-group"><label class="form-label">CNIC / B-Form</label><div class="form-file"><input type="file" accept="image/*,.pdf"></div></div>
        <div class="form-group"><label class="form-label">Portfolio</label><div class="form-file"><input type="file" accept="image/*,.pdf" multiple></div></div>
        <div class="form-group"><label class="form-label">Previous Artwork</label><div class="form-file"><input type="file" accept="image/*,.pdf" multiple></div></div>
      </div>

      <div class="form-step" data-step="5">
        <h2>Additional Information</h2>
        <div class="form-group"><label class="form-label">How did you hear about us?</label>
          <select class="form-select" data-field="How did you hear about us?">
            <option value="">Select</option><option>Instagram</option><option>Friend / Family</option><option>Google</option><option>Walk-in</option><option>Other</option>
          </select></div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Emergency Contact Name</label><input type="text" class="form-input" data-field="Emergency Contact Name"></div>
          <div class="form-group"><label class="form-label">Emergency Contact Phone</label><input type="tel" class="form-input" data-field="Emergency Contact Phone"></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label class="form-label">Parent / Guardian</label><input type="text" class="form-input" data-field="Parent / Guardian"></div>
          <div class="form-group"><label class="form-label">Parent / Guardian Phone</label><input type="tel" class="form-input" data-field="Parent / Guardian Phone"></div>
        </div>
        <div class="form-group"><label class="form-label">Additional Comments</label><textarea class="form-textarea" data-field="Additional Comments"></textarea></div>
        <div class="form-group"><label class="form-label">Special Requirements</label><textarea class="form-textarea" data-field="Special Requirements"></textarea></div>
      </div>

      <div class="form-step" data-step="6">
        <h2>Review Your Application</h2>
        <div id="review-output"></div>
        <label class="form-check" style="margin-top:1.5rem;">
          <input type="checkbox" data-field="Consent Confirmed" required>
          <span>I confirm the information above is accurate to the best of my knowledge.</span>
        </label>
      </div>

      <div class="form-step" data-step="7">
        <div class="success-box">
          <p class="eyebrow" style="justify-content:center;">Application Ready</p>
          <h2>Thank you &mdash; almost there.</h2>
          <p class="ref" id="ref-code"></p>
          <p style="opacity:.75;max-width:44ch;margin:0 auto 1.5rem;">This is a temporary reference for your own records &mdash; Cairo School of Art will confirm your official Application ID once your form is received. Send it to us on WhatsApp, or print a copy for your files.</p>
          <div class="btn-row no-print" style="justify-content:center;">
            <a href="#" id="btn-whatsapp" target="_blank" rel="noopener" class="btn btn--oxblood">Send via WhatsApp</a>
            <button type="button" id="btn-print" class="btn btn--outline">Print / Save Application</button>
          </div>
        </div>
      </div>

      <div class="btn-row no-print" style="justify-content:space-between;margin-top:2.5rem;">
        <button type="button" id="btn-back" class="btn btn--outline">Back</button>
        <button type="button" id="btn-next" class="btn btn--oxblood">Next</button>
        <button type="button" id="btn-submit" class="btn btn--oxblood" style="display:none;">Submit Application</button>
      </div>
    </form>
  </div>
</section>
"""

def gallery_content():
    categories = sorted(set(cat for cat, _ in GALLERY_ITEMS))
    tabs = '<button class="filter-tab is-active" data-filter="all">All</button>' + "".join(
        f'<button class="filter-tab" data-filter="{cat}">{cat}</button>' for cat in categories)
    tiles = "\n".join(f"""
      <div class="art-tile reveal" data-category="{cat}"><div class="art-tile__label"><div class="art-tile__cat">{cat}</div><div class="art-tile__title">{title}</div></div></div>"""
      for cat, title in GALLERY_ITEMS)
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Gallery &amp; student work</p>
    <h1 style="color:#fff;">From the Studio</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">
      <span class="badge badge--demo">Demo content</span> &mdash; placeholder tiles below stand in for real studio and student photography, added from Admin Settings once available.
    </p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="filter-tabs">{tabs}</div>
    <div class="grid grid--3">{tiles}</div>
  </div>
</section>
"""

def workshops_content():
    kinds = sorted(set(w["kind"] for w in WORKSHOPS))
    tabs = '<button class="filter-tab is-active" data-filter="all">All</button>' + "".join(
        f'<button class="filter-tab" data-filter="{k}">{k}</button>' for k in kinds)
    cards = "\n".join(f"""
      <div class="card reveal" data-category="{w['kind']}">
        <span class="badge badge--demo">Demo content</span>
        <h3 class="card__title">{w['title']}</h3>
        <p class="card__meta">{w['kind']} &middot; {w['note']}</p>
        <div class="card__foot"><a href="contact.html" class="btn btn--sm btn--outline">Register Interest</a></div>
      </div>""" for w in WORKSHOPS)
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Workshops &amp; events</p>
    <h1 style="color:#fff;">Beyond the Core Programmes</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;"><span class="badge badge--demo">Demo content</span> &mdash; real dates and registration open once confirmed by the studio.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="filter-tabs">{tabs}</div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>
"""

def testimonials_content():
    cards = "\n".join(f"""
      <div class="testimonial reveal">
        <p>&ldquo;{t['quote']}&rdquo;</p>
        <cite>{t['name']} <span class="badge badge--demo" style="margin-left:.5rem;">Demo</span></cite>
      </div>""" for t in TESTIMONIALS)
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Testimonials</p>
    <h1 style="color:#fff;">What Students Say</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;"><span class="badge badge--demo">Demo content</span> &mdash; shown as placeholders until real testimonials are added from Admin Settings.</p>
  </div>
</section>
<section class="section">
  <div class="container grid grid--3">{cards}</div>
</section>
"""

def faq_content():
    items = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS)
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">FAQ</p>
    <h1 style="color:#fff;">Frequently Asked Questions</h1>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:760px;">{items}</div>
</section>
"""

def teachers_content():
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Teachers</p>
    <h1 style="color:#fff;">Meet the Instructors</h1>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:640px;">
    <div class="empty-state reveal">
      <h3>Instructor profiles are coming soon</h3>
      <p>We're not listing placeholder names here &mdash; real teacher profiles will be added from Admin Settings once confirmed. Our team can tell you exactly who teaches a given course when you enquire.</p>
      <div class="btn-row" style="justify-content:center;">
        <a href="contact.html" class="btn btn--oxblood">Ask About a Teacher</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" class="btn btn--outline">Follow @cairo.artstudio</a>
      </div>
    </div>
  </div>
</section>
"""

def contact_content():
    return f"""
<section class="section section--ink">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Contact</p>
    <h1 style="color:#fff;">Get in Touch</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">Lahore &amp; Islamabad &mdash; studio addresses confirmed directly when you reach out.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid--2">
    <div class="reveal stack-lg">
      <div class="card">
        <h3 class="card__title">Call or WhatsApp</h3>
        <p style="opacity:.8;font-size:.9rem;">{PHONE_DISPLAY} &middot; WhatsApp {WA_DISPLAY}</p>
        <div class="btn-row" style="margin-top:.75rem;">
          <a href="tel:{PHONE_TEL}" class="btn btn--sm btn--outline">Call Now</a>
          <a href="https://wa.me/{WA_INTL}" target="_blank" rel="noopener" class="btn btn--sm btn--oxblood">WhatsApp Us</a>
        </div>
      </div>
      <div class="card">
        <h3 class="card__title">Instagram</h3>
        <p style="opacity:.8;font-size:.9rem;">@cairo.artstudio</p>
        <div class="btn-row" style="margin-top:.75rem;"><a href="{INSTAGRAM}" target="_blank" rel="noopener" class="btn btn--sm btn--outline">Visit Profile</a></div>
      </div>
      <div class="card">
        <h3 class="card__title">Payment Methods</h3>
        <p style="opacity:.8;font-size:.9rem;">Easypaisa &middot; JazzCash &middot; NayaPay &middot; Bank Transfer &middot; Cash</p>
        <p style="opacity:.6;font-size:.8rem;margin-top:.4rem;">Payment details are confirmed directly when you enrol.</p>
      </div>
      <div class="card">
        <h3 class="card__title">Locations</h3>
        <p style="opacity:.8;font-size:.9rem;">Lahore and Islamabad. Exact studio addresses are shared when you get in touch.</p>
      </div>
    </div>

    <div class="reveal">
      <h3 style="margin-bottom:1rem;">Send a Message</h3>
      <form id="contact-form">
        <div class="form-group"><label class="form-label">Name</label><input type="text" class="form-input" id="c-name"></div>
        <div class="form-group"><label class="form-label">Phone or Email</label><input type="text" class="form-input" id="c-contact"></div>
        <div class="form-group"><label class="form-label">Message</label><textarea class="form-textarea" id="c-message"></textarea></div>
        <button type="button" id="c-submit" class="btn btn--oxblood btn--block">Send via WhatsApp</button>
      </form>
    </div>
  </div>
</section>
"""

def portal_content():
    return f"""
<section class="section section--ink" style="min-height:55vh;display:flex;align-items:center;">
  <div class="container text-center reveal">
    <p class="eyebrow" style="justify-content:center;">Student &amp; Admin Portal</p>
    <h1 style="color:#fff;">Portal Login &mdash; Coming Soon</h1>
    <p class="lede" style="margin:1rem auto 0;color:var(--bone);opacity:.85;">Secure student and admin accounts go live once the school management system is connected to a real backend and database. This page is a placeholder &mdash; no login form is shown here because it wouldn't actually be able to verify anyone yet.</p>
    <div class="btn-row" style="justify-content:center;margin-top:2rem;">
      <a href="admissions.html" class="btn btn--gold">Apply for a Course</a>
      <a href="contact.html" class="btn btn--outline" style="border-color:#D3B679;">Contact the Studio</a>
    </div>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# BUILD
# --------------------------------------------------------------------------

def build_all():
    write("index.html", page_shell(SITE_NAME,
        "Cairo School of Art & Calligraphy, in collaboration with Al Azhar Fine Art Studio -- calligraphy, drawing, painting, photography and more in Lahore and Islamabad.",
        "", "index.html", home_content(), active="home"))

    write("about.html", page_shell("About",
        "The story, teaching philosophy and learning modalities behind Cairo School of Art & Calligraphy.",
        "", "about.html", about_content(), active="about"))

    write("courses.html", page_shell("Courses",
        "Browse all fifteen art, calligraphy and design courses offered by Cairo School of Art & Calligraphy, with fees and durations.",
        "", "courses.html", courses_listing_content(), active="courses"))

    write("admissions.html", page_shell("Admissions",
        "Apply to Cairo School of Art & Calligraphy in seven guided steps.",
        "", "admissions.html", admissions_content(), active="admissions",
        extra_scripts='\n<script src="assets/js/courses-data.js"></script>\n<script src="assets/js/admissions.js"></script>'))

    write("gallery.html", page_shell("Gallery & Student Work",
        "Student and studio artwork from Cairo School of Art & Calligraphy.",
        "", "gallery.html", gallery_content(), active="gallery",
        extra_scripts='\n<script src="assets/js/gallery.js"></script>'))

    write("workshops.html", page_shell("Workshops & Events",
        "Upcoming workshops, masterclasses and exhibitions at Cairo School of Art & Calligraphy.",
        "", "workshops.html", workshops_content(), active="workshops",
        extra_scripts='\n<script src="assets/js/gallery.js"></script>'))

    write("testimonials.html", page_shell("Testimonials",
        "What students say about Cairo School of Art & Calligraphy.",
        "", "testimonials.html", testimonials_content(), active=""))

    write("faq.html", page_shell("FAQ",
        "Frequently asked questions about courses, fees, modalities and admissions at Cairo School of Art & Calligraphy.",
        "", "faq.html", faq_content(), active=""))

    write("teachers.html", page_shell("Teachers",
        "Meet the instructors at Cairo School of Art & Calligraphy.",
        "", "teachers.html", teachers_content(), active=""))

    write("contact.html", page_shell("Contact",
        "Get in touch with Cairo School of Art & Calligraphy -- Lahore and Islamabad.",
        "", "contact.html", contact_content(), active="contact",
        extra_scripts='\n<script src="assets/js/contact.js"></script>'))

    write("portal.html", page_shell("Portal",
        "Student and admin portal login for Cairo School of Art & Calligraphy.",
        "", "portal.html", portal_content(), active=""))

    for c in COURSES:
        write(f"courses/{c['slug']}/index.html",
              page_shell(c["name"], c["description"], "../../", f"courses/{c['slug']}/",
                         course_detail_content(c, "../../"), active="courses"))

    js_courses = [{"slug": c["slug"], "name": c["name"], "pricing": c["pricing"]} for c in COURSES]
    write("assets/js/courses-data.js", "var CSA_COURSES = " + json.dumps(js_courses, indent=2) + ";\n")

    urls = (["index.html", "about.html", "courses.html", "admissions.html", "gallery.html", "workshops.html",
             "testimonials.html", "faq.html", "teachers.html", "contact.html", "portal.html"]
            + [f"courses/{c['slug']}/" for c in COURSES])
    sitemap_entries = "\n".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_entries}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"Built {11 + len(COURSES)} HTML pages + courses-data.js + sitemap.xml + robots.txt")

if __name__ == "__main__":
    build_all()
