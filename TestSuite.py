# Requires pytest module

import PIL
from PIL import ImageTk, Image, ImageDraw

from TestInterface import TestInterface

import pytest


class TestSuite:

    def test_line_spacing(self):
        # *** Baseline Parameters ***
        TestInterface.aspect_x = 700
        TestInterface.aspect_y = 400
        TestInterface.line_spacing = 5

        start_x = 10
        start_y = 10
        separation_count = TestInterface.line_spacing

        ls_image = TestInterface.generate_image(TestInterface())

        # *** Test if vertical lines are separated enough ***
        while start_x < TestInterface.aspect_x - 10:
            if ls_image.getpixel((start_x, 11)) == (0, 0, 0):
                assert separation_count >= TestInterface.line_spacing
                separation_count = 0

            start_x += 1
            separation_count += 1

        separation_count = TestInterface.line_spacing
        # *** Test if horizontal lines are separated enough ***
        while start_y < TestInterface.aspect_y - 10:
            if ls_image.getpixel((11, start_y)) == (0, 0, 0):
                assert separation_count >= TestInterface.line_spacing
                separation_count = 0

            start_y += 1
            separation_count += 1




