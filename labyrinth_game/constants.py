# labyrinth_game/constants.py
"""
Лабиринт Шиноби: Испытание Воли Огня
Описание всех комнат и их свойств
"""

ROOMS = {
    "entrance": {
        "description": (
            "Каменные ворота с эмблемой Конохи. Перед тобой надпись: "
            "'Лишь тот, кто хранит волю огня, войдет.'"
        ),
        "exits": {"north": "academy"},
        "items": ["wooden_leaf_symbol"],
        "puzzle": (
            "Как называется философия, которой следуют шиноби Конохи?",
            "Воля огня",
        ),
    },

    "academy": {
        "description": (
            "Старое здание с деревянными полами и свитками. "
            "На доске написано имя Ирyки."
            "Ты вспоминаешь свои первые уроки ниндзя."
        ),
        "exits": {"south": "entrance", "east": "training_field"},
        "items": ["basic_scroll"],
        "puzzle": (
            "Кто был первым учителем Наруто в Академии ниндзя?",
            "Ирyка",
        ),
    },

    "training_field": {
        "description": (
            "Поле с тремя столбами и колокольчиком. "
            "Ты чувствуешь, что кто-то наблюдает за тобой издалека."
        ),
        "exits": {"west": "academy", "north": "forest_of_death"},
        "items": ["bell"],
        "puzzle": (
            "Кто проверял Наруто, Сакуру и Саске в их первом задании?",
            "Какаши",
        ),
    },

    "forest_of_death": {
        "description": (
            "Тёмный и влажный лес, наполненный звуками. "
            "По деревьям видны следы боя. Ты чувствуешь присутствие Орочимару..."
        ),
        "exits": {"south": "training_field", "east": "cave_of_snakes"},
        "items": ["hidden_kunai"],
        "puzzle": (
            "Как зовут sannin, владевшего змеями?",
            "Орочимару",
        ),
    },

    "cave_of_snakes": {
        "description": (
            "Стены покрыты символами призыва. В глубине слышится шипение. "
            "В центре — огромная печать с змеей."
        ),
        "exits": {"west": "forest_of_death", "north": "temple_of_akatsuki"},
        "items": ["summon_scroll"],
        "puzzle": (
            "Как зовут змея-призыва Орочимару?",
            "Манда",
        ),
    },

    "temple_of_akatsuki": {
        "description": (
            "Красные облака украшают стены. Воздух пропитан мрачной чакрой. "
            "Ты чувствуешь взгляды Итачи и Нагато..."
        ),
        "exits": {"south": "cave_of_snakes", "east": "bridge_of_meeting"},
        "items": ["akatsuki_ring"],
        "puzzle": (
            "Кто был лидером организации Акацуки?",
            "Пэйн",
        ),
    },

    "bridge_of_meeting": {
        "description": (
            "Туман, дождь, запах стали. На мосту — разбитая маска. "
            "Ты вспоминаешь бой Какаши и Забузы..."
        ),
        "exits": {"west": "temple_of_akatsuki", "north": "hokage_office"},
        "items": ["mist_headband"],
        "puzzle": (
            "Как назывался меч Забузы?",
            "Кубикириботё",
        ),
    },

    "hokage_office": {
        "description": (
            "Огромное окно с видом на Коноху. На столе лежит свиток с символом Огня. "
            "Ты чувствуешь спокойствие — испытание окончено."
        ),
        "exits": {"south": "bridge_of_meeting"},
        "items": ["hokage_scroll"],
        "puzzle": (
            "Кто стал Седьмым Хокаге?",
            "Наруто",
        ),
    },
}