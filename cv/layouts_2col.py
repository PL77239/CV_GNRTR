# -*- coding: utf-8 -*-
"""Two-column CV layout variants (human-facing).

Layouts:
  light  — existing light sidebar + divider (built in generate_cv.py)
  panel  — dark charcoal sidebar, soft-blue accents (closest to uploaded template)
  slate  — slate-blue sidebar, cooler accents (second iteration)

No photo: contact sits in the dark sidebar Profile block instead.
"""

import html

from weasyprint import HTML


def esc(text):
    return html.escape(str(text))


def _css_dark_sidebar(sidebar_bg, accent_bar, accent_text, link_color):
    ink = "#1e2732"
    return f"""
@page {{
    size: A4;
    margin: 0;
}}
* {{ box-sizing: border-box; }}
html {{ -weasy-hyphens: none; }}
body {{
    font-family: "Liberation Sans", "Arial", "Noto Sans", sans-serif;
    color: {ink};
    font-size: 9.5pt;
    line-height: 1.32;
    margin: 0;
}}
a {{ color: {link_color}; text-decoration: none; border-bottom: 1px solid {link_color}; }}

.page {{
    display: table;
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    min-height: 297mm;
}}
.sidebar, .main {{
    display: table-cell;
    vertical-align: top;
}}
.sidebar {{
    width: 33%;
    background: {sidebar_bg};
    color: #f2f2f2;
    padding: 11mm 7mm 10mm 9mm;
}}
.main {{
    width: 67%;
    background: #ffffff;
    padding: 11mm 10mm 9mm 9mm;
}}

.side-name {{
    font-size: 16pt; font-weight: 700; color: #ffffff;
    margin: 0 0 2px 0; letter-spacing: 0.3px; line-height: 1.15;
}}
.side-headline {{
    font-size: 8pt; font-weight: 600; color: {accent_bar};
    margin: 0 0 12px 0; line-height: 1.35;
}}

.side-section {{ margin: 0 0 12px 0; }}
.side-section:last-child {{ margin-bottom: 0; }}
.side-h {{
    display: inline-block;
    font-size: 8.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px;
    color: {accent_text}; background: {accent_bar};
    margin: 0 0 7px 0; padding: 3px 8px; border-radius: 3px;
}}
.profile-row {{
    font-size: 8.5pt; color: #e6e6e6; margin: 0 0 5px 0; line-height: 1.3;
}}
.profile-row .k {{
    display: block; font-size: 7.5pt; font-weight: 700;
    color: {accent_bar}; text-transform: uppercase; letter-spacing: 0.5px;
    margin-bottom: 1px;
}}
.profile-row a {{ color: {accent_bar}; border-bottom-color: {accent_bar}; }}

.side-skill {{ margin: 0 0 6px 0; }}
.side-skill:last-child {{ margin-bottom: 0; }}
.side-skill .lab {{
    font-weight: 700; font-size: 8.5pt; color: #ffffff; margin: 0 0 1px 0;
}}
.side-skill .val {{
    font-size: 8pt; color: #d0d0d0; margin: 0; line-height: 1.3;
}}
.side-lang {{
    font-size: 8.5pt; color: #e0e0e0; margin: 0 0 3px 0;
}}
.side-lang b {{ color: #ffffff; }}
.side-interests {{
    font-size: 8.5pt; color: #d5d5d5; margin: 0; line-height: 1.35;
}}

.main-name {{
    font-size: 24pt; font-weight: 700; color: {sidebar_bg};
    margin: 0; letter-spacing: 0.2px; line-height: 1.1;
}}
.main-headline {{
    font-size: 9pt; font-weight: 700; color: #666666;
    margin: 3px 0 10px 0; letter-spacing: 0.1px;
}}
.about-label {{
    display: inline-block;
    font-size: 8.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;
    color: #ffffff; background: {sidebar_bg};
    margin: 0; padding: 3px 9px; border-radius: 3px 3px 0 0;
}}
.about-box {{
    background: {accent_bar};
    color: {sidebar_bg};
    padding: 8px 10px;
    margin: 0 0 12px 0;
    border-radius: 0 0 4px 4px;
    font-size: 9pt; line-height: 1.35;
}}
.about-box p {{ margin: 0; }}

.main-section {{ margin: 0 0 11px 0; }}
.main-section:last-child {{ margin-bottom: 0; }}
.main-h {{
    font-size: 9.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
    color: #ffffff; background: {sidebar_bg};
    margin: 0 0 7px 0; padding: 4px 8px;
}}

.entry {{ margin-bottom: 8px; }}
.entry:last-child {{ margin-bottom: 0; }}
.entry-dates {{
    font-size: 8.5pt; color: #777777; font-style: italic;
    font-weight: 600; margin: 0 0 1px 0;
}}
.entry-title {{
    font-weight: 700; font-size: 10pt; color: {ink}; margin: 0;
}}
.entry-org {{
    font-size: 9pt; color: #555555; font-weight: 600; margin: 0 0 2px 0;
}}
.entry.compact .entry-title {{ font-size: 9pt; }}
.entry.compact {{ margin-bottom: 4px; }}
ul.bullets {{ margin: 2px 0 0 0; padding-left: 14px; }}
ul.bullets li {{ margin: 1px 0; font-size: 9pt; color: {ink}; }}
ul.bullets li::marker {{ color: {sidebar_bg}; }}

.footer {{
    margin: 8px 0 0 0;
    padding-top: 4px;
    border-top: 1px solid #dddddd;
    font-size: 6pt;
    color: #888888;
    font-style: italic;
    line-height: 1.2;
}}
"""


