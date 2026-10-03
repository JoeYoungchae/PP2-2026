'''
작성일: 2026.10.03
작성자: 조영채

문제: 노래 가사를 출력하는 Song이라는 클래스를 작성해보자.

설계:

- 클래스:
    - Song: 노래 가사를 리스트로 받아서 한 줄에 한 항목씩 출력한다.

- 함수:
    - __init__(self): 생성자 함수
    - __str__(): Song의 정보를 문자열로 변환하는 함수
    - sing(): 가사를 한 줄에 한 항목씩 출력하는 함수
'''

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for lyric in self.lyrics:
            print(lyric)

    def __str__(self):
        return "\n".join(self.lyrics)


def test_prog8():
    littleWing = Song(["When I'm sad she comes to me", "With a thousand smiles",
                       "She gives to me free", '"It\'s alright", she says "It\'s alright"',
                       "Take anything you want from me, ANYTHING"])
    littleWing.sing()

if __name__ == "__main__":
    test_prog8()