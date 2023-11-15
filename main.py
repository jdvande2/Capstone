# ======================================================================================================================
# 2023-2024 California State University San Marcos Capstone Project: Ai Art Generation, version 0.1
# Authors: Josh Vande Berg, Bryce Tuller, Abraham Rosales
# ======================================================================================================================

# AUTHORS NOTE: Pycharm installed packages should be: Pillow, pip, setuptools, wheel

# ** Import statements **
from urllib.request import urlopen

import tkinter
from tkinter import *
from tkinter import ttk

import PIL
from PIL import ImageTk, Image, ImageDraw

import random
from TestInterface import TestInterface

if __name__ == '__main__':
    tkRoot = Tk()
    aiArtGui = TestInterface(tkRoot)
    tkRoot.mainloop()
