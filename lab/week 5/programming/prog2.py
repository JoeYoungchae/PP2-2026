'''
작성일: 2026.10.09
작성자: 조영채

문제: 주소를 나타내는 Address와 사람을 나타내는 Person 클래스를 정의한다. Address와 Person을 동시에 상속받아서
      Contact 클래스를 정의해보자. Contact 클래스는 연락처를 나타낸다.

설계:

- 클래스:
    - Address: 
        - __init__(self, street, city): street, city를 멤버 변수에 저장하는 생성자 함수

    - Person: 
        - __init__(self, name, email): name, email을 멤버 변수에 저장하는 생성자 함수

    - Contact(Address, Person): 
        - __init__(self, street, city, name, email): 부모 클래스의 생성자로 street, city, name, email을 저장한다.
'''

class Address:
    def __init__(self, street, city):
        self.street = str(street)       # 전달받은 값을 문자열로 바꾼다.
        self.city = str(city)

class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

def test_prog2():
    contact = Contact("Baker St.", "London", "Sherlock Holmes", "sherlock@example.com")
    # 리스트 elements에 연락처의 각 요소를 담아, for문을 통해 한 줄에 하나씩 출력한다.
    elements = [contact.name, contact.email, contact.street, contact.city]
    for element in elements:
        print(element)

if __name__ == "__main__":
    test_prog2()