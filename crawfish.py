#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by barzarrhey on 2018/6/10

from qtcv import Qtcv
from start import drawSnake
import sys

def main():
    drawsnake = drawSnake()
    drawsnake.draw()
    Qtcv.run()

main()
