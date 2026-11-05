'''
작성일: 2026.11.05
작성자: 조영채

문제: 2개의 버튼을 가지는 카운터를 작성해보자.

조건: "감소" 버튼을 누르면 값이 1 감소하고, "증가" 버튼을 누르면 값이 1 증가한다.

'''

# 1. tkinter 모듈을 불러오고 루트 윈도우를 생성한다.
from tkinter import *

window = Tk()
total = 0

# 2. 카운터의 값을 표시하는 레이블을 생성한다.
label = Label(window, text=str(total))
label.grid(row=0, column=2, columnspan=2)

# 3. 카운터의 값을 1씩 빼거나 더해주는 함수를 작성한다.
def decrease():
    global total
    total -= 1
    # 레이블 객체가 가진 'text' 속성은 딕셔너리처럼 찾을 수 있다. 
    label['text'] = str(total)

def increase():
    global total
    total += 1
    label['text'] = str(total)

# 4. 증가, 감소 버튼을 만들고 이벤트 발생 시 호출되는 콜백 함수를 등록한다.
decreaseButton = Button(window, text='감소', command=decrease)
decreaseButton.grid(row=0, column=0, columnspan=2)

increaseButton = Button(window, text='증가', command=increase)
increaseButton.grid(row=0, column=4, columnspan=2)

window.mainloop()