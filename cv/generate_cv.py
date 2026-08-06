# -*- coding: utf-8 -*-
"""Generate ATS-friendly PDF CVs (PL + EN) for Jan Blaz.

Aligned to 2026/2027 standards across Workday, Greenhouse, Lever, LinkedIn
and Indeed (single-column, skills-first hybrid, standard headings, body
10–11pt, generous white space for a 6–7s recruiter F-pattern scan).

Usage:
    python3 generate_cv.py
Outputs (repo root):
    Jan_Blaz_CV_EN.pdf / Jan_Blaz_CV_PL.pdf           — single-column (ATS)
    Jan_Blaz_CV_EN_2col.pdf / Jan_Blaz_CV_PL_2col.pdf — two-column (human-facing)
"""

import html
import os

from weasyprint import HTML

from cv_data import CV_EN, CV_PL

# ---------------------------------------------------------------------------
# Visual motives. Switch with ACTIVE_THEME.
# All stay ATS-safe: real text, single column, standard headings.
# ---------------------------------------------------------------------------
THEMES = {
    # Active: solid page-wide section bars for fast human scanning + breathing room.
    "scan": {
        "style": "scan",
        "primary": "#1a3350",
        "accent": "#1a3350",
        "accent_dark": "#245891",
        "ink": "#1e2732",
        "muted": "#5a6570",
        "rule": "#d0d5db",
        "banner_text": "#ffffff",
        "banner_link": "#cfe0f5",
    },
    "modern": {
        "style": "modern",
        "primary": "#16324e",
        "accent": "#2f6db3",
        "accent_dark": "#245891",
        "ink": "#1e2732",
        "muted": "#586170",
        "rule": "#c9ced6",
        "banner_text": "#ffffff",
        "banner_link": "#ffffff",
    },
    "editorial": {
        "style": "editorial",
        "primary": "#5a1f27",
        "accent": "#9b2d39",
        "accent_dark": "#7a2531",
        "ink": "#222222",
        "muted": "#5b5b5b",
        "rule": "#e2d9da",
        "banner_text": "#ffffff",
        "banner_link": "#ffffff",
    },
    "navy": {
        "style": "band",
        "primary": "#123252",
        "accent": "#cf8a2e",
        "accent_dark": "#9c631a",
        "ink": "#1d2733",
        "muted": "#586170",
        "rule": "#dde1e7",
        "banner_text": "#e9eef4",
        "banner_link": "#f2c680",
    },
    "green": {
        "style": "classic",
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

ACTIVE_THEME = "scan"

_T = THEMES[ACTIVE_THEME]
STYLE = _T["style"]
PRIMARY = _T["primary"]
ACCENT = _T["accent"]
ACCENT_DARK = _T["accent_dark"]
INK = _T["ink"]
MUTED = _T["muted"]
RULE = _T["rule"]
BANNER_TEXT = _T["banner_text"]
BANNER_LINK = _T["banner_link"]
ORG_COLOR = PRIMARY if STYLE in ("band", "scan") else ACCENT


def _header_css():
    if STYLE == "band":
        return f"""
.header {{
    background: {PRIMARY};
    margin: -12mm -14mm 10px -14mm;
    padding: 5mm 14mm 3mm 14mm;
}}
.name {{ font-size: 22pt; font-weight: 700; letter-spacing: 0.4px; color: #ffffff; margin: 0; }}
.headline {{ font-size: 10pt; font-weight: 700; color: {ACCENT}; margin: 3px 0 6px 0; letter-spacing: 0.2px; }}
.contact {{ font-size: 9pt; color: {BANNER_TEXT}; line-height: 1.45; }}
.contact .sep {{ color: rgba(255,255,255,0.35); padding: 0 6px; }}
.contact a {{ color: {BANNER_LINK}; border-bottom: 1px solid {BANNER_LINK}; }}
"""
    if STYLE == "scan":
        return f"""
.header {{ margin: 0 0 8px 0; padding-bottom: 6px; border-bottom: 3px solid {PRIMARY}; }}
.name {{ font-size: 22pt; font-weight: 700; letter-spacing: 0.3px; color: {PRIMARY}; margin: 0; }}
.headline {{ font-size: 9.5pt; font-weight: 700; color: {MUTED}; margin: 3px 0 5px 0; letter-spacing: 0.15px; }}
.contact {{ font-size: 9pt; color: {MUTED}; line-height: 1.4; }}
.contact .sep {{ color: {RULE}; padding: 0 5px; }}
"""
    name_tt = "text-transform: uppercase; letter-spacing: 2px;" if STYLE == "editorial" else "letter-spacing: 0.4px;"
    if STYLE == "modern":
        border = f"border-bottom: 2px solid {PRIMARY};"
        name_color = PRIMARY
    elif STYLE == "editorial":
        border = f"border-bottom: 2px solid {ACCENT};"
        name_color = INK
    else:
        border = f"border-bottom: 2.5px solid {ACCENT};"
        name_color = INK
    return f"""
.header {{ margin: 0 0 8px 0; padding-bottom: 6px; {border} }}
.name {{ font-size: 22pt; font-weight: 700; {name_tt} color: {name_color}; margin: 0; }}
.headline {{ font-size: 10pt; font-weight: 700; color: {ACCENT}; margin: 3px 0 5px 0;
    text-transform: uppercase; letter-spacing: 0.5px; }}
.contact {{ font-size: 9pt; color: {MUTED}; line-height: 1.45; }}
.contact .sep {{ color: {RULE}; padding: 0 6px; }}
"""


def _heading_css():
    if STYLE == "scan":
        # Solid page-wide bars — the strongest visual jump points for a 6–7s scan.
        return f"""
.section h2 {{
    font-size: 10.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px;
    color: #ffffff; background: {PRIMARY};
    margin: 0 0 7px 0; padding: 4px 8px;
}}
"""
    if STYLE == "modern":
        return f"""
.section h2 {{
    font-size: 12pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
    color: {PRIMARY}; margin: 0 0 6px 0; padding-bottom: 3px;
    border-bottom: 2px solid {ACCENT};
}}
"""
    if STYLE == "editorial":
        return f"""
.section h2 {{
    display: inline-block;
    font-size: 11pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1.4px;
    color: {ACCENT}; margin: 0 0 6px 0; padding-bottom: 2px;
    border-bottom: 2px solid {ACCENT};
}}
"""
    if STYLE == "band":
        return f"""
.section h2 {{
    font-size: 11pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
    color: {PRIMARY}; margin: 0 0 6px 0; padding-bottom: 3px; border-bottom: 2px solid {ACCENT};
}}
"""
    return f"""
.section h2 {{
    font-size: 11pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
    color: {ACCENT_DARK}; margin: 0 0 6px 0; padding-bottom: 3px; border-bottom: 1.5px solid {RULE};
}}
"""


CSS = f"""
@page {{
    size: A4;
    margin: 10mm 14mm 8mm 14mm;
}}
* {{ box-sizing: border-box; }}
html {{ -weasy-hyphens: none; }}
body {{
    font-family: "Liberation Sans", "Arial", "Noto Sans", sans-serif;
    color: {INK};
    font-size: 10.5pt;
    line-height: 1.32;
    margin: 0;
}}
a {{ color: {ACCENT_DARK}; text-decoration: none; border-bottom: 1px solid {ACCENT}; }}

{_header_css()}

.section {{ margin-top: 8px; page-break-inside: auto; }}
{_heading_css()}
p.summary {{ margin: 0; }}

.entry {{ margin-bottom: 6px; }}
.entry:last-child {{ margin-bottom: 0; }}
.entry-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 12px;
}}
.entry-title {{ font-weight: 700; font-size: 10.5pt; color: {INK}; }}
.entry-org {{ font-size: 10pt; color: {ORG_COLOR}; font-weight: 700; }}
.entry-dates {{
    font-size: 9.5pt;
    color: {MUTED};
    white-space: nowrap;
    font-weight: 600;
}}
.entry-sub {{ font-size: 10pt; color: {MUTED}; margin: 1px 0 3px 0; }}
.entry-loc {{ font-size: 10pt; color: {MUTED}; font-weight: 400; }}
.entry.compact {{ margin-bottom: 4px; }}
ul.bullets {{ margin: 3px 0 0 0; padding-left: 16px; }}
ul.bullets li {{ margin: 2px 0; padding-left: 2px; }}
ul.bullets li::marker {{ color: {PRIMARY}; }}

.grid {{ display: table; width: 100%; border-collapse: collapse; }}
.grid-row {{ display: table-row; }}
.grid-key, .grid-val {{ display: table-cell; padding: 2px 0; vertical-align: top; }}
.grid-key {{
    font-weight: 700;
    color: {INK};
    width: 28%;
    padding-right: 10px;
}}
.grid-val {{ color: {MUTED}; }}
.interests {{ margin: 0; color: {MUTED}; }}
.inline-list {{ margin: 0; color: {MUTED}; }}
.inline-list b {{ color: {INK}; }}
.footer {{
    margin: 4px 0 0 0;
    padding-top: 2px;
    border-top: 1px solid {RULE};
    font-size: 6pt;
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
        f'<div class="header">'
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
        loc = f' <span class="entry-loc">— {esc(e["location"])}</span>' if e.get("location") else ""
        if e.get("compact"):
            rows.append(
                f'<div class="entry compact">'
                f'<div class="entry-head">'
                f'<span><span class="entry-title">{esc(e["role"])}</span>'
                f' <span class="entry-org">— {esc(e.get("org",""))}</span>{loc}</span>'
                f'<span class="entry-dates">{esc(e["dates"])}</span>'
                f'</div>'
                f'</div>'
            )
            continue
        bullets = "".join(f"<li>{esc(b)}</li>" for b in e["bullets"])
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


def render_interests(cv):
    if not cv.get("interests"):
        return ""
    return render_section(
        cv["labels"]["interests"], f'<p class="interests">{esc(cv["interests"])}</p>'
    )


def build_html(cv):
    # Skills-first hybrid (2026 recommended for cross-domain / keyword-dense profiles):
    # Summary → Skills → Experience → Education → Languages.
    # Interests live in the 2-column human-facing variant (more room in the sidebar).
    body = (
        render_header(cv)
        + render_section(cv["labels"]["summary"], f'<p class="summary">{esc(cv["summary"])}</p>')
        + render_skills(cv)
        + render_experience(cv)
        + render_education(cv)
        + render_languages(cv)
    )
    if cv.get("footer"):
        body += f'<p class="footer">{esc(cv["footer"])}</p>'
    return (
        f'<!DOCTYPE html><html lang="{cv["lang"]}"><head>'
        f'<meta charset="utf-8"><style>{CSS}</style></head>'
        f'<body>{body}</body></html>'
    )


# ---------------------------------------------------------------------------
# Two-column (human-facing) layout.
# Full-width header + left sidebar (skills/languages/interests) | main column
# (summary/experience/education). Prefer for networking / email / interview;
# keep the single-column PDFs for ATS uploads.
# ---------------------------------------------------------------------------
CSS_2COL = f"""
@page {{
    size: A4;
    margin: 10mm 12mm 9mm 12mm;
}}
* {{ box-sizing: border-box; }}
html {{ -weasy-hyphens: none; }}
body {{
    font-family: "Liberation Sans", "Arial", "Noto Sans", sans-serif;
    color: {INK};
    font-size: 10pt;
    line-height: 1.32;
    margin: 0;
}}
a {{ color: {ACCENT_DARK}; text-decoration: none; border-bottom: 1px solid {ACCENT}; }}

.header {{
    margin: 0 0 10px 0;
    padding-bottom: 7px;
    border-bottom: 3px solid {PRIMARY};
}}
.name {{
    font-size: 22pt; font-weight: 700; letter-spacing: 0.3px;
    color: {PRIMARY}; margin: 0;
}}
.headline {{
    font-size: 9.5pt; font-weight: 700; color: {MUTED};
    margin: 3px 0 5px 0; letter-spacing: 0.15px;
}}
.contact {{ font-size: 9pt; color: {MUTED}; line-height: 1.4; }}
.contact .sep {{ color: {RULE}; padding: 0 5px; }}

.layout {{
    display: table;
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
}}
.sidebar, .main {{
    display: table-cell;
    vertical-align: top;
}}
.sidebar {{
    width: 32%;
    padding-right: 12px;
    border-right: 2px solid {PRIMARY};
}}
.main {{
    width: 68%;
    padding-left: 14px;
}}

.section {{ margin-top: 0; margin-bottom: 11px; }}
.section:last-child {{ margin-bottom: 0; }}
.section h2 {{
    font-size: 9.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
    color: #ffffff; background: {PRIMARY};
    margin: 0 0 6px 0; padding: 3px 7px;
}}

p.summary {{ margin: 0; }}

.skill-block {{ margin-bottom: 7px; }}
.skill-block:last-child {{ margin-bottom: 0; }}
.skill-label {{
    font-weight: 700; font-size: 9pt; color: {INK};
    margin: 0 0 1px 0;
}}
.skill-items {{
    font-size: 8.5pt; color: {MUTED}; margin: 0; line-height: 1.3;
}}

.lang-row {{
    font-size: 9pt; color: {MUTED}; margin: 0 0 3px 0;
}}
.lang-row b {{ color: {INK}; }}

.entry {{ margin-bottom: 8px; }}
.entry:last-child {{ margin-bottom: 0; }}
.entry-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 8px;
}}
.entry-title {{ font-weight: 700; font-size: 10pt; color: {INK}; }}
.entry-org {{ font-size: 9pt; color: {PRIMARY}; font-weight: 700; }}
.entry-dates {{
    font-size: 8.5pt; color: {MUTED}; white-space: nowrap; font-weight: 600;
}}
.entry-sub {{ font-size: 9pt; color: {MUTED}; margin: 1px 0 2px 0; }}
.entry-loc {{ font-size: 9pt; color: {MUTED}; font-weight: 400; }}
.entry.compact {{ margin-bottom: 4px; }}
ul.bullets {{ margin: 2px 0 0 0; padding-left: 14px; }}
ul.bullets li {{ margin: 1px 0; padding-left: 1px; font-size: 9.5pt; }}
ul.bullets li::marker {{ color: {PRIMARY}; }}

