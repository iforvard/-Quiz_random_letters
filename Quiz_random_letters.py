import random

while True:
    size_players = input('Введите число игроков ')
    if size_players.isdigit() and int(size_players) == float(size_players):
        size_players = int(size_players)
        break

ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
random_letters = [random.choice(ru_alphabet) for _ in range(size_players * 3)]
players = {}
for i in range(1, size_players + 1):
    players[i] = {
        'Имя': input(f'Введите имя Игрока #{i} '),
        'Счет': 0
    }
# Выбор игрока который ходит первый
move = random.randint(1, size_players)

print(f'В спиоск добавлно {len(random_letters)} букв. '
      f'Буквы прописные, русские и могут повторяться. '
      f'Для победы нужно первым угадать 3!')

while True:
    print(f'Ходит {players[move]["Имя"]}')
    word = input('Введите букву: ')
    if word in random_letters:
        random_letters.remove(word)
        players[move]["Счет"] += 1
        print(f'Угадал теперь твой счет {players[move]["Счет"]}')
        if players[move]['Счет'] == 3:
            print(players[move]["Имя"], 'Победил!!!')
            break
    else:
        print('Не угадал')
    if move == size_players:
        move = 1
    else:
        move += 1