CSS_PANEL = _css_dark_sidebar(
    sidebar_bg="#2b2b2b",
    accent_bar="#b8c9d9",
    accent_text="#2b2b2b",
    link_color="#b8c9d9",
)

CSS_SLATE = _css_dark_sidebar(
    sidebar_bg="#1e3a4c",
    accent_bar="#9ec5d8",
    accent_text="#1e3a4c",
    link_color="#9ec5d8",
)


def _render_experience(cv):
    rows = []
    for e in cv["experience"]:
        if e.get("compact"):
            org = esc(e.get("org", ""))
            loc = f' — {esc(e["location"])}' if e.get("location") else ""
            rows.append(
                f'<div class="entry compact">'
                f'<div class="entry-dates">{esc(e["dates"])}</div>'
                f'<div class="entry-title">{esc(e["role"])} – {org}{loc}</div>'
                f'</div>'
            )
            continue
        bullets = "".join(f"<li>{esc(b)}</li>" for b in e["bullets"])
        rows.append(
            f'<div class="entry">'
            f'<div class="entry-dates">{esc(e["dates"])}</div>'
            f'<div class="entry-title">{esc(e["role"])}</div>'
            f'<div class="entry-org">{esc(e.get("org",""))}'
            f'{(" — " + esc(e["location"])) if e.get("location") else ""}</div>'
            f'<ul class="bullets">{bullets}</ul>'
            f'</div>'
        )
    return "".join(rows)


def _render_education(cv):
    rows = []
    for e in cv["education"]:
        rows.append(
            f'<div class="entry">'
            f'<div class="entry-dates">{esc(e["dates"])}</div>'
            f'<div class="entry-title">{esc(e["degree"])}</div>'
            f'<div class="entry-org">{esc(e.get("org",""))}'
            f'{(" — " + esc(e["location"])) if e.get("location") else ""}</div>'
            f'</div>'
        )
    return "".join(rows)


def build_html_dark(cv, css):
    c = cv["contact"]
    lbl = cv["labels"]

    profile = (
        f'<div class="side-section">'
        f'<div class="side-h">{esc(lbl["profile"])}</div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["location_label"])}</span>{esc(cv["location"])}</div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["phone_label"])}</span>{esc(c["phone"])}</div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["email_label"])}</span>'
        f'<a href="mailto:{esc(c["email"])}">{esc(c["email"])}</a></div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["linkedin"])}</span>'
        f'<a href="{esc(c["linkedin_url"])}">{esc(lbl["linkedin"])}</a></div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["portfolio"])}</span>'
        f'<a href="{esc(c["portfolio_url"])}">{esc(lbl["portfolio"])}</a></div>'
        f'<div class="profile-row"><span class="k">{esc(lbl["github"])}</span>'
        f'<a href="{esc(c["github_url"])}">{esc(lbl["github"])}</a></div>'
        f'</div>'
    )

    skills = (
        f'<div class="side-section"><div class="side-h">{esc(lbl["skills"])}</div>'
        + "".join(
            f'<div class="side-skill"><div class="lab">{esc(s["group"])}</div>'
            f'<p class="val">{esc(s["items"])}</p></div>'
            for s in cv["skills"]
        )
        + "</div>"
    )

    languages = (
        f'<div class="side-section"><div class="side-h">{esc(lbl["languages"])}</div>'
        + "".join(
            f'<p class="side-lang"><b>{esc(l["name"])}</b> — {esc(l["level"])}</p>'
            for l in cv["languages"]
        )
        + "</div>"
    )

    interests = ""
    if cv.get("interests"):
        interests = (
            f'<div class="side-section"><div class="side-h">{esc(lbl["interests"])}</div>'
            f'<p class="side-interests">{esc(cv["interests"])}</p></div>'
        )

    side_headline = cv["headline"].split("•")[0].strip()

    sidebar = (
        f'<div class="side-headline" style="margin-top:2px;margin-bottom:14px;font-size:9pt;">'
        f'{esc(side_headline)}</div>'
        f'{profile}{skills}{languages}{interests}'
    )

    main = (
        f'<div class="main-name">{esc(c["name"])}</div>'
        f'<div class="main-headline">{esc(cv["headline"])}</div>'
        f'<div class="about-label">{esc(lbl["about"])}</div>'
        f'<div class="about-box"><p>{esc(cv["summary"])}</p></div>'
        f'<div class="main-section"><div class="main-h">{esc(lbl["experience"])}</div>'
        f'{_render_experience(cv)}</div>'
        f'<div class="main-section"><div class="main-h">{esc(lbl["education"])}</div>'
        f'{_render_education(cv)}</div>'
    )
    if cv.get("footer"):
        main += f'<p class="footer">{esc(cv["footer"])}</p>'

    body = (
        f'<div class="page">'
        f'<div class="sidebar">{sidebar}</div>'
        f'<div class="main">{main}</div>'
        f'</div>'
    )
    return (
        f'<!DOCTYPE html><html lang="{cv["lang"]}"><head>'
        f'<meta charset="utf-8"><style>{css}</style></head>'
        f'<body>{body}</body></html>'
    )


def build_html_panel(cv):
    return build_html_dark(cv, CSS_PANEL)


def build_html_slate(cv):
    return build_html_dark(cv, CSS_SLATE)


def write_pdf(cv, path, builder):
    HTML(string=builder(cv)).write_pdf(path)
