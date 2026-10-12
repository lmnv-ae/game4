label start:

    ## Начальные настройки
    $ chapter = 0
    $ quick_menu = True

    ## Имя игрока
    $ mc_name = renpy.input("Как тебя зовут?", default="Алекс", length=20).strip()
    if not mc_name:
        $ mc_name = "Алекс"

    jump prologue