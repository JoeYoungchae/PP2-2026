'''
작성일: 2026.09.29
작성자: 조영채

문제: 고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자.
      접근자와 설정자를 사용해보자.

설계:

- 클래스:
    - Cat: 고양이의 정보를 저장하고 출력하는 클래스

- 함수:
    - __init__(self, name, age): 생성자 함수
    - __str__(): 고양이 정보를 문자열로 변환하는 함수
    - setName(), getName(), setAge(), getAge(): 각 속성에 대한 접근자와 설정자 함수들
    - test_cat(): Cat 클래스의 테스트 함수
'''


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def __str__(self):
        msg = str(self.name) + " " + str(self.age)
        return msg

def test_prob1():
    Leo = Cat(name="레오", age=1)
    print(Leo)

if __name__ == "__main__":      # 파일이 직접 실행된 경우에만 아래의 코드를 실행하라는 뜻.
    test_prob1()