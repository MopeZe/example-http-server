#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     PrepareForPcuFlash.py
# Author:   Michael Glettig
# Date:     01.03.2018
#


import ControlResetBootPins
import time

ControlResetBootPins.setPins(True,True,False,True)
time.sleep(0.1)
ControlResetBootPins.setPins(True,False,False,True)
time.sleep(0.1)

print("PCU ready to flash...")
