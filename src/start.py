# -*- coding: utf-8 -*-
# Created by barzarrhey on 2018/6/10

import turtle
import sys
import turtle
import time

class drawSnake():
    def __init__(self):
        self.rad = 20
        self.angle = 80
        self.len = 6
        self.colors = ["red", "orange", "yellow", "green", "cyan", "blue"]
        self.pythonSize = 15
        self.neckRad = self.pythonSize / 2

    def draw(self):
        turtle.setup(666, 400)
        turtle.bgcolor("black")
        # turtle.bgpic("logo.JPG")
        turtle.hideturtle()
        turtle.speed(10)
        turtle.penup()
        turtle.goto(-200, 50)
        turtle.pendown()
        turtle.pensize(self.pythonSize)
        turtle.seth(-40)
        for i in range(self.len):
            turtle.color(self.colors[i])
            turtle.circle(self.rad, self.angle)
            turtle.circle(-self.rad, self.angle)

        turtle.color("purple")
        turtle.circle(self.rad, self.angle / 2)
        turtle.fd(self.rad)
        turtle.circle(self.neckRad + 1, 180)
        turtle.fd(self.rad * 2 / 3)
        # turtle.write(s, font=(“font-name”, font_size, ”font_type”))
        turtle.penup()
        turtle.goto(-60,-60)
        turtle.color("pink")
        turtle.pendown()
        turtle.write("让我们吃着小龙虾", align="left", font=("Courier", 20, "bold"))
        time.sleep(1)
        turtle.penup()
        turtle.goto(-60, -80)
        turtle.pendown()
        turtle.write("看着屏幕", align="left", font=("Courier", 20, "bold"))
        time.sleep(1)
        turtle.penup()
        turtle.goto(-60, -100)
        turtle.pendown()
        turtle.write("享受这大千世界与开源不求回报的礼物", align="left", font=("Courier", 20, "bold"))
        time.sleep(1)
        turtle.penup()
        turtle.goto(-60, -120)
        turtle.pendown()
        turtle.write("Forever don't forget the day,", align="left", font=("Courier", 20, "bold"))
        time.sleep(1.5)
        turtle.penup()
        turtle.goto(-60, -140)
        turtle.pendown()
        turtle.write("that someone told you excitedly!", align="left", font=("Courier", 20, "bold"))
        time.sleep(1.5)
        turtle.penup()
        turtle.goto(-60, -160)
        turtle.pendown()
        turtle.write("we needn't rewhell!", align="left", font=("Courier", 20, "bold"))
        time.sleep(2)

if __name__ == '__main__':
    drawsnake = drawSnake()
    drawsnake.draw()