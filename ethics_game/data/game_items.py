from typing import Any, Literal


Enemies: dict[
    tuple[int, int], dict[Literal["name", "question", "after", "answer", "img_uri"], Any]
] = {
    (186, 78): {
        "name": "Crystode",
    },
    (162, 61): {
        "name": "Stone Soldier",
    },
    (194, 90): {
        "name": "Leaf Lurker",
    },
    (212, 92): {
        "name": "Sideways Ghost",
    },
    (220, 70): {
        "name": "Mini Minotaur",
    },
    (238, 81): {
        "name": "Ruin Guard",
    },
    (178, 107): {
        "name": "Software Licenses",
        "question": "Which is not always true for Public Domain Software?<BR> <BR>[A] It has no ownership<BR>[B] It is open source<BR>[C] Anybody can redistribute it<BR>[D] Anybody can modify it",
        "after": "Public Domain Software may be either closed or open source.",
        "answer": "B",
        "img_uri": "",
    },
    (178, 129): {
        "name": "Personal Privacy",
        "question": "Which area of IT in the workplace can affect personal privacy?<BR> <BR>[A] Personal photos left in company cubicles<BR>[B] Mileage accured on company vehicles<BR>[C] Text messages sent on company owned devices<BR>[D] Taking a phone call during lunch break",
        "after": "All activity on company-owned devices are not the private property of the employee.",
        "answer": "C",
        "img_uri": "",
    },
    (193, 131): {
        "name": "Environmental Sustainability",
        "question": "As cloud hosting/computing becomes the modern de facto, which scaling strategy is most eco-friendly and efficient?<BR> <BR>[A] Vertical cloud scaling<BR>[B] Horizontal cloud scaling<BR>[C] Rewrite all the code in Rust<BR>[D] Rate limit server requests",
        "after": "Strengthening the specs of your machine is the most eco-friendly and efficient strategy, although horizontal scaling is inevitable",
        "answer": "A",
        "img_uri": "",
    },
    (170, 4): {
        "name": "Wavy Shadow",
    },
    (168, 47): {
        "name": "Fang",
    },
    (168, 49): {
        "name": "Phoenix",
    },
    (168, 51): {
        "name": "West Key Guardian",
    },
    (215, 129): {
        "name": "Client Security",
        "question": "Which best maximises client security?<BR> <BR>[A] SQL injection prevention<BR>[B] Scanning dependency vulnerabilities<BR>[C] Securely hashing & salting sensitive data<BR>[D] Stronger frontend/backend encryption",
        "after": "To your clients, the worst situation is a data breach. Their sensitive data must be protected.",
        "answer": "C",
        "img_uri": "",
    },
    (217, 109): {
        "name": "Personal Privacy II",
        "question": "With the advance of software, companies can now scour the web for the online presence of potential clients and employees. Which conclusion is best drawn?<BR> <BR>[A] Software enhances productivity at the cost of consumer prices<BR>[B] Software enhances efficiency at the cost of personal privacy<BR>[C] Software enhances productivity at the cost of client experience<BR>[D] Software makes all company clients subject to blackmail",
        "after": "Clients and employees all have digital footprints that can affect their work life",
        "answer": "B",
        "img_uri": "",
    },
    (219, 144): {
        "name": "Client Health",
        "question": "",
        "after": "",
        "answer": "A",
        "img_uri": "",
    },
    (225, 117): {
        "name": "Giga Gnome",
    },
    (212, 31): {
        "name": "Eden",
    },
    (214, 4): {
        "name": "Cayenne",
    },
    (220, 6): {
        "name": "Calcifer",
    },
    (222, 25): {
        "name": "Topaz Tiger",
    },
    (235, 25): {
        "name": "Cavalier",
    },
    (237, 6): {
        "name": "Mythic Guardian",
    },
    (251, 123): {
        "name": "Life Mage",
    },
    (233, 125): {
        "name": "Iron Ballista",
    },
    (235, 144): {
        "name": "Witch of Flames",
    },
    (241, 133): {
        "name": "Dragon of Terror",
    },
    (242, 157): {
        "name": "Necromancer",
    },
    (242, 161): {
        "name": "Hellfire Stallion",
    },
    (242, 165): {
        "name": "Arctic Prisoner",
    },
    (242, 169): {
        "name": "Heavy Sentry",
    },
    (242, 173): {
        "name": "Executioner",
    },
    (242, 177): {
        "name": "Scoundrel",
    },
}
