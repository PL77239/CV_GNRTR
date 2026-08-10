# -*- coding: utf-8 -*-
"""Content for Jan Blaz's CV in Polish (PL) and English (EN).

Kept as structured data so both language versions share the exact same,
ATS-friendly layout and only the text differs.

Primary focus: 3D modelling / product design, with Front-end Development, IT
and International Marketing as complementary tracks.
"""

# Shared contact details (identical in both versions).
CONTACT = {
    "name": "Jan Błaż",
    "phone": "+48 697 655 050",
    "email": "jmtentertainment777@gmail.com",
    # Links preserved / derived from the original CV; all stay clickable.
    "linkedin_url": "http://www.linkedin.com/in/jan-b%C5%82a%C5%BC-39b0523a5",
    "portfolio_url": "https://guapdad8k.github.io/WEB-PORTFOLIO/",
    "github_url": "https://github.com/guapdad8k",
}

CV_EN = {
    "lang": "en",
    "contact": CONTACT,
    "location": "Warsaw, Poland",
    "headline": (
        "3D Modeler & Product Designer  •  Front-end Developer  •  IT  •  "
        "International Marketing (events, trade fairs)"
    ),
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
        "github": "GitHub",
        "summary": "Professional Summary",
        "about": "About me",
        "profile": "Profile",
        "location_label": "Location",
        "phone_label": "Mobile",
        "email_label": "Email",
        "experience": "Professional Experience",
        "education": "Education",
        "skills": "Skills",
        "languages": "Languages",
        "certifications": "Certifications",
        "interests": "Interests",
        "present": "Present",
    },
    "summary": (
        "3D modeler and product designer with commercial work in game-ready assets, "
        "functional 3D-printed automotive parts and music production. Strong toolset across "
        "Blender, 3ds Max, Maya, SolidWorks, Fusion 360 and Rhino 3D, plus a Front-end "
        "Development base (web, IT, cybersecurity) and years of international B2B marketing — "
        "brand launches, events and trade fairs. Open to roles in 3D/product design, IT or "
        "international marketing, including internships."
    ),
    "experience": [
        {
            "role": "3D Designer (Freelance)",
            "org": "Self-employed",
            "location": "Remote",
            "dates": "2023 – Present",
            "bullets": [
                "Produced ~10 game-ready car models for racing titles such as Assetto Corsa.",
                "Designed and 3D-printed 10+ functional automotive parts; one is being reproduced in glass fibre for production.",
                "Deliver commercial CAD and 3D work end-to-end, from concept to final model or print.",
            ],
        },
        {
            "role": "Sales & Marketing Assistant",
            "org": "Independent Traders & Consultants",
            "location": "Warsaw, Poland",
            "dates": "2023 – Mar 2026",
            "bullets": [
                "Introduced 20+ foreign suppliers and brands to the Polish and CEE markets.",
                "Organised 4 industry trade fairs in Poland and coordinated international B2B events and meetings.",
                "Conducted market research to identify new opportunities and partners.",
            ],
        },
        {
            "role": "Junior Marketing Assistant",
            "org": "Biotop-Service Sp. z o.o.",
            "location": "Warsaw, Poland",
            "dates": "2020 – 2023",
            "bullets": [
                "Maintained marketing and customer databases; acquired new clients and partners.",
                "Provided day-to-day IT support across the team.",
            ],
        },
        {
            "role": "Sales Specialist (Cold Lead)",
            "org": "SentiOne",
            "location": "Poland",
            "dates": "2019 – 2020",
            "compact": True,
            "bullets": [],
        },
        {
            "role": "Work & Travel Programme",
            "org": "Tokyo, Japan",
            "location": "",
            "dates": "2019",
            "compact": True,
            "bullets": [],
        },
        {
            "role": "Door-to-Door Sales Representative",
            "org": "Energy Match",
            "location": "Poland",
            "dates": "2018 – 2019",
            "compact": True,
            "bullets": [],
        },
    ],
    "education": [
        {
            "degree": "BSc in Front-end Development (in progress)",
            "org": "Vistula Academy of Finance and Business",
            "location": "Warsaw, Poland",
            "dates": "2025 – Present",
            "note": "",
        },
        {
            "degree": "Automotive Engineering",
            "org": "Politecnico di Torino",
            "location": "Turin, Italy",
            "dates": "2021 – 2023",
            "note": "",
        },
    ],
    "skills": [
        {"group": "3D Modelling & CAD", "items": "Blender, 3ds Max, Maya, SolidWorks, Fusion 360, Rhino 3D; 3D printing, product design, game assets; Photoshop"},
        {"group": "Front-end & Web", "items": "HTML, CSS, JavaScript, React, Node.js, Git"},
        {"group": "Programming & Data", "items": "Python, C#, SQL (SSMS)"},
        {"group": "Audio & Sound Design", "items": "Logic Pro, FL Studio, Ableton; sound design, mixing"},
        {"group": "Office & Productivity", "items": "Microsoft Office (Word, Excel, PowerPoint)"},
    ],
    "languages": [
        {"name": "Polish", "level": "Native"},
        {"name": "English", "level": "Advanced (C1, TOEFL certified)"},
        {"name": "Spanish", "level": "Advanced (C1)"},
        {"name": "Basics", "level": "Japanese (A2), French (A2), Italian (A1)"},
    ],
    "certifications": [
        "TOEFL English Certificate",
    ],
    # Dropped from the main layout to free white space for a scannable one-pager;
    # kept in data in case we re-enable later.
    "interests": "Travel · Automotive engineering & motorsport · Basketball · 3D printing & product design",
    "footer": "",
}

