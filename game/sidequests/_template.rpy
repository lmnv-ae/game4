## Шаблон сайд-квеста. Скопируй и переименуй.

label sidequest_TEMPLATE:
    # Условие входа
    if not met_eileen:
        return

    scene bg location
    with dissolve

    "Текст квеста..."

    menu:
        "Вариант А":
            $ rel_eileen += 1
        "Вариант Б":
            pass

    return