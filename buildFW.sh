#!/bin/bash

rm -rf deps
rm -rf build

mos build --arch esp8266 --local --verbose
