import sys
alphabet = 'абвгдеёжзиӣклмнопрстуфхцчшщэьъыюя'


gamer = {'name': input('Как вас зовут? '),
         'age': int(input('Сколько тебе лет? ')),
         'sex': input('Твой пол: '),
         'pet_name': input('Имя твоего питомца: '),
         }

boolvar = bool(input("Тебе нравится играть? "))
if gamer['age'] < 18:
        print('Тебе нельзя играть')
        print('Удачи ', gamer['name'])
elif gamer['age'] >= 90:
        a = input("Ты точно хочешь играть? Это может тебя утомить (N/Y): ")
        if a == 'Y':
            b = input("Точно? (N/Y): ")
            if b == 'Y':
                print('Добро пожаловать в Игру ',gamer['name'])
                namelowercase = gamer['name'].lower()
                for char in alphabet:
                    if char not in namelowercase:
                        print(char)

            elif b == 'N':
                print('Удачи ', gamer['name'])
                sys.exit(0)
            else:
                sys.exit(0)

        elif a == 'N':
            print('Удачи ', gamer['name'])
            sys.exit(0)
        else:
            sys.exit(0)



else:
    print('Добро пожаловать в Игру',gamer['name'])
    namelowercase = gamer['name'].lower()
    for char in alphabet:
        if char not in namelowercase:
           print(char)