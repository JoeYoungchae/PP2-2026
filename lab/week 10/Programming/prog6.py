'''
작성일: 2026.11.05
작성자: 조영채

문제: 육면체 주사위 굴리기 시뮬레이션 프로그램 작성하기

조건: "굴리기" 버튼을 클릭하면 1-6 사이 임의의 정수가 표시되어야 한다.

'''

# 1. tkinter와 random 모듈을 불러온다.
from tkinter import *
import random

# 2. 루트 윈도우를 불러오고 주사위값을 저장하는 변수 dice를 생성한다.
window = Tk()
dice = 0

# 3. 주사위값을 표시하는 레이블을 생성한다.
label = Label(text=dice)
label.grid(row=0, column=0)

# 4. 주사위를 굴리는 함수를 작성한다.
def roll_dice():
    global dice
    dice = random.randint(1, 6)
    label['text'] = dice

# 5. 굴리기 버튼을 생성하여 이벤트 발생 시 호출되는 콜백 함수를 등록한다.
button = Button(window, text='굴리기', command=roll_dice)
button.grid(row=0, column=1)

window.mainloop()