# -*- coding:utf-8 -*-
"""
gui module.
"""
#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


# ----------------------------------------------------------------


import pyautogui as ui
import pymsgbox as box


def run():
    # dclick()

    # dclick_ocr()

    # sleep(2)
    # click()

    # screenshot()

    confirm()


def sleep(seconds: int):
    ui.sleep(seconds)


def move(x=None, y=None, duration=0.0):
    ui.moveTo(x, y, duration)


def dclick():
    ui.doubleClick(30, 35, duration=1)


def dclick_ocr():
    pass


def click():
    ui.click(1895, 25)


def screenshot():
    ui.screenshot('pycharm.png')


def confirm():
    rvt = box.confirm('Title', 'Hello', ['Ok', 'Cancel'])
    print(rvt)
