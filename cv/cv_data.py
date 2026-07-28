# -*- coding: utf-8 -*-
"""Content for Jan Blaz's CV in Polish (PL) and English (EN).

Kept as structured data so both language versions share the exact same,
ATS-friendly layout and only the text differs.

Primary focus: 3D modelling / product design, with Front-end Development & IT
as a versatile secondary track.
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
    "headline": "3D Modeler & Product Designer  •  Front-end Developer  •  IT",
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
        "github": "GitHub",
        "summary": "Professional Summary",
        "experience": "Professional Experience",
        "education": "Education",
        "skills": "Skills",
        "languages": "Languages",
        "certifications": "Certifications",
        "interests": "Interests",
        "present": "Present",
    },
    "summary": (
        "3D modeler and product designer with commercial experience building game-ready assets "
        "and functional, 3D-printed automotive parts. Skilled across Blender, 3ds Max, Maya, "
        "SolidWorks, Fusion 360 and Rhino 3D, with a solid Front-end Development base (web, IT, "
        "cybersecurity) and several years of B2B sales and marketing experience. Seeking a "
        "part-time role in 3D/product design or IT alongside full-time studies; open to internships."
    ),
    "experience": [
        {
            "role": "3D Designer (Freelance)",
            "org": "Self-employed",
            "location": "Remote",
            "dates": "2023 – Present",
            "bullets": [
                "Design and produce game-ready 3D models, including ~10 car models for racing titles such as Assetto Corsa.",
                "Design and 3D-print 10+ functional automotive parts; one is currently being reproduced in glass fibre for production.",
                "Build technical CAD models for automotive use and abstract 3D assets for games and bespoke client projects.",
                "Deliver commercial 3D work end-to-end, from concept to final model or print.",
            ],
        },
        {
            "role": "Sales & Marketing Assistant",
            "org": "Independent Traders & Consultants",
            "location": "Warsaw, Poland",
            "dates": "2023 – Mar 2026",
            "bullets": [
                "Introduced 20+ foreign suppliers and brands to the Polish and CEE markets.",
                "Organised 4 industry trade fairs in Poland and coordinated B2B meetings.",
                "Conducted market research to identify new opportunities and partners.",
                "Provided day-to-day IT support to the team.",
            ],
        },
        {
            "role": "Junior Marketing Assistant",
            "org": "Biotop-Service Sp. z o.o.",
            "location": "Warsaw, Poland",
            "dates": "2020 – 2023",
            "bullets": [
                "Monitored and maintained marketing and customer databases.",
                "Acquired new clients and business partners.",
                "Organised business meetings and trips.",
                "Provided IT support across the team.",
            ],
        },
        {
            "role": "Sales Specialist (Cold Lead)",
            "org": "SentiOne",
            "location": "Poland",
            "dates": "2019 – 2020",
            "bullets": [
                "Generated and qualified cold leads and ran outreach to prospective clients.",
            ],
        },
        {
            "role": "Work & Travel Programme",
            "org": "Tokyo, Japan",
            "location": "Japan",
            "dates": "2019",
            "bullets": [
                "Gained international work experience and cross-cultural communication skills.",
            ],
        },
        {
            "role": "Door-to-Door Sales Representative",
            "org": "Energy Match",
            "location": "Poland",
            "dates": "2018 – 2019",
            "bullets": [
                "Carried out direct door-to-door sales and client acquisition.",
            ],
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
        {
            "degree": "High School Diploma",
            "org": "Liceum nr 40 / Nauka i Wiedza Foundation",
            "location": "Warsaw, Poland",
            "dates": "2017 – 2020",
            "note": "",
        },
    ],
    "skills": [
        {"group": "3D Modelling & CAD", "items": "Blender, 3ds Max, Maya, SolidWorks, Fusion 360, Rhino 3D; 3D printing, product design, game assets; Photoshop"},
        {"group": "Front-end & Web", "items": "HTML, CSS, JavaScript, React, Node.js, Git"},
        {"group": "Programming & Data", "items": "Python, C#, SQL (SSMS)"},
        {"group": "Focus areas", "items": "3D & product development, Front-end Development, IT, Cybersecurity"},
    ],
    "languages": [
        {"name": "Polish", "level": "Native"},
        {"name": "English", "level": "Advanced (C1, TOEFL certified)"},
        {"name": "Spanish", "level": "Intermediate (B1)"},
        {"name": "Japanese", "level": "Elementary (A2)"},
        {"name": "French", "level": "Elementary (A2)"},
        {"name": "Italian", "level": "Basic (A1)"},
    ],
    "certifications": [
        "TOEFL English Certificate",
    ],
    "interests": "Travel · Automotive engineering & motorsport · Basketball · 3D printing & product design",
    "footer": "",
}

CV_PL = {
    "lang": "pl",
    "contact": CONTACT,
    "location": "Warszawa, Polska",
    "headline": "Modelarz 3D i projektant produktu  •  Front-end Developer  •  IT",
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
        "github": "GitHub",
        "summary": "Podsumowanie zawodowe",
        "experience": "Doświadczenie zawodowe",
        "education": "Wykształcenie",
        "skills": "Umiejętności",
        "languages": "Języki",
        "certifications": "Certyfikaty",
        "interests": "Zainteresowania",
        "present": "obecnie",
    },
    "summary": (
        "Modelarz 3D i projektant produktu z komercyjnym doświadczeniem w tworzeniu modeli do gier "
        "oraz funkcjonalnych, drukowanych 3D części samochodowych. Biegły w programach Blender, "
        "3ds Max, Maya, SolidWorks, Fusion 360 i Rhino 3D, z solidną podstawą Front-end Development "
        "(web, IT, cyberbezpieczeństwo) i kilkuletnim doświadczeniem w sprzedaży oraz marketingu B2B. "
        "Poszukuję pracy w niepełnym wymiarze godzin w obszarze 3D/projektowania produktu lub IT, "
        "równolegle ze studiami dziennymi; otwarty również na staże."
    ),
    "experience": [
        {
            "role": "Projektant 3D (freelance)",
            "org": "Działalność własna",
            "location": "Zdalnie",
            "dates": "2023 – obecnie",
            "bullets": [
                "Tworzenie modeli 3D gotowych do gier, w tym ok. 10 modeli samochodów do tytułów wyścigowych, takich jak Assetto Corsa.",
                "Projektowanie i druk 3D ponad 10 funkcjonalnych części samochodowych; jedna z nich jest obecnie odtwarzana z włókna szklanego do produkcji.",
                "Budowa technicznych modeli CAD do zastosowań motoryzacyjnych oraz abstrakcyjnych obiektów 3D do gier i indywidualnych projektów klientów.",
                "Realizacja komercyjnych zleceń 3D od koncepcji po gotowy model lub wydruk.",
            ],
        },
        {
            "role": "Asystent ds. sprzedaży i marketingu",
            "org": "Independent Traders & Consultants",
            "location": "Warszawa, Polska",
            "dates": "2023 – marzec 2026",
            "bullets": [
                "Wprowadzenie ponad 20 zagranicznych dostawców i marek na rynek polski i CEE.",
                "Organizacja 4 targów branżowych w Polsce oraz koordynacja spotkań B2B.",
                "Prowadzenie badań rynku w celu identyfikacji szans i partnerów.",
                "Bieżące wsparcie IT dla zespołu.",
            ],
        },
        {
            "role": "Młodszy asystent ds. marketingu",
            "org": "Biotop-Service Sp. z o.o.",
            "location": "Warszawa, Polska",
            "dates": "2020 – 2023",
            "bullets": [
                "Monitorowanie i utrzymanie baz danych marketingowych i klientów.",
                "Pozyskiwanie nowych klientów oraz partnerów biznesowych.",
                "Organizacja spotkań i wyjazdów biznesowych.",
                "Wsparcie IT w zespole.",
            ],
        },
        {
            "role": "Specjalista ds. sprzedaży (cold lead)",
            "org": "SentiOne",
            "location": "Polska",
            "dates": "2019 – 2020",
            "bullets": [
                "Generowanie i kwalifikacja zimnych leadów oraz kontakt z potencjalnymi klientami.",
            ],
        },
        {
            "role": "Program Work & Travel",
            "org": "Tokio, Japonia",
            "location": "Japonia",
            "dates": "2019",
            "bullets": [
                "Zdobycie międzynarodowego doświadczenia zawodowego i umiejętności komunikacji międzykulturowej.",
            ],
        },
        {
            "role": "Przedstawiciel handlowy D2D",
            "org": "Energy Match",
            "location": "Polska",
            "dates": "2018 – 2019",
            "bullets": [
                "Bezpośrednia sprzedaż door-to-door i pozyskiwanie klientów.",
            ],
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
        {
            "degree": "Świadectwo maturalne",
            "org": "Liceum nr 40 / Fundacja Nauka i Wiedza",
            "location": "Warszawa, Polska",
            "dates": "2017 – 2020",
            "note": "",
        },
    ],
    "skills": [
        {"group": "Modelowanie 3D i CAD", "items": "Blender, 3ds Max, Maya, SolidWorks, Fusion 360, Rhino 3D; druk 3D, projektowanie produktu, obiekty do gier; Photoshop"},
        {"group": "Front-end i web", "items": "HTML, CSS, JavaScript, React, Node.js, Git"},
        {"group": "Programowanie i dane", "items": "Python, C#, SQL (SSMS)"},
        {"group": "Obszary rozwoju", "items": "3D i rozwój produktu, Front-end Development, IT, cyberbezpieczeństwo"},
    ],
    "languages": [
        {"name": "Polski", "level": "Ojczysty"},
        {"name": "Angielski", "level": "Zaawansowany (C1, certyfikat TOEFL)"},
        {"name": "Hiszpański", "level": "Średnio zaawansowany (B1)"},
        {"name": "Japoński", "level": "Podstawowy (A2)"},
        {"name": "Francuski", "level": "Podstawowy (A2)"},
        {"name": "Włoski", "level": "Podstawowy (A1)"},
    ],
    "certifications": [
        "Certyfikat języka angielskiego TOEFL",
    ],
    "interests": "Podróże · Inżynieria samochodowa i motorsport · Koszykówka · Druk 3D i projektowanie produktu",
    "footer": (
        "Wyrażam zgodę na przetwarzanie moich danych osobowych na potrzeby procesu rekrutacji "
        "(zgodnie z RODO – Rozporządzenie UE 2016/679)."
    ),
}
