print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")
player_1 = input('Игрок 1, введите свое имя: ')
player_2 = input('Игрок 2, введите свое имя: ')

play = ('камень', 'ножницы', 'бумага',)
hints = 'соблюдайте правила игры. Начнем игру заново!'

while True:
    step_p_1 = input(f'{player_1}:')
    step_p_2 = input(f'{player_2}:')

    # Проверяем введенные данные, если они не соответствуют условиям игры
    # выводим сообщение об ошибку

    if step_p_1 not in play and step_p_2 not in play:
        print('ПРЕДУПРЕЖДЕНИЕ: Пожалуйста', hints)
    elif step_p_1 not in play:
        print('ПРЕДУПРЕЖДЕНИЕ: ', player_1, hints)
    elif step_p_2 not in play:
        print('ПРЕДУПРЕЖДЕНИЕ: ', player_2, hints)
    # если все игроки верно сделали свой ход, проверяем кто выиграл
    else:
        if step_p_1 == step_p_2:
            print('Ничья! Продолжайте играть')
        elif ((step_p_1 == 'камень' and step_p_2 == 'ножницы')
              or (step_p_1 == 'ножницы' and step_p_2 == 'бумага')
              or (step_p_1 == 'бумага' and step_p_2 == 'камень')):
            print(f'Поздравляем! Победитель - {player_1}!')
            if input('Хотите сыграть еще раз? (да/нет): ') == 'нет':
                print('До встречи!')
                break

        else:
            print(f'Поздравляем! Победитель - {player_2}!')
            if input('Хотите сыграть еще раз? (да/нет): ') == 'нет':
                print('До встречи!')
                break
