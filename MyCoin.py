# Программа для имитации подбрасывания монеты
import random


class Coin:
    def __init__(self):
        self.__sideup = 'Орел'

    def toss(self):
        if random.randint(0, 1) == '0':
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup


def main():
    my_coin = Coin()
    print('Показать сторону монеты', my_coin.get_sideup())
    print('Подбрасываю монету...')
    my_coin.toss()
    print('Показать сторону монеты', my_coin.get_sideup())


main()
