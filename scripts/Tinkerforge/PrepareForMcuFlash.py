#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     PrepareForMcuFlash.py
# Author:   Michael Glettig
# Date:     01.03.2018
#


import ControlResetBootPins
import time

ControlResetBootPins.setPins(True,True,True,False)
time.sleep(0.1)
ControlResetBootPins.setPins(False,True,True,False)

print("MCU ready to flash...")
