# -*- coding: utf-8 -*-
"""Generate ATS-friendly PDF CVs (PL + EN) for Jan Blaz.

Design goals (aligned with modern AI/ATS CV-screening guidelines):
  * Single-column layout with a clear reading order (parsers read top-to-bottom).
  * Real, selectable text rendered with a standard font (Liberation Sans / Arial).
  * Standard section headings (Experience, Education, Skills, Languages ...).
  * No information encoded only in graphics (e.g. skill "bars") - everything is text.
  * Consistent date formatting and reverse-chronological experience.
  * Clickable hyperlinks (LinkedIn, Portfolio) preserved as real PDF link annotations.

Usage:
    python3 generate_cv.py
Outputs (repo root):
    Jan_Blaz_CV_EN.pdf
    Jan_Blaz_CV_PL.pdf
"""

import html
import os

from weasyprint import HTML

from cv_data import CV_EN, CV_PL

# ---------------------------------------------------------------------------
# Visual motives. Switch the whole CV look by changing ACTIVE_THEME.
# All themes stay ATS-safe: real text, single column, standard headings.
# ---------------------------------------------------------------------------
THEMES = {
    # Current motive: professional navy header band with warm amber accents.
    "navy": {
        "primary": "#123252",
        "accent": "#cf8a2e",
        "accent_dark": "#9c631a",
        "ink": "#1d2733",
        "muted": "#586170",
        "rule": "#dde1e7",
        "banner_text": "#e9eef4",
        "banner_link": "#f2c680",
    },
    # Original motive (kept for easy switching): light header, green accents.
    "green": {
        "primary": "#2f8f4e",
        "accent": "#2f8f4e",
        "accent_dark": "#1f6b39",
        "ink": "#1c1c1c",
        "muted": "#555555",
        "rule": "#d9d9d9",
        "banner_text": "#eaf5ee",
        "banner_link": "#d8f2e0",
    },
}

ACTIVE_THEME = "navy"

_T = THEMES[ACTIVE_THEME]
PRIMARY = _T["primary"]
ACCENT = _T["accent"]
ACCENT_DARK = _T["accent_dark"]
INK = _T["ink"]
MUTED = _T["muted"]
RULE = _T["rule"]
BANNER_TEXT = _T["banner_text"]
BANNER_LINK = _T["banner_link"]

CSS = f"""
@page {{
    size: A4;
    margin: 8mm 13mm 8mm 13mm;
}}
* {{ box-sizing: border-box; }}
html {{ -weasy-hyphens: none; }}
body {{
    font-family: "Liberation Sans", "Arial", "Noto Sans", sans-serif;
    color: {INK};
    font-size: 9pt;
    line-height: 1.2;
    margin: 0;
}}
a {{ color: {ACCENT_DARK}; text-decoration: none; border-bottom: 1px solid {ACCENT}; }}

/* ---------- Header banner (full-bleed) ---------- */
.banner {{
    background: {PRIMARY};
    margin: -8mm -13mm 4px -13mm;
    padding: 4mm 13mm 1.5mm 13mm;
}}
.name {{
    font-size: 23pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #ffffff;
    margin: 0;
}}
.headline {{
    font-size: 10pt;
    font-weight: 700;
    color: {ACCENT};
    margin: 2px 0 5px 0;
    letter-spacing: 0.3px;
}}
.contact {{
    font-size: 8.5pt;
    color: {BANNER_TEXT};
    line-height: 1.4;
}}
.contact .sep {{ color: rgba(255,255,255,0.35); padding: 0 5px; }}
.contact a {{ color: {BANNER_LINK}; border-bottom: 1px solid {BANNER_LINK}; }}

/* ---------- Sections ---------- */
.section {{ margin-top: 3px; }}
.section h2 {{
    font-size: 10.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.1px;
    color: {PRIMARY};
    margin: 0 0 4px 0;
    padding-bottom: 2px;
    border-bottom: 1.5px solid {ACCENT};
}}
.section h2::before {{
    content: "";
    display: inline-block;
    width: 7px;
    height: 7px;
    background: {ACCENT};
    margin-right: 7px;
    vertical-align: 12%;
}}
p.summary {{ margin: 0; text-align: justify; }}

/* ---------- Entries (experience / education) ---------- */
.entry {{ margin-bottom: 3px; }}
.entry:last-child {{ margin-bottom: 0; }}
.entry-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 12px;
}}
.entry-title {{ font-weight: 700; font-size: 10pt; color: {INK}; }}
.entry-org {{ font-size: 9pt; color: {PRIMARY}; font-weight: 700; }}
.entry-dates {{
    font-size: 8.5pt;
    color: {MUTED};
    white-space: nowrap;
    font-weight: 600;
}}
.entry-sub {{ font-size: 9pt; color: {MUTED}; margin: 1px 0 2px 0; }}
ul.bullets {{ margin: 2px 0 0 0; padding-left: 15px; }}
ul.bullets li {{ margin: 0; padding-left: 2px; }}
ul.bullets li::marker {{ color: {ACCENT}; }}

/* ---------- Skills / languages grids ---------- */
.grid {{ display: table; width: 100%; border-collapse: collapse; }}
.grid-row {{ display: table-row; }}
.grid-key, .grid-val {{ display: table-cell; padding: 1px 0; vertical-align: top; }}
.grid-key {{
    font-weight: 700;
    color: {INK};
    width: 33%;
    padding-right: 10px;
}}
.grid-val {{ color: {MUTED}; }}
.interests {{ margin: 0; color: {MUTED}; }}
.inline-list {{ margin: 0; color: {MUTED}; }}
.inline-list b {{ color: {INK}; }}
.footer {{
    margin: 3px 0 0 0;
    padding-top: 2px;
    border-top: 1px solid {RULE};
    font-size: 6.5pt;
    color: {MUTED};
    font-style: italic;
    line-height: 1.2;
}}
"""


