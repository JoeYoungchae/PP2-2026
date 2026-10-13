'''
작성일: 2026.10.13
작성자: 조영채

문제: 파일 "input.txt" 안에 저장된 단어 중에서 가장 긴 단어를 찾는 프로그램을 작성하라.

설계:
- 파일 "input.txt"를 읽기 모드로 연다.
- 각 줄을 공백으로 나누어 단어를 하나씩 확인한다.
- 지금까지 찾은 단어보다 더 긴 단어가 있으면 가장 긴 단어를 갱신한다.
- 모든 단어를 확인한 뒤 가장 긴 단어를 출력한다.

'''

with open("input.txt", "r", encoding="utf-8") as f:
    longest_word = ""

    for line in f:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

if longest_word == "":
    print("파일에 단어가 없습니다.")
else:
    print(f"가장 긴 단어는 {longest_word}입니다.")