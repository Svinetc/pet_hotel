import random

print("Попробуте угадать число от 1 до 100: ")

num =  random.randint(1,100+1) # Сгенерированное число
while True:
    person_num = int(input())
    if num < person_num:
        print('Слишком много, попробуйте еще раз')
    elif num > person_num:
        print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break
