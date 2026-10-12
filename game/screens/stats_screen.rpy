## ═══════════════════════════════════════
##  ЭКРАН СТАТИСТИКИ
## ═══════════════════════════════════════

screen stats_screen():

    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        background "#000000cc"

        vbox:
            spacing 20

            text "СТАТИСТИКА" size 40 bold True xalign 0.5

            null height 20

            ## Отношения
            text "Отношения:" size 30 bold True
            hbox:
                spacing 20
                text "🌸 Аня:" size 26
                bar value rel_anya range 100 xsize 300
                text "[rel_anya]" size 26

            hbox:
                spacing 20
                text "📚 Катя:" size 26
                bar value rel_kate range 100 xsize 300
                text "[rel_kate]" size 26

            hbox:
                spacing 20
                text "🌙 Лена:" size 26
                bar value rel_lena range 100 xsize 300
                text "[rel_lena]" size 26

            null height 20

            ## Быт
            text "Быт:" size 30 bold True
            text "💰 Деньги: [money] ₽" size 26
            text "🏠 Аренда: [rent_paid]" size 26
            text "💡 Коммуналка: [utilities_paid]" size 26
            text "😊 Настроение: [mood]/100" size 26
            text "⭐ Репутация: [reputation]/100" size 26

            null height 20

            textbutton "Закрыть" action Return() xalign 0.5


## Горячая клавиша для вызова
init python:
    config.keymap['show_stats'] = ['K_F1']

    config.underlay.append(
        renpy.Keymap(
            show_stats=ShowMenu('stats_screen')
        )
    )