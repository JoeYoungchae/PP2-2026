# 작성일: 2026.09.29
# 작성자: 조영채
# 문제: 
# 설계: 
'''
작성일: 2026.10.03
작성자: 조영채

문제: 삼각형을 나타내는 클래스 Triangle을 작성해 보자.

설계:

- 클래스:
    - Triangle: 삼각형의 세 각을 구해 내각의 합이 180도인지 확인한다.

- 함수:
    - __init__(self, angle1, angle2, angle3): 매개 변수의 생성자 함수
    - __str__(): 삼각형의 정보를 문자열로 변환하는 함수
    - setAngle1(), getAngle1(), setAngle2(), getAngle2(), setAngle3(), getAngle3():
                각 속성에 대한 접근자와 설정자 함수들
    - checkAngles(): 삼각형 내각 합이 180도인지 확인하는 함수
'''

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.__angle1 = angle1
        self.__angle2 = angle2
        self.__angle3 = angle3

    def getAngle1(self):
        return self.__angle1
    def getAngle2(self):
        return self.__angle2
    def getAngle3(self):
        return self.__angle3

    def setAngle1(self, angle1):
        self.__angle1 = angle1
    def setAngle2(self, angle2):
        self.__angle2 = angle2
    def setAngle3(self, angle3):
        self.__angle3 = angle3

    def checkAngles(self):
        if self.__angle1 + self.__angle2 + self.__angle3 == 180:
            return True
        
        return False

    def __str__(self):
        msg = f"angle1: {self.__angle1}, angle2: {self.__angle2}, angle3: {self.__angle3}"
        return msg

def test_prog5():
    t = Triangle(90, 30, 60)
    print(t)
    print("삼각형입니다." if t.checkAngles() else "삼각형이 아닙니다.")

if __name__ == "__main__":
    test_prog5()