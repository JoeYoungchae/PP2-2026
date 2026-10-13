'''
작성일: 2026.10.13
작성자: 조영채

문제: 파일 "input.txt"의 3줄을 한 줄씩 출력하라.

설계:
- 파일 "input.txt"를 읽기 모드로 연다.
- readline()으로 한 줄을 읽고, 빈 줄이 아닐 동안 출력한다.
- input.txt는 programming 폴더에서 프로그램을 실행할 때 찾는다.

'''
with open("input.txt", "r", encoding="utf-8") as f:
    line = f.readline().strip()
    while line != "":
        print(line)
        line = f.readline().strip()