def esc(text):
    return html.escape(str(text))


def render_header(cv):
    c = cv["contact"]
    lbl = cv["labels"]
    links = (
        f'<a href="{esc(c["linkedin_url"])}">{esc(lbl["linkedin"])}</a>'
        f'<span class="sep">|</span>'
        f'<a href="{esc(c["portfolio_url"])}">{esc(lbl["portfolio"])}</a>'
        f'<span class="sep">|</span>'
        f'<a href="{esc(c["github_url"])}">{esc(lbl["github"])}</a>'
    )
    contact_line = (
        f'{esc(cv["location"])}<span class="sep">|</span>'
        f'{esc(c["phone"])}<span class="sep">|</span>'
        f'<a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a>'
        f'<span class="sep">|</span>{links}'
    )
    return (
        f'<div class="banner">'
        f'<h1 class="name">{esc(c["name"])}</h1>'
        f'<div class="headline">{esc(cv["headline"])}</div>'
        f'<div class="contact">{contact_line}</div>'
        f'</div>'
    )


def render_section(title, inner):
    return f'<div class="section"><h2>{esc(title)}</h2>{inner}</div>'


def render_experience(cv):
    rows = []
    for e in cv["experience"]:
        bullets = "".join(f"<li>{esc(b)}</li>" for b in e["bullets"])
        org_bits = [b for b in [e.get("org"), e.get("location")] if b]
        sub = " — ".join(org_bits)
        rows.append(
            f'<div class="entry">'
            f'<div class="entry-head">'
            f'<span class="entry-title">{esc(e["role"])}</span>'
            f'<span class="entry-dates">{esc(e["dates"])}</span>'
            f'</div>'
            f'<div class="entry-sub"><span class="entry-org">{esc(e.get("org",""))}</span>'
            f'{(" — " + esc(e.get("location",""))) if e.get("location") else ""}</div>'
            f'<ul class="bullets">{bullets}</ul>'
            f'</div>'
        )
    return render_section(cv["labels"]["experience"], "".join(rows))


def render_education(cv):
    rows = []
    for e in cv["education"]:
        org_line = ""
        if e.get("org"):
            org_line = (
                f'<div class="entry-sub"><span class="entry-org">{esc(e["org"])}</span>'
                f'{(" — " + esc(e.get("location",""))) if e.get("location") else ""}</div>'
            )
        rows.append(
            f'<div class="entry">'
            f'<div class="entry-head">'
            f'<span class="entry-title">{esc(e["degree"])}</span>'
            f'<span class="entry-dates">{esc(e["dates"])}</span>'
            f'</div>'
            f'{org_line}'
            f'</div>'
        )
    return render_section(cv["labels"]["education"], "".join(rows))


def render_skills(cv):
    rows = "".join(
        f'<div class="grid-row"><div class="grid-key">{esc(s["group"])}</div>'
        f'<div class="grid-val">{esc(s["items"])}</div></div>'
        for s in cv["skills"]
    )
    return render_section(cv["labels"]["skills"], f'<div class="grid">{rows}</div>')


def render_languages(cv):
    parts = " · ".join(
        f'<b>{esc(l["name"])}</b> — {esc(l["level"])}' for l in cv["languages"]
    )
    return render_section(cv["labels"]["languages"], f'<p class="inline-list">{parts}</p>')


def render_certifications(cv):
    items = " · ".join(esc(c) for c in cv["certifications"])
    return render_section(cv["labels"]["certifications"], f'<p class="inline-list">{items}</p>')


def render_interests(cv):
    return render_section(
        cv["labels"]["interests"], f'<p class="interests">{esc(cv["interests"])}</p>'
    )


def build_html(cv):
    body = (
        render_header(cv)
        + render_section(cv["labels"]["summary"], f'<p class="summary">{esc(cv["summary"])}</p>')
        + render_experience(cv)
        + render_education(cv)
        + render_skills(cv)
        + render_languages(cv)
        + render_certifications(cv)
        + render_interests(cv)
    )
    if cv.get("footer"):
        body += f'<p class="footer">{esc(cv["footer"])}</p>'
    return (
        f'<!DOCTYPE html><html lang="{cv["lang"]}"><head>'
        f'<meta charset="utf-8"><style>{CSS}</style></head>'
        f'<body>{body}</body></html>'
    )


def main():
    out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    targets = [
        (CV_EN, os.path.join(out_dir, "Jan_Blaz_CV_EN.pdf")),
        (CV_PL, os.path.join(out_dir, "Jan_Blaz_CV_PL.pdf")),
    ]
    for cv, path in targets:
        HTML(string=build_html(cv)).write_pdf(path)
        print("Wrote", path)


if __name__ == "__main__":
    main()
