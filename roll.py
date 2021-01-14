'''Случайным образом выпадает число в диапазоне от 1 до 99.'''
import random

number = random.randint(1, 99)

def dice_n_roll(guess):
    '''Случайным образом выпадает число в диапазоне от 1 до 99.'''

    while guess != number:
        if (guess - number) < -10 and 0 < guess < 100:
            print('Нет, загаданное число гораздо больше этого.')
        elif 0 < (guess - number) < 10 and 0 < guess < 100:
            print('Горячо, загаданное число немного меньше этого.')
        elif 10 < (guess - number) < 100 and 0 < guess < 100:
            print('Холодно, загаданное число гораздо меньше этого.')
        elif (-10 < (guess - number) < 0) and (0 < guess < 100):
            print('Рядом, загаданное число немного больше этого.')
        else:
            print('Число вне заданного диапазона.')

        guess = int(input('Введите целое число: '))

    print('Поздравляю, вы угадали,')
    print('(хотя и не выиграли никакого приза!)')
    print('Завершено')

goal = int(input('Угадайте целое число(от 1 до 99): '))
dice_n_roll(goal)

#print(dice_n_roll.__doc__)
__version__ = '0.1'