.interests {{ margin: 0; color: {MUTED}; font-size: 9pt; }}
.footer {{
    margin: 8px 0 0 0;
    padding-top: 4px;
    border-top: 1px solid {RULE};
    font-size: 6.5pt;
    color: {MUTED};
    font-style: italic;
    line-height: 1.25;
}}
"""


def render_skills_sidebar(cv):
    blocks = "".join(
        f'<div class="skill-block">'
        f'<div class="skill-label">{esc(s["group"])}</div>'
        f'<p class="skill-items">{esc(s["items"])}</p>'
        f'</div>'
        for s in cv["skills"]
    )
    return render_section(cv["labels"]["skills"], blocks)


def render_languages_sidebar(cv):
    rows = "".join(
        f'<p class="lang-row"><b>{esc(l["name"])}</b> — {esc(l["level"])}</p>'
        for l in cv["languages"]
    )
    return render_section(cv["labels"]["languages"], rows)


def build_html_2col(cv):
    sidebar = (
        render_skills_sidebar(cv)
        + render_languages_sidebar(cv)
        + render_interests(cv)
    )
    main = (
        render_section(cv["labels"]["summary"], f'<p class="summary">{esc(cv["summary"])}</p>')
        + render_experience(cv)
        + render_education(cv)
    )
    body = (
        render_header(cv)
        + f'<div class="layout">'
        f'<div class="sidebar">{sidebar}</div>'
        f'<div class="main">{main}</div>'
        f'</div>'
    )
    if cv.get("footer"):
        body += f'<p class="footer">{esc(cv["footer"])}</p>'
    return (
        f'<!DOCTYPE html><html lang="{cv["lang"]}"><head>'
        f'<meta charset="utf-8"><style>{CSS_2COL}</style></head>'
        f'<body>{body}</body></html>'
    )


def main():
    out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    targets = [
        (CV_EN, "Jan_Blaz_CV_EN.pdf", build_html),
        (CV_PL, "Jan_Blaz_CV_PL.pdf", build_html),
        (CV_EN, "Jan_Blaz_CV_EN_2col.pdf", build_html_2col),
        (CV_PL, "Jan_Blaz_CV_PL_2col.pdf", build_html_2col),
    ]
    for cv, filename, builder in targets:
        path = os.path.join(out_dir, filename)
        HTML(string=builder(cv)).write_pdf(path)
        print("Wrote", path)


if __name__ == "__main__":
    main()
