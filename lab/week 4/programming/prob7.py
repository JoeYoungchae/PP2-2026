'''
작성일: 2026.10.03
작성자: 조영채

문제: 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성해보자.

설계:

- 클래스:
    - PhoneBook: 딕셔너리를 이용해 사람들의 연락처를 저장한다. 연락처는 (name, mobile, office, email)로 구성된다.

- 함수:
    - __init__(self): 생성자 함수. 생성자에서 딕셔너리를 생성한다.
    - __str__(): 연락처의 정보를 문자열로 변환하는 함수
    - add(self, name, mobile=None, office=None, email=None): 한 사람의 연락처를 추가하는 함수
'''

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email,     # 키: 값
        }

    def __str__(self):
        if not self.contacts:
            return ""           # 연락처가 비어있으면 빈 문자열을 반환한다.

        lines = []
        for name, contact in self.contacts.items():
            lines.append(
                f"{name}\n"
                f"office phone: {contact['office']}\n"
                f"email address: {contact['email']}"
            )
        return "\n\n".join(lines)


def test_prog7():
    obj = PhoneBook()
    obj.add("Kim", office="1234", email="kim@company.com")
    obj.add("Park", office="2345", email="park@company.com")
    print(obj)


if __name__ == "__main__":
    test_prog7()
