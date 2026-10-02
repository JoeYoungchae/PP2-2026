'''
작성일: 2026.09.29
작성자: 조영채

문제: 로켓을 나타내는 Rocket 클래스를 작성해 보자.

설계:

- 클래스:
    - Rocket: 로켓의 위치를 저장하고 출력하는 클래스.

- 함수:
    - __init__(self, x, y): 생성자 함수
    - __str__(): 로켓 정보를 문자열로 변환하는 함수
    - moveUp(self): 로켓의 y좌표가 1만큼 증가된다.
'''

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y += 1

    def __str__(self):
        msg = str(self.y)
        return msg
    
def test_prob2():
    myRocket = Rocket(0, 0)
    print("로켓의 높이:", myRocket)

    myRocket.moveUp()
    print("로켓의 높이:", myRocket)

if __name__ == "__main__":
    test_prob2()