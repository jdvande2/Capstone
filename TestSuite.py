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
        # Line Spacing Default
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

    def test_line_thickness(self):
        # *** Baseline Parameters ***
        TestInterface.aspect_x = 700
        TestInterface.aspect_y = 400
        # Line Thickness Default
        TestInterface.line_thickness = 5

        start_x = 8
        start_y = 8
        thickness_count = 0
        on_line = False

        lt_image = TestInterface.generate_image(TestInterface())

        # Test if vertical lines are thick enough ***
        while start_x < TestInterface.aspect_x:
            if lt_image.getpixel((start_x, 13)) == (0, 0, 1):
                on_line = True
                thickness_count += 1
            if (lt_image.getpixel((start_x, 13)) != (0, 0, 0) and lt_image.getpixel((start_x, 13)) != (0, 0, 1)) and on_line:
                # Account for line spacing test redraw
                thickness_count += 1
                assert thickness_count == TestInterface.line_thickness
                thickness_count = 0
                on_line = False
            start_x += 1

        thickness_count = 0
        on_line = False

        # Test if horizontal lines are thick enough ***
        while start_y < TestInterface.aspect_y:
            if lt_image.getpixel((13, start_y)) == (0, 0, 1):
                on_line = True
                thickness_count += 1
            if (lt_image.getpixel((13, start_y)) != (0, 0, 0) and lt_image.getpixel((13, start_y)) != (0, 0, 1)) and on_line:
                # Account for line spacing test redraw
                thickness_count += 1
                assert thickness_count == TestInterface.line_thickness
                thickness_count = 0
                on_line = False
            start_y += 1




