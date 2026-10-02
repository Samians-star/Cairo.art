# Cairo School of Art & Calligraphy — Website

The public website for Cairo School of Art & Calligraphy, in collaboration with
Al Azhar Fine Art Studio. Plain HTML/CSS/JS — no build step, no framework —
so it deploys directly to **GitHub Pages** with zero configuration.

---

## What's here

A complete public site: Home, About, all 15 courses (listing + individual
pages), a 7-step Admissions form, Gallery, Workshops & Events, Testimonials,
FAQ, Teachers, Contact, and a Portal placeholder.

**What's not here, and why:** an admin dashboard, student/teacher accounts,
a real database, payments, and attendance. GitHub Pages only serves static
files — it cannot run a server, a database, or real authentication. Building
those for real (see **Roadmap**, below) is a separate, larger project. This
site is scoped honestly to what a static host can actually do, rather than
including fake login forms or fake "saved to database" messages that
wouldn't really work.

## Project structure

```
cairo-school-website/
├── index.html, about.html, courses.html, admissions.html, …   ← top-level pages
├── courses/<slug>/index.html                                  ← one folder per course (15)
├── assets/css/style.css                                       ← the entire design system
├── assets/js/                                                 ← main.js, admissions.js, gallery.js, contact.js, courses-data.js
├── scripts/build.py                                           ← regenerates every HTML page from the data below
├── sitemap.xml, robots.txt
```

## Editing content

Almost everything — course names, fees, durations, curricula, FAQs, home
page copy, testimonials, workshops — lives in one place:
**`scripts/build.py`**, in the `COURSES`, `TESTIMONIALS`, `WORKSHOPS`,
`GALLERY_ITEMS` and `FAQS` variables near the top of the file.

To change something (e.g. the Fashion Design fee, once it's finalised):

1. Edit the value in `scripts/build.py`
2. Regenerate every page:
   ```
   python3 scripts/build.py
   ```
3. Commit and push — GitHub Pages updates automatically.

This is a lightweight stand-in for the "admin can edit fees" requirement
until a real admin dashboard exists — one file to edit, instead of hunting
through 26 HTML files by hand.

Durations other than "8 Weeks" are **suggested prices**, calculated from the
8-week fee and clearly labelled as such on every course page — they are not
assumed to be proportional, per the original brief. Update them directly in
`COURSES` once real package pricing is decided.

## Preview locally

Don't just double-click `index.html` — the mobile menu and admissions form
still work, but relative paths behave better through an actual local server.
From the project folder:

```
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser.

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `cairo-school-website`) and push this
   folder's contents to it.
2. In the repo: **Settings → Pages → Build and deployment → Source: Deploy
   from a branch → Branch: `main` / root**.
3. Wait a minute or two — GitHub gives you a URL like
   `https://your-username.github.io/cairo-school-website/`.
4. Open `scripts/build.py`, update `SITE_URL` at the top to that real URL,
   re-run `python3 scripts/build.py`, and push again — this fixes the
   canonical links, `sitemap.xml` and `robots.txt`, which currently point at
   a placeholder.
5. (Optional) Add a custom domain under **Settings → Pages → Custom domain**.

## Content still marked as placeholder — replace before calling this "live"

- **Logo** — no logo file was provided, so the header/footer use a
  typographic wordmark ("Cairo / School of Art & Calligraphy"). Swap in the
  real logo image once you have it.
- **Photography** — the hero, course cards and gallery use abstract
  colour/typography treatments instead of stock photos, so nothing here
  misrepresents real students' or the studio's actual work. Replace with
  real photography whenever it's ready.
- **Fashion Design fee** — shown as "To be announced" everywhere, per the
  original brief.
- **Exact studio addresses** — intentionally not shown (only "Lahore" and
  "Islamabad"), per the original brief; the Contact page directs people to
  ask directly.
- **Teacher names** — not invented; the Teachers page is an honest "coming
  soon" state.
- **Gallery / Workshops / Testimonials** — demo content, clearly labelled
  with a "Demo content" badge on the page itself.

## How Admissions and Contact actually work right now

Both forms are fully interactive client-side (multi-step validation, a live
fee lookup, a review screen) but there's no backend yet to save anything to.
On submit, they build a pre-filled **WhatsApp message** to
0339 3338224 and let the applicant print/save a copy for their own records.
The reference code shown (`CSA-REF-…`) is a temporary local reference, not
an official sequential Application ID — that requires a real database (see
below) to guarantee uniqueness across everyone who applies.

## Roadmap: turning this into the full system from the original brief

The original spec (admin CRM, student/teacher portals, attendance, QR
check-in, payments, certificates, audit logs, role-based auth) is a real
backend application — a database, server-side authentication, and business
logic, none of which GitHub Pages can run. Suggested path, roughly following
the original brief's own phased build strategy:

1. **Backend & database** — e.g. Node.js/Express or Next.js API routes, with
   Postgres (Supabase, Neon or Railway all work well for this).
2. **Auth & roles** — Super Admin / Admin / Teacher / Student, enforced
   server-side (never just hidden nav items).
3. **Hosting for the backend** — GitHub Pages stays as the public site;
   the app itself deploys to something like Vercel, Render or Railway.
4. **Admissions → real submissions**, replacing the WhatsApp hand-off.
5. **Student & Admin portals**, replacing `portal.html`.
6. **Payments, attendance, certificates, receipts, reporting**, per the
   original brief's sections on each.

This is a genuinely large build in its own right — happy to start on it
whenever you're ready; it's a good candidate to scope out as its own project
rather than bolt on all at once.
