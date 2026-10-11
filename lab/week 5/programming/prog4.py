'''
작성일: 2026.10.11
작성자: 조영채

문제: 주사위 게임 프로그램을 작성해보자. 정상적인 주사위를 나타내는 Dice를 먼저 작성하고, Dice 클래스를 상속받아서
        FraudDice 클래스를 작성하여 원하는 수가 나올 때까지 주사위를 굴린다.

설계:

- 클래스:
    - Dice: 주사위를 나타내는 클래스
        - roll(): 난수를 이용해 주사위를 한 번 던지는 동작을 구현하는 메소드

    - FraudDoice: Dice를 상속받아서 원하는 숫자가 나올 때까지 주사위를 굴린다.
        - roll(): 주사위의 값이 3이하이면 다시 던진다.
'''

import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class FraudDice(Dice):
    def roll(self):
        while True:
            value = super().roll()
            if value > 3:
                return value

def test_prog4():
    d = Dice()
    print(d.roll())

    fd = FraudDice()
    for _ in range(10):
        print(fd.roll())

if __name__ == "__main__":
    test_prog4()