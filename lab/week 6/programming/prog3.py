'''
작성일: 2026.10.13
작성자: 조영채

문제: 파일 이름과 행 번호를 입력받아 해당 행을 출력하는 프로그램을 작성하시오.

설계:
- 파일 이름과 행 번호를 입력받는다.
- 파일을 열고 입력한 행 번호의 줄을 읽는다.
- 해당 행을 지정된 형식으로 출력한다.

'''

file_name = input("파일 이름을 입력하시오: ")
line_number = int(input("행 번호를 입력하시오: "))

with open(file_name, "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[line_number - 1].strip()  # 리스트는 0부터 시작하므로 행 번호에서 1을 뺀다.
print(f"{line_number}번 행은 {line}.입니다.")