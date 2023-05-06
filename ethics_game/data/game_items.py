from typing import Any, Literal


Enemies: dict[tuple[int, int], dict[Literal["name", "after", "answer", "img_uri"], Any]] = {
    (178, 107): {
        "name": "Software Licenses",
        "after": "Public Domain Software may be either closed or open source.",
        "answer": "B",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q0.png",
    },
    (178, 129): {
        "name": "Personal Privacy",
        "after": "All activity on company-owned devices are not the private property of the employee.",
        "answer": "C",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q1.png",
    },
    (193, 131): {
        "name": "Environmental Sustainability",
        "after": "Strengthening the specs of your machine is the most eco-friendly and efficient strategy, although horizontal scaling is inevitable",
        "answer": "A",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q2.png",
    },
    (215, 129): {
        "name": "Client Security",
        "after": "To your clients, the worst situation is a data breach. Their sensitive data must be protected.",
        "answer": "C",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q3.png",
    },
    (217, 109): {
        "name": "Personal Privacy II",
        "after": "Clients and employees all have digital footprints that can affect their work life",
        "answer": "B",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q4.png",
    },
    (219, 144): {
        "name": "Trojan Horse",
        "after": "Trojans disguise themselves as regular software, being unnoticed by the victim",
        "answer": "A",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q5.png",
    },
    (225, 117): {
        "name": "Social Requisites",
        "after": "Commerical software must adhere to all aforementioned criteria",
        "answer": "D",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q6.png",
    },
    (251, 123): {
        "name": "User Experience",
        "after": "The other answers are distractions; familiar and easy to use UI is a key factor of UX",
        "answer": "D",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q7.png",
    },
    (233, 125): {
        "name": "Embedded Software",
        "after": "Bluetooth is a convenience feature and is by no means always necessary in embedded systems",
        "answer": "C",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q8.png",
    },
    (235, 144): {
        "name": "Social Media",
        "after": "Content recommendation algorithms may relate to ethics, but are less pivotal to the end user's privacy than the other answers",
        "answer": "B",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q9.png",
    },
    (241, 133): {
        "name": "Robust Data",
        "after": "All these factors contribute to creating robust data structures with minimal unexpected behaviour",
        "answer": "A",
        "img_uri": "https://raw.githubusercontent.com/amiyuki7/ethics_game/main/images/q10.png",
    },
}
