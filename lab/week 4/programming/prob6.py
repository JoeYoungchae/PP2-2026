'''
작성일: 2026.10.03
작성자: 조영채

문제: Person이라는 클래스를 작성해 보자.

설계:

- 클래스:
    - Person: 사람의 연락처를 저장한다.

- 함수:
    - __init__(self, name, mobile, office, email): 사람의 연락처를 초기화한다.
    - __str__(): Person의 정보를 문자열로 변환하는 함수
    - 각 속성에 대한 접근자와 설정자 함수들
'''


class Person:
    def __init__(self, name, mobile="", office="", email=""):       # 생략할 수 있도록 인수에 기본값 저장
        self.__name = name
        self.__mobile = mobile
        self.__office = office
        self.__email = email

    def getName(self):
        return self.__name

    def getMobile(self):
        return self.__mobile

    def getOffice(self):
        return self.__office

    def getEmail(self):
        return self.__email

    def setName(self, name):
        self.__name = name

    def setMobile(self, mobile):
        self.__mobile = mobile

    def setOffice(self, office):
        self.__office = office

    def setEmail(self, email):
        self.__email = email

    def __str__(self):
        return (
            f"name: {self.__name}, mobile: {self.__mobile}, "
            f"office: {self.__office}, email: {self.__email}"
        )


def test_prog6():
    p1 = Person("Kim", office="1234", email="kim@company.com")
    p2 = Person("Park", office="2345")
    p2.setEmail("park@company.com")

    print(p1)
    print(p2)

if __name__ == "__main__":
    test_prog6()
