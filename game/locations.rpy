init python:
    locations = [
        {
            "name": "Дом",
            "label": "location_home",
            "x": 200, "y": 300, "width": 150, "height": 100,
            "description": "Моя квартира. Уютно, но одиноко.",
            "min_money": 0,
            "requires_flag": None,
            "time_of_day": "any"
        },
        {
            "name": "Колледж",
            "label": "location_college",
            "x": 500, "y": 200, "width": 200, "height": 120,
            "description": "Место работы. Шумно, но привычно.",
            "min_money": 0,
            "requires_flag": None,
            "time_of_day": "day"
        },
        {
            "name": "Кафе «Мечта»",
            "label": "location_cafe_dream",
            "x": 800, "y": 400, "width": 180, "height": 110,
            "description": "Модное кафе. Любимое место Ани.",
            "min_money": 500,
            "requires_flag": "met_anya",
            "time_of_day": "evening"
        },
        {
            "name": "Квартира Кати",
            "label": "location_kate_flat",
            "x": 350, "y": 500, "width": 160, "height": 100,
            "description": "Уютная квартира. Пахнет чаем и книгами.",
            "min_money": 0,
            "requires_flag": "met_kate",
            "time_of_day": "evening"
        },
        {
            "name": "Бар «Ноктюрн»",
            "label": "location_bar_nocturne",
            "x": 1000, "y": 250, "width": 170, "height": 100,
            "description": "Тёмный бар. Любимое место Лены.",
            "min_money": 800,
            "requires_flag": "met_lena",
            "time_of_day": "evening"
        },
        {
            "name": "Спортзал",
            "label": "location_gym",
            "x": 650, "y": 600, "width": 150, "height": 90,
            "description": "Железо и пот. Место, где забываю о проблемах.",
            "min_money": 300,
            "requires_flag": None,
            "time_of_day": "any"
        },
        {
            "name": "Парк",
            "label": "location_park",
            "x": 100, "y": 600, "width": 200, "height": 130,
            "description": "Тихий парк. Хорошее место для прогулок.",
            "min_money": 0,
            "requires_flag": None,
            "time_of_day": "day"
        },
        {
            "name": "Магазин",
            "label": "location_shop",
            "x": 900, "y": 650, "width": 140, "height": 80,
            "description": "Продуктовый магазин. Надо купить еду.",
            "min_money": 500,
            "requires_flag": None,
            "time_of_day": "any"
        }
    ]