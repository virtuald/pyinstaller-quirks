#!/bin/bash

cd `dirname $0`

rm -rf build
rm -rf dist
rm *.spec

pyinstaller imp_quirk.py
pyinstaller loader_quirk.py 