#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File:     ControlResetBootPins.py
# Author:   Michael Glettig
# Date:     13.03.2018
#
# Usage:    ControlResetBootPins.setPins(True,True,True,False)

HOST = "localhost"
PORT = 4223
UID_RELAY = "Bym" # Change XYZ to the UID of your Industrial Quad Relay Bricklet

import sys
import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_quad_relay import BrickletIndustrialQuadRelay

def setPins(mcuReset,pcuReset,mcuBoot,pcuBoot):
      ipcon = IPConnection() # Create IP connection
      relay = BrickletIndustrialQuadRelay(UID_RELAY, ipcon) # Create device object

      ipcon.connect(HOST, PORT) # Connect to brickd
      # Don't use device before ipcon is connected

      relayValue = 0

      if mcuReset:
          relayValue |= (1 << 0)

      if mcuBoot:
          relayValue |= (1 << 1)

      if pcuReset:
          relayValue |= (1 << 2)

      if pcuBoot:
          relayValue |= (1 << 3)

      relay.set_value(relayValue)

      ipcon.disconnect()
