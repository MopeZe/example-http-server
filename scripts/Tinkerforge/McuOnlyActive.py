#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     McuOnlyActive.py
# Author:   Michael Glettig
# Date:     01.03.2018
#


import ControlResetBootPins
import time

ControlResetBootPins.setPins(True,True,True,False)
time.sleep(0.5)
ControlResetBootPins.setPins(False,True,False,False)

print("MCU active, PCU in reset...")
