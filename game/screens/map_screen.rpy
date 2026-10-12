## ═══════════════════════════════════════
##  ЭКРАН КАРТЫ ГОРОДА
## ═══════════════════════════════════════

screen map_screen():
    tag menu

    ## Фон карты
    add "images/map_city.png"

    ## Заголовок
    frame:
        xalign 0.5
        yalign 0.05
        background "#000000aa"
        xpadding 30
        ypadding 15

        text "КАРТА ГОРОДА" size 36 bold True xalign 0.5

    ## Информация о времени и деньгах
    frame:
        xalign 0.95
        yalign 0.05
        background "#000000aa"
        xpadding 20
        ypadding 10

        vbox:
            text "💰 [money] ₽" size 24
            text "🕐 [time_of_day]" size 24
            text "📅 День [day]" size 24

    ## Кликабельные зоны локаций
    for loc in locations:
        ## Проверка доступности
        $ is_available = True

        if loc["requires_flag"] and not eval(loc["requires_flag"]):
            $ is_available = False

        ## Кликабельная область (кнопка вместо hotspot)
        if is_available:
            button:
                xpos loc["x"]
                ypos loc["y"]
                xsize loc["width"]
                ysize loc["height"]
                background "#00ff0033"
                hover_background "#00ff0066"
                action Jump(loc["label"])

            ## Зелёный маркер
            text "●":
                xpos loc["x"] + loc["width"]/2
                ypos loc["y"] - 15
                xanchor 0.5
                size 28
                color "#44ff44"
                outlines [(2, "#000000", 0, 0)]

            ## Название (белое)
            text loc["name"]:
                xpos loc["x"] + loc["width"]/2
                ypos loc["y"] + loc["height"] + 5
                xanchor 0.5
                size 20
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

        else:
            ## Неактивная зона
            button:
                xpos loc["x"]
                ypos loc["y"]
                xsize loc["width"]
                ysize loc["height"]
                background "#33333333"
                action NullAction()

            ## Серый маркер с замком
            text "🔒":
                xpos loc["x"] + loc["width"]/2
                ypos loc["y"] - 15
                xanchor 0.5
                size 22
                color "#999999"
                outlines [(2, "#000000", 0, 0)]

            ## Название (серое)
            text loc["name"]:
                xpos loc["x"] + loc["width"]/2
                ypos loc["y"] + loc["height"] + 5
                xanchor 0.5
                size 20
                color "#999999"
                outlines [(2, "#000000", 0, 0)]

    ## Кнопка возврата
    textbutton "← Назад" action Return() xalign 0.05 yalign 0.95