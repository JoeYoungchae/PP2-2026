'''
작성일: 2026.10.09
작성자: 조영채

문제: 2차원 공간의 한 점(x, y)를 나타내는 클래스 Point 정의한다. 이 클래스의 __init__() 메소드는 self, x, y를 받아서
      멤버 변수에 할당한다. __str__()을 정의하여 "(x, y)" 형태의 문자열을 반환한다. Point를 상속받아서 3차원 공간의 한 점 (x, y, z)를
      나타내는 Point3D 클래스를 정의해보자.

설계:

- 클래스:
    - Point: 2차원 공간의 한 점 (x, y)를 나타내는 클래스
        - __init__(self, x, y): x, y를 멤버 변수에 저장한다.
        - __str__(self): 점을 "(x, y)" 형태의 문자열로 반환한다.

    - Point3D(Point): Point를 상속받아 3차원 공간의 한 점 (x, y, z)를 나타내는 클래스
        - __init__(self, x, y, z): 부모 클래스의 생성자로 x, y를 저장하고, z를 멤버 변수에 저장한다.
        - __str__(self): 좌표를 "(x, y, z)" 형태의 문자열로 반환한다.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        twoD_coordinate = f"({str(self.x)}, {str(self.y)})"
        return twoD_coordinate

class Point3D(Point):       # Point 클래스를 상속받음
    def __init__(self, x, y, z):
        super().__init__(x, y)      # 부모 클래스의 생성자 호출
        self.z = z

    def __str__(self):
        threeD_coordinate = f"({self.x}, {self.y}, {self.z})"
        return threeD_coordinate

def test_prog1():
    coordinate = Point3D(10, 10, 10)
    print(coordinate)

if __name__ == "__main__":
    test_prog1()