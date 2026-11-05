'''
작성일: 2026.11.05
작성자: 조영채

문제: 주소를 입력하는 다음과 같은 어플을 작성해보기

설계:
1. tkinter 모듈 가져오기
2. Label 클래스를 이용해 격자 배치 관리자를 이용해 주소 정보 레이블 만들기
3. Entry 클래스를 이용해 주소 정보를 입력하는 엔트리 위젯 만들기
4. Button 클래스를 이용해 삭제, 제출 버튼 만들기

'''

from tkinter import *

window = Tk()

Label(window, text='이름:').grid(row=0, column=0)
Label(window, text='주소:').grid(row=1, column=0)
Label(window, text='도:').grid(row=2, column=0)
Label(window, text='우편번호:').grid(row=3, column=0)
Label(window, text='국가:').grid(row=4, column=0)

name = Entry(window).grid(row=0, column=1, columnspan=30)
address = Entry(window).grid(row=1, column=1, columnspan=30)
state = Entry(window).grid(row=2, column=1, columnspan=30)
postcode = Entry(window).grid(row=3, column=1, columnspan=30)
nation = Entry(window).grid(row=4, column=1, columnspan=30)

clearButton = Button(window, text='clear')
clearButton.grid(row=5, column=29)

submitButton = Button(window, text='submit')
submitButton.grid(row=5, column=30)

window.mainloop()