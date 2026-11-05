'''
작성일: 2026.11.05
작성자: 조영채

문제: 배치 관리자를 이용하여 버튼을 3 x 10 격자 형태로 배치해보자.

설계:
1. tkinter 모듈 가져오기
2. 루트 윈도우 생성하기
3. for 반복 루프를 사용하여 버튼과 버튼의 텍스트 생성하기

'''
from tkinter import *

window = Tk()

for r in range(0, 3):
    for c in range(0, 10):
        button = Button(window, text=f"{r}행, {c}열")
        button.grid(row=r, column=c)

window.mainloop()