'''
작성일: 2026.10.03
작성자: 조영채

문제: 상자를 나타내는 Box 클래스를 작성해보자.

설계:

- 클래스:
    - Box: 상자의 길이와 높이를 저장하여 상자의 부피를 계산 후 출력한다.

- 함수:
    - __init__(self, length, height, depth): 매개 변수 length, height, depth를 가지는 생성자 함수
    - __str__(): 상자 정보를 문자열로 변환하는 함수
    - setLength(), getLength(), setHeight(), getHeight(), setDepth(), getDepth(): 각 속성에 대한 접근자와 설정자 함수들
'''

class Box:
    def __init__(self, length, height, depth):
        self.__length = length
        self.__height = height
        self.__depth = depth
        self.volume = length * height * depth

    def getLength(self):
        return self.__length

    def getHeight(self):
        return self.__height

    def getDepth(self):
        return self.__depth

    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def setDepth(self, depth):
        self.__depth = depth

    def __str__(self):
         return "상자의 부피는 " + str(self.volume) + "입니다."


def test_prog3():
    b1 = Box(100, 100, 100)
    print(b1)


if __name__ == "__main__":
    test_prog3()