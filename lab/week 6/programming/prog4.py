'''
작성일: 2026.10.13
작성자: 조영채

문제: 현재 작업 디렉토리에 A.txt, B.txt, ..., Z.txt까지 총 26개의 텍스트 파일을 생성해보자.

설계:
- 알파벳 A부터 Z까지 반복한다.
- 알파벳 뒤에 ".txt"를 붙여 파일 이름을 만든다.
- 파일이 아직 없으면 쓰기 모드로 열어 빈 파일을 만든다.
- 이미 같은 이름의 파일이 있으면 내용을 덮어쓰지 않고 건너뛴다.

'''
import os       # 운영 체제와 상호작용하기 위한 내장 라이브러리

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    file_name = letter + ".txt"

    # 이미 있는 파일은 덮어쓰지 않는다.
    if not os.path.exists(file_name):       # file_name에 해당하는 파일이 있는지 확인한다.
        with open(file_name, "w", encoding="utf-8"):
            pass

print("A.txt부터 Z.txt까지 파일 생성을 완료했습니다.")