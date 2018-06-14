#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by barzarrhey on 2018/6/10

from qtcv import Qtcv
from start import drawSnake
import os

def main():
    # drawsnake = drawSnake()
    # drawsnake.draw()
    # Qtcv.run()
    cmd1 = "python /bin/start.exe"
    cmd2 = "python /bin/qtcv.exe"
    os.system(cmd1)
    os.system(cmd2)


main()
