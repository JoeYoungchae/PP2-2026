'''
작성일: 2026.11.05
작성자: 조영채

문제: 하나의 레이블과 하나의 버튼을 가지는 프로그램을 작성하자. 

조건: 버튼을 누르면 레이블은 "clicked"를 표시한다.

설계:
1. tkinter의 모듈을 가져온다.
2. process() 함수를 정의한다. process()가 호출되면 레이블 위젯의 텍스트가 clicked로 바뀐다.
3. 루트 윈도우 생성하고 window에 할당.
4. Button 클래스로 버튼 생성, command 인수에 process() 전달.
5. 격자 배치 관리자로 위젯을 배치한다.
6. 윈도우의 이벤트 루프를 시작한다.

'''

from tkinter import *

def process():
    label['text'] = "clicked"

window = Tk()
window.geometry("200x100")

label = Label(window, text="Hi!")
label.grid(row=0, column=0)

button = Button(window, text="click me", command=process)
button.grid(row=0, column=1)

window.mainloop()