CV_PL = {
    "lang": "pl",
    "contact": CONTACT,
    "location": "Warszawa, Polska",
    "headline": (
        "Modelarz 3D i projektant produktu  •  Front-end Developer  •  IT  •  "
        "Marketing międzynarodowy (eventy, targi)"
    ),
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
        "github": "GitHub",
        "summary": "Podsumowanie zawodowe",
        "about": "O mnie",
        "profile": "Profil",
        "location_label": "Adres",
        "phone_label": "Telefon",
        "email_label": "E-mail",
        "experience": "Doświadczenie zawodowe",
        "education": "Wykształcenie",
        "skills": "Umiejętności",
        "languages": "Języki",
        "certifications": "Certyfikaty",
        "interests": "Zainteresowania",
        "present": "obecnie",
    },
    "summary": (
        "Modelarz 3D i projektant produktu z komercyjnym doświadczeniem w modelach do gier, "
        "drukowanych 3D częściach samochodowych i produkcji muzycznej. Biegły w Blender, 3ds Max, "
        "Maya, SolidWorks, Fusion 360 i Rhino 3D; podstawa Front-end Development (web, IT) oraz "
        "kilkuletni międzynarodowy marketing B2B — marki, eventy i targi. Otwarty na role w "
        "3D/projekcie produktu, IT lub marketingu międzynarodowym, w tym staże."
    ),
    "experience": [
        {
            "role": "Projektant 3D (freelance)",
            "org": "Działalność własna",
            "location": "Zdalnie",
            "dates": "2023 – obecnie",
            "bullets": [
                "Ok. 10 modeli samochodów gotowych do gier wyścigowych, m.in. Assetto Corsa.",
                "Ponad 10 funkcjonalnych części samochodowych drukowanych 3D; jedna jest odtwarzana z włókna szklanego do produkcji.",
                "Realizacja komercyjnych zleceń CAD/3D od koncepcji po gotowy model lub wydruk.",
            ],
        },
        {
            "role": "Asystent ds. sprzedaży i marketingu",
            "org": "Independent Traders & Consultants",
            "location": "Warszawa, Polska",
            "dates": "2023 – marzec 2026",
            "bullets": [
                "Wprowadzenie ponad 20 zagranicznych dostawców i marek na rynek polski i CEE.",
                "Organizacja 4 targów branżowych w Polsce oraz koordynacja międzynarodowych eventów i spotkań B2B.",
                "Badania rynku w celu identyfikacji szans i partnerów.",
            ],
        },
        {
            "role": "Młodszy asystent ds. marketingu",
            "org": "Biotop-Service Sp. z o.o.",
            "location": "Warszawa, Polska",
            "dates": "2020 – 2023",
            "bullets": [
                "Utrzymanie baz marketingowych i klientów; pozyskiwanie nowych partnerów.",
                "Bieżące wsparcie IT w zespole.",
            ],
        },
        {
            "role": "Specjalista ds. sprzedaży (cold lead)",
            "org": "SentiOne",
            "location": "Polska",
            "dates": "2019 – 2020",
            "compact": True,
            "bullets": [],
        },
        {
            "role": "Program Work & Travel",
            "org": "Tokio, Japonia",
            "location": "",
            "dates": "2019",
            "compact": True,
            "bullets": [],
        },
        {
            "role": "Przedstawiciel handlowy D2D",
            "org": "Energy Match",
            "location": "Polska",
            "dates": "2018 – 2019",
            "compact": True,
            "bullets": [],
        },
    ],
    "education": [
        {
            "degree": "Licencjat, Front-end Development (w trakcie)",
            "org": "Akademia Finansów i Biznesu Vistula",
            "location": "Warszawa, Polska",
            "dates": "2025 – obecnie",
            "note": "",
        },
        {
            "degree": "Inżynieria samochodowa",
            "org": "Politecnico di Torino",
            "location": "Turyn, Włochy",
            "dates": "2021 – 2023",
            "note": "",
        },
    ],
    "skills": [
        {"group": "Modelowanie 3D i CAD", "items": "Blender, 3ds Max, Maya, SolidWorks, Fusion 360, Rhino 3D; druk 3D, projektowanie produktu, obiekty do gier; Photoshop"},
        {"group": "Front-end i web", "items": "HTML, CSS, JavaScript, React, Node.js, Git"},
        {"group": "Programowanie i dane", "items": "Python, C#, SQL (SSMS)"},
        {"group": "Produkcja muzyczna i dźwięk", "items": "Logic Pro, FL Studio, Ableton; sound design, miksowanie"},
        {"group": "Office i produktywność", "items": "Microsoft Office (Word, Excel, PowerPoint)"},
    ],
    "languages": [
        {"name": "Polski", "level": "Ojczysty"},
        {"name": "Angielski", "level": "Zaawansowany (C1, certyfikat TOEFL)"},
        {"name": "Hiszpański", "level": "Zaawansowany (C1)"},
        {"name": "Podstawy", "level": "Japoński (A2), Francuski (A2), Włoski (A1)"},
    ],
    "certifications": [
        "Certyfikat języka angielskiego TOEFL",
    ],
    "interests": "Podróże · Inżynieria samochodowa i motorsport · Koszykówka · Druk 3D i projektowanie produktu",
    "footer": (
        "Wyrażam zgodę na przetwarzanie moich danych osobowych na potrzeby rekrutacji (RODO – UE 2016/679)."
    ),
}
