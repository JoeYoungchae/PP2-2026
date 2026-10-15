'''
작성일: 2026.10.15
작성자: 조영채

문제: 파일을 변환하는 프로그램 작성하기

실행 결과:
    line 1                      line 1
    line 2          ->          line 2
    line 3                      line 2-1
                                line 3

설계:
- 

'''

with open("prog5.txt", "r", encoding="utf-8") as infile:
    # splitlines(): 줄바꿈을 기준으로 내용을 나눠 lines 리스트에 넣음
    lines = infile.read().splitlines()

line2 = lines[1]    # 두 번째 줄인 line 2
lines.insert(2, line2 + "-1")

with open("prog5.txt", "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(lines) + "\n")