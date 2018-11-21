#!/bin/bash

# Parse parameters
###############################################################################

COM_PORT=$1

# Flash
###############################################################################

python scripts/Tinkerforge/PrepareForMcuFlash.py

mos flash --port=$COM_PORT --esp-baud-rate=115200 --firmware=build/fw.zip


python scripts/Tinkerforge/McuOnlyActive.py
mos ls --port=$COM_PORT
python scripts/Tinkerforge/EndFlash.py

echo Flash procedure finished
