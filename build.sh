#! /usr/bin/env bash

pyinstaller -w --onefile clock.py
pyinstaller -w --onefile dice.py
pyinstaller -c --onefile randgame.py