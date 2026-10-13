'''
작성일: 2026.10.11
작성자: 조영채

문제: Animal 클래스를 상속받아 Cat 클래스를 정의해보자. Cat 클래스로 3마리의 고양이 객체를 생성하고,
        가장 나이가 많은 고양이의 나이를 출력한다.

설계:

- 클래스:
    - Animal: 
        - __init__(self, name, age, breed): 생성자 함수

    - Cat: Animal 클래스를 상속받아 정보를 저장한다.
        - __init__(self, name, age, breed): 생성자 함수. 부모 클래스의 생성자를 호출한다.
        - get_oldest_cat(*args): max()를 이용해 가장 나이가 많은 고양이를 반환한다. *args에 리스트를 저장한다.
'''

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class Cat(Animal): 
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

    def get_oldest_cat(self, *cats):
        # cats에는 *를 붙여 전달한 고양이 객체들이 튜플로 들어있다.
        # key는 max()가 정해 둔 매개변수 이름으로, 무엇을 기준으로 크기를 비교할지 알려준다.
        # lambda cat: cat.age 는 각 고양이(cat)의 나이(age)를 비교 기준으로 삼는다는 뜻.
        return max(cats, key=lambda cat: cat.age)

def test_prog5():
    cat_list = [
        Cat("나비", 3, "페르시안"),
        Cat("모모", 7, "러시안 블루"),
        Cat("루루", 5, "코리안숏헤어"),
    ]

    oldest = cat_list[0].get_oldest_cat(*cat_list)
    print(f"가장 나이가 많은 고양이는 {oldest.age}살입니다.")

if __name__ == "__main__":
    test_prog5()

'''
lambda cat: cat.age는,

def get_age(cat):
    return cat.age
와 같다.
'''