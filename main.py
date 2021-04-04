#project monopoly
#Правила игры: побеждает тот, кто первый соберет комбинацию из трех компаний
#Карта 5х5, в углах карты находятся пустые клетки
#Игроки начинают игру с пустой клетки
#Игра расчитана на двух игроков
#Команды: b - купить компанию, m - пропустить и бросить кубик
#На старте игроки имеют 2000$
#Игрок может приобрести карту только до броска кубика


import random
print("\nСписок команд")
print("b - купить клетку;")
print("t - бросок кубиков;")
credit1 = 2000
credit2 = 2000
card1 = []
card2 = []
a = ['Старт/Финиш','Велопрокат','Пониклуб ','Прокат электросамокатов','Пустая клетка','Кафе-мороженое','Хот-доги','Пиццерия','Пустая клетка','Роллердром','Каток','Бассейн','Пустая клетка','Аквапарк','Центральный парк','Горголыжный курорт']
n = 1
player1 = 0
player2 = 0
cube = 0

while True:
    while n == 1:
        print('\nХОД ПЕРВОГО ИГРОКА')
        print('Вы находитесь на ', a[player1])
        if len(card1) == 1:
            print('У вас есть ', ' '.join(card1))
        elif len(card1) > 1:
            print('У вас есть ', ', '.join(card1))
        print('Остаток ', credit1)
        command = input("Введите команду: ")
        if command == 'b':
            if player1 == 0 or player1 == 4 or player1 == 8 or player1 == 12:
                print('Вы стоите на пустой клетке. Пожалуйста, сделайте ход.')
                n = 0

            elif a[player1] in card1:
                print('У вас уже есть такая карта')
                n = 0
            elif a[player1] in card2:
                print('Вы не можете купить эту карту, так как ею владеет игрок 2.')
                n = 0
            else:
                print('Вы уверены, что хотите купить - ', a[player1],'Цена - 400$ ', '(yes/no)')
                command = input()
                if command == 'yes':
                    if credit1 - 400 > 0:
                        credit1 -= 400
                        card1.append(a[player1])
                        if a[1] and a[2] and a[3] in card1 or a[5] and a[6] and a[7] in card1 or a[9] and a[10] and a[11] in card1 or a[13] and a[14] and a[15] in card1:
                            print('Победил игрок 1')
                            n = 10
                        
                        command = input('Бросить кубик: ')
                        cube = random.randrange(1, 6)
                        print('Выпало: ', cube)
                        player1 += cube
                        if player1 > 15:
                            player1 -= 16
                        print('Вы стоите на ', a[player1])
                    else:
                        print('У вас недостаточно средств. Победил игрок 2.')
                        n = 10
                else:
                    n = 0

        elif command == 't':
            cube = random.randrange(1,6)
            print('Выпало: ', cube)
            player1 += cube
            if player1 > 15:
                player1 -= 16
            print('Вы стоите на ', a[player1])
        if len(card1) + len(card2) == 12:
            print('Игра окончена в ничью')
            n = 10
        n += 1

    while n == 2:
        print('\nХОД ВТОРОГО ИГРОКА')
        print('Вы находитесь на ', a[player2])
        if len(card2) == 1:
            print('У вас есть ', ' '.join(card2))
        elif len(card2) > 1:
            print('У вас есть ', ', '.join(card2))
        print('Остаток ', credit2)
        command = input("Введите команду: ")
        if command == 'b':
            if player2 == 0 or player2 == 4 or player2 == 8 or player2 == 12:
                print('Вы стоите на пустой клетке. Пожалуйста, сделайте ход.')
                n = 3
            elif a[player2] in card2:
                print('У вас уже есть такая карта')
                n = 3
            elif a[player2] in card1:
                print('Вы не можете купить эту карту, так как ею владеет игрок 1.')
                n = 3
            else:
                print('Вы уверены, что хотите купить - ', a[player2], 'Цена - 400$ ', '(yes/no)')
                command = input()
                if command == 'yes':
                    if credit2 - 400 > 0:
                        credit2 -= 400
                        card2.append(a[player2])
                        if a[1] and a[2] and a[3] in card2 or a[5] and a[6] and a[7] in card2 or a[9] and a[10] and a[11] in card2 or a[13] and a[14] and a[15] in card2:
                            print('Победил игрок 2')
                            n = 10
                        command = input('Бросить кубик: ')
                        cube = random.randrange(1, 6)
                        print('Выпало: ', cube)
                        player2 += cube
                        if player2 > 15:
                            player2 -= 16
                        print('Вы стоите на ', a[player2])
                    else:
                        print('У вас недостаточно средств. Победил игрок 1.')
                        n = 10
                else:
                    command = input('Кинуть кубик: ')
                    n = 2

        elif command == 't':
            cube = random.randrange(1, 6)
            print('Выпало: ', cube)
            player2 += cube
            if player2 > 15:
                player2 -= 16
            print('Вы стоите на ', a[player2])
        if len(card1) + len(card2) == 12:
            print('Игра окончена в ничью')
            n = 10
        n -= 1
    



