#!/bin/bash

# rm -rf deps
# rm -rf build
#mkdir deps
#cp -r deps_cesanta_knob/mongoose deps

mos build --arch esp8266 --local --verbose
