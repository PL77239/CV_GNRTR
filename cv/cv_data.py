# -*- coding: utf-8 -*-
"""Content for Jan Blaz's CV in Polish (PL) and English (EN).

Kept as structured data so both language versions share the exact same,
ATS-friendly layout and only the text differs.
"""

# Shared contact details (identical in both versions).
CONTACT = {
    "name": "Jan Błaż",
    "phone": "+48 697 655 050",
    "email": "jmtentertainment777@gmail.com",
    # Links preserved exactly from the original CV; both stay clickable.
    "linkedin_url": "http://www.linkedin.com/in/jan-b%C5%82a%C5%BC-39b0523a5",
    "portfolio_url": "https://guapdad8k.github.io/WEB-PORTFOLIO/",
}

CV_EN = {
    "lang": "en",
    "contact": CONTACT,
    "location": "Warsaw, Poland",
    "headline": "Front-end Developer  •  IT Support  •  3D CAD Designer",
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
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
        "IT student specialising in Front-end Development, combining hands-on technical skills "
        "with several years of experience in sales, marketing and B2B development across "
        "international markets. Comfortable with HTML, C#, Python and SQL as well as CAD/3D design, "
        "with a strong interest in programming, cybersecurity and databases. Seeking a part-time "
        "role to grow within IT alongside full-time studies; open to internships."
    ),
    "experience": [
        {
            "role": "Sales & Marketing Assistant",
            "org": "Independent Traders & Consultants",
            "location": "Warsaw, Poland",
            "dates": "2023 – Mar 2026",
            "bullets": [
                "Introduced and positioned foreign brands in the Polish and CEE markets.",
                "Organised and coordinated B2B meetings and industry trade fairs.",
                "Conducted market research to identify new opportunities and partners.",
                "Provided day-to-day IT support to the team.",
            ],
        },
        {
            "role": "3D Designer (Freelance)",
            "org": "Self-employed",
            "location": "Remote",
            "dates": "2023 – Present",
            "bullets": [
                "Design technical CAD models for the automotive sector.",
                "Create abstract 3D assets for games and bespoke client projects.",
                "Deliver commercial 3D work from concept to final model.",
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
            "degree": "Study & career break (health reasons)",
            "org": "",
            "location": "",
            "dates": "2023 – 2025",
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
        {"group": "Programming & Web", "items": "HTML, C#, Python, SQL (SSMS), Java (learning)"},
        {"group": "3D & CAD", "items": "Fusion 360, technical CAD modelling, 3D asset design"},
        {"group": "Tools & Software", "items": "Visual Studio, Microsoft Office 365, Adobe Photoshop"},
        {"group": "Audio Production", "items": "Logic Pro, FL Studio"},
        {"group": "Areas of interest", "items": "Cybersecurity, Front-end Development, Databases"},
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
    "interests": "Travel · Music production · Automotive engineering & motorsport · Basketball · 3D design & programming",
}

CV_PL = {
    "lang": "pl",
    "contact": CONTACT,
    "location": "Warszawa, Polska",
    "headline": "Front-end Developer  •  Wsparcie IT  •  Projektant 3D CAD",
    "labels": {
        "linkedin": "LinkedIn",
        "portfolio": "Portfolio",
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
        "Student informatyki na kierunku Front-end Development, łączący praktyczne umiejętności "
        "techniczne z kilkuletnim doświadczeniem w sprzedaży, marketingu i rozwoju biznesu B2B na "
        "rynkach międzynarodowych. Swobodnie posługuję się HTML, C#, Python i SQL oraz "
        "projektowaniem CAD/3D, ze szczególnym zainteresowaniem programowaniem, cyberbezpieczeństwem "
        "i bazami danych. Poszukuję pracy w niepełnym wymiarze godzin, aby rozwijać się w IT "
        "równolegle ze studiami dziennymi; jestem otwarty również na staże."
    ),
    "experience": [
        {
            "role": "Asystent ds. sprzedaży i marketingu",
            "org": "Independent Traders & Consultants",
            "location": "Warszawa, Polska",
            "dates": "2023 – marzec 2026",
            "bullets": [
                "Wprowadzanie i pozycjonowanie zagranicznych marek na rynku polskim i CEE.",
                "Organizacja i koordynacja spotkań B2B oraz targów branżowych.",
                "Prowadzenie badań rynku w celu identyfikacji szans i partnerów.",
                "Bieżące wsparcie IT dla zespołu.",
            ],
        },
        {
            "role": "Projektant 3D (freelance)",
            "org": "Działalność własna",
            "location": "Zdalnie",
            "dates": "2023 – obecnie",
            "bullets": [
                "Projektowanie technicznych modeli CAD dla branży motoryzacyjnej.",
                "Tworzenie abstrakcyjnych obiektów 3D do gier i indywidualnych projektów klientów.",
                "Realizacja komercyjnych zleceń 3D od koncepcji po gotowy model.",
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
            "degree": "Przerwa w nauce i karierze (powody zdrowotne)",
            "org": "",
            "location": "",
            "dates": "2023 – 2025",
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
        {"group": "Programowanie i web", "items": "HTML, C#, Python, SQL (SSMS), Java (w nauce)"},
        {"group": "3D i CAD", "items": "Fusion 360, techniczne modelowanie CAD, projektowanie obiektów 3D"},
        {"group": "Narzędzia i oprogramowanie", "items": "Visual Studio, Microsoft Office 365, Adobe Photoshop"},
        {"group": "Produkcja muzyczna", "items": "Logic Pro, FL Studio"},
        {"group": "Obszary zainteresowań", "items": "Cyberbezpieczeństwo, Front-end Development, bazy danych"},
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
    "interests": "Podróże · Produkcja muzyczna · Inżynieria samochodowa i motorsport · Koszykówka · Projektowanie 3D i programowanie",
}
