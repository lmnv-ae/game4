## ═══════════════════════════════════════
##  ГЛАВА 3: ВЫХОДНЫЕ
## ═══════════════════════════════════════

label chapter_3:
    $ chapter = 3
    $ day = 6
    $ time_of_day = "morning"

    scene bg bedroom_morning
    with dissolve

    "Суббота. Наконец-то выходной."

    "Я просыпаюсь поздно — в 10 утра. За окном серое небо, но настроение лучше, чем в будни."

    mc "Так, какие планы на день?"

    "Можно сходить куда-нибудь. Или остаться дома."

    "Открываю карту города на телефоне..."

    call screen map_screen

    ## Возврат из карты — игрок выбрал локацию
    jump chapter_3_end

## ═══════════════════════════════════════
##  ЛОКАЦИИ
## ═══════════════════════════════════════

label location_home:
    $ time_of_day = "day"
    scene bg bedroom_day
    with dissolve

    "Остаюсь дома. Надо отдохнуть."

    menu:
        "Посмотреть фильм":
            $ mood += 3
            "Смотрю старый комедийный фильм. Смешно, но одиноко."

        "Позвонить маме":
            $ mood += 5
            "Звоню маме. Она рада, расспрашивает о работе. Говорю, что всё хорошо."

        "Приготовить ужин":
            $ mood += 4
            "Готовлю пасту. Простое блюдо, но вкусное."

    jump chapter_3_end

label location_college:
    $ time_of_day = "day"
    scene bg college_corridor
    with dissolve

    "Иду в колледж. Сегодня субботние курсы для желающих."

    "Работаю пару часов. Студенты благодарны — не все приходят в выходной."

    $ reputation += 3

    jump chapter_3_end

label location_cafe_dream:
    $ time_of_day = "evening"
    
    scene bg cafe_interior
    with dissolve

    "Кафе «Мечта». Модное место с ярким интерьером."

    if met_anya:
        show alya_happy at center
        with dissolve

        "Аня здесь! Она сидит за столиком."

        a "[mc_name]! Привет! Садись со мной!"

        menu:
            "Сесть с ней (500 ₽ на кофе и десерт)":
                if money >= 500:
                    $ money -= 500
                    $ rel_anya += 5
                    "Сажусь. Заказываем кофе и десерт. Аня счастлива."
                else:
                    "У меня недостаточно денег. Придётся отказаться."
                    $ rel_anya -= 2
                    "Извини, Аня, я сегодня не могу..."

            "Просто выпить кофе (300 ₽)":
                if money >= 300:
                    $ money -= 300
                    $ rel_anya += 2
                    "Пью кофе. Аня рассказывает о своей жизни."
                else:
                    "Даже на кофе не хватает. Грустно."

            "Уйти без заказа":
                "Извиняюсь, спешу. Аня выглядит разочарованной."
                $ rel_anya -= 3

        hide alya_happy
        with dissolve

    else:
        "Просто пью кофе. Наблюдаю за молодёжью."

    jump chapter_3_end

label location_kate_flat:
    $ time_of_day = "evening"

    scene bg apartment_cozy
    with dissolve

    "Квартира Кати. Маленькая, но уютная."

    show kate_smile at center
    with dissolve

    k "Привет, [mc_name]. Заходи."

    menu:
        "Принести цветы (800 ₽)":
            if money >= 800:
                $ money -= 800
                $ rel_kate += 7
                "Приношу букет роз. Катя краснеет."
                k "Ой, спасибо! Как мило..."
            else:
                "У меня нет денег на цветы. Придётся прийти с пустыми руками."
                $ rel_kate += 2

        "Принести торт (500 ₽)":
            if money >= 500:
                $ money -= 500
                $ rel_kate += 5
                "Приношу торт. Катя рада."
                k "О, спасибо! Как раз к чаю."
            else:
                "Даже на торт не хватает."

        "Прийти с пустыми руками":
            $ rel_kate += 2
            "Прихожу без подарка. Катя не обижается."
            k "Главное, что ты пришёл."

    hide kate_smile
    with dissolve

    jump chapter_3_end

label location_bar_nocturne:
    $ time_of_day = "evening"

    scene bg bar_interior
    with dissolve

    "Бар «Ноктюрн». Тёмный, с приглушённым светом."

    if met_lena:
        show lena_smile at center
        with dissolve

        "Лена сидит за барной стойкой."

        l "Привет. Что будешь пить?"

        menu:
            "Виски (800 ₽)":
                if money >= 800:
                    $ money -= 800
                    $ rel_lena += 5
                    "Заказываю виски. Лена одобряет."
                    l "Хороший выбор."
                else:
                    "У меня недостаточно денег. Придётся брать что-то подешевле."
                    jump location_bar_nocturne_cheap

            "Пиво (300 ₽)":
                if money >= 300:
                    $ money -= 300
                    $ rel_lena += 2
                    "Беру пиво. Лена пожимает плечами."
                else:
                    "Даже на пиво не хватает. Грустно."

            "Просто воду (бесплатно)":
                $ rel_lena += 1
                "Беру воду. Лена усмехается."
                l "Ты сегодня экономный."

        hide lena_smile
        with dissolve

    else:
        "Пью один. Наблюдаю за людьми."

    jump chapter_3_end

label location_bar_nocturne_cheap:
    "Беру самое дешёвое пиво."
    $ money -= 300
    jump location_bar_nocturne_continue

label location_bar_nocturne_continue:
    "Продолжаю вечер в баре."
    jump chapter_3_end

label location_gym:
    $ time_of_day = "any"
    $ money -= 300
    $ mood += 5

    scene bg gym
    with dissolve

    "Спортзал. Железо, пот, музыка."

    "Час на тренажёрах. После тренировки — легче."

    "Забываю о проблемах. Только тело, только движение."

    jump chapter_3_end

label location_park:
    $ time_of_day = "day"
    $ mood += 4

    scene bg park
    with dissolve

    "Парк. Тихо, спокойно. Осенние листья шуршат под ногами."

    "Гуляю один. Думаю о жизни."

    "Может, пора что-то изменить?"

    jump chapter_3_end

label location_shop:
    $ time_of_day = "any"
    $ money -= 500

    scene bg shop
    with dissolve

    "Магазин. Покупаю продукты на неделю."

    "Очередь, суета. Но надо есть."

    jump chapter_3_end

## ═══════════════════════════════════════
##  КОНЕЦ ДНЯ
## ═══════════════════════════════════════

label chapter_3_end:
    scene bg bedroom_night
    with dissolve

    "Вечер. Я дома. Усталый, но с мыслями о прожитом дне."

    "Что дальше?"

    "Может, пора уже определиться с выбором?"

    mc "Посмотрим..."

    "Завтра — новый день. Новые решения."

    jump chapter_4