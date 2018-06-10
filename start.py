# -*- coding: utf-8 -*-
# Created by barzarrhey on 2018/6/10

import turtle
import sys
import turtle

class drawSnake():
    def __init__(self):
        self.rad = 40
        self.angle = 80
        self.len = 6
        self.colors = ["red", "orange", "yellow", "green", "cyan", "blue"]
        self.pythonSize = 30
        self.neckRad = self.pythonSize / 2

    def draw(self):
        turtle.setup(1300, 800, 0, 0)
        turtle.penup()
        turtle.goto(-350, 0)
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

if __name__ == '__main__':
    drawsnake = drawSnake()
    sys.exit(drawsnake.draw())