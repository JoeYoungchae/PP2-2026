'''
작성일: 2026.10.03
작성자: 조영채

문제: 사각형을 나타내는 Rectangle 클래스를 작성해 보자.

설계:

- 클래스:
    - Rectangle: 사각형 두 개의 좌표를 구해 서로 겹치는 지 알려주는 클래스

- 함수:
    - __init__(self, x, y, w, h): 매개변수 x, y, w, h를 가지는 생성자 함수
    - __str__(): 사각형의 좌표와 크기를 문자열로 반환하는 함수
    - setX(), getX(), setY(), getY(), setWidth(), getWidth(), setHeight(), getHeight():
                각 속성에 대한 접근자, 설정자 함수들
    - getArea(): 사각형의 면적을 계산하여 반환한다.
    - overlap(r): 현재 사각형과 전달된 사각형이 겹치면 True, 그렇지 않으면 False 반환.
'''

class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def overlap(self, r):
        lt1 = self.__x
        rt1 = self.__x + self.__width
        top1 = self.__y
        bottom1 = self.__y + self.__height

        lt2 = r.__x
        rt2 = r.__x + r.__width
        top2 = r.__y
        bottom2 = r.__y + r.__height

        if rt1 <= lt2:
            return False
        if lt1 >= rt2:
            return False
        if bottom1 <= top2:
            return False
        if top1 >= bottom2:
            return False

        return True

    def __str__(self):
        return f"Rectangle(x={self.__x}, y={self.__y}, w={self.__width}, h={self.__height})"

def test_prog4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    print(r1)
    print(r2)
    print("r1과 r2는 서로 겹침" if r1.overlap(r2) else "r1과 r2는 서로 겹치지 않음")
    # 조건 표현식(삼항 연산자), 참일 때 값 if 조건 else 거짓일 때 값

if __name__ == "__main__":
    test_prog4()