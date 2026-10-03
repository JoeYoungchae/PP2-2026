'''
작성일: 2026.10.03
작성자: 조영채

문제: 터틀 그래픽에서 각각의 거북이는 객체이다. 2개의 거북이를 생성하여 서로 다른 방향으로 움직이도록 하자.
'''

import turtle

screen = turtle.Screen()
screen.tracer(0)

t1 = turtle.Turtle()
t1.shape("turtle")
t2 = turtle.Turtle()
t2.shape("circle")


def test_prob9():
    t1.fd(100)
    t2.bk(100)

    t1.rt(90)
    t2.lt(90)

    t1.fd(25)
    t2.fd(25)

    t1.lt(90)
    t2.lt(90)

    t1.fd(75)
    t2.fd(75)

if __name__ == "__main__":
    test_prob9()
    turtle.done()