import random 

def rock_poper_scissors():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)
    user_choice = input("Ваш выбор (камень, ножницы, бумага): ").lower()
    print(f'Вы выбрали: {user_choice}')
    print(f'Компьютер выбрал: {computer_choice}')
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
    else:
        print("Вы проиграли.")

rock_poper_scissors()


