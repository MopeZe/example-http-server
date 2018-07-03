#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     EndFlash.py
# Author:   Michael Glettig
# Date:     01.03.2018
#


import ControlResetBootPins
import time

ControlResetBootPins.setPins(True,True,False,False)
time.sleep(0.1)
ControlResetBootPins.setPins(False,False,False,False)
