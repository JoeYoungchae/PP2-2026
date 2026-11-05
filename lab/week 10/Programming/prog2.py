'''
작성일: 2026.11.05
작성자: 조영채

문제: 하나의 레이블을 가지는 프로그램 작성하기.

조건: 
    - 레이블의 배경색은 오렌지색, 글자색은 파란색으로 한다.
    - 레이블 크기는 50 x 3으로 한다.

설계:
1. tkinter 모듈을 가져온다.
2. 루트 윈도우를 생성하고 window에 할당한다.
3. 레이블을 생성하고 매개변수에 배경색, 글자색, 크기를 전달한다.
4. 이벤트 루프를 시작한다.

'''

from tkinter import *

window = Tk()

label = Label(text="Hello, I'm Label", bg='orange', fg='blue', width=50, height=3)
label.pack()

window.mainloop()