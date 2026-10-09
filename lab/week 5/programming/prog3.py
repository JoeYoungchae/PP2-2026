'''
작성일: 2026.10.09
작성자: 조영채

문제: 일반적인 함수를 나타내는 Function 클래스를 정의한다. Function 클래스의 value()는 아직 결정되지 않았다.

설계:

- 클래스:
    - Function: 함수를 나타내는 클래스
        - value(x): x에서 f()의 값을 반환하는 메소드

    - Quadratic: Function 클래스를 상속받아서 2차 방정식을 나타내는 클래스.
        - __init__(self, a, b, c): a, b, c를 멤버 변수에 저장하는 생성자 함수
        - value(x): x에서 f()의 값을 반환하는 메소드
        - get_roots(): 2개의 근을 계산하여 반환한다.
'''
import cmath        # 방정식이 허근을 가질 때 cmath 모듈을 사용해 구한다.

class Function:
    def value(self, x):     # 입력값 x에서 함수의 값을 계산한다는 약속이다.
        # Function 자체에 계산식이 없으므로 직접 호출 시 에러 발생.
        raise NotImplementedError("자식 클래스에서 value 구현")

class Quadratic(Function):
    # 객체 a, b, c를 전달받아 생성자 안에서 판별식을 계산해 D에 저장한다.
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.D = b ** 2 - 4 * a * c

    def value(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def get_roots(self):
        sqrt_D = cmath.sqrt(self.D)     # 허근을 계산해주는 함수

        root1 = (-self.b + sqrt_D) / (2 * self.a)
        root2 = (-self.b - sqrt_D) / (2 * self.a)

        return root1, root2

def test_prog3():
    f = Quadratic(3, 2, 5)

    print(f"f(x) = {f.a}x^2 + {f.b}x + {f.c}")
    print(f"f(3) = {f.value(3)}")
    print(f"f(x)의 두 근: {f.get_roots()}")

if __name__ == "__main__":
    test_prog3()