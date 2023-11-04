# ======================================================================================================================
# 2023-2024 California State University San Marcos Capstone Project: Ai Art Generation, version 0.1
# Authors: Josh Vande Berg
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


class FrontEnd:
    def __init__(self, root):
        # **** WINDOW ****
        self.master = root
        self.master.title("Local")
        self.master.geometry("1250x500")
        self.master.configure(background='LightGrey')
        # **** WINDOW ****

        # **** DEFAULTS ****
        # ** text above overall image settings **
        self.overallSettingsLabel = Label(self.master, text="Image settings:")
        self.overallSettingsLabel.configure(background='LightGrey')
        self.overallSettingsLabel.grid(row=0, column=0, padx=20, pady=(20, 0), sticky=W)

        # ** text above generated image **
        self.imageText = Label(self.master, text="Image result:")
        self.imageText.configure(background='LightGrey')
        self.imageText.grid(row=0, column=1, padx=20, pady=(20, 0), sticky=W)

        # *** Aspect Ratios ***
        # ** aspect ratio parameters **
        self.aspect_x = 700  # variable defining scale of generated image from left to right, 700px by default
        self.aspect_y = 400  # variable defining scale of generated image from top to bottom, 400px by default

        def set_aspect(x, y):
            self.aspect_x = x
            self.aspect_y = y
            update_ratio()

        # ** text above aspect ratios **
        self.aspectLabel = Label(self.master, text="Aspect Ratio Selection:")
        self.aspectLabel.configure(background='LightGrey')
        self.aspectLabel.grid(row=1, column=0, padx=20, pady=(0, 0), sticky=NW)

        # ** 3:2 ratio **
        self.aspect3_2Button = Button(self.master, text="3:2", command=lambda: set_aspect(900, 600))
        self.aspect3_2Button.grid(row=1, column=0, padx=23, pady=(20, 0), sticky=NW)

        # ** 6:4 ratio **
        self.aspect6_4Button = Button(self.master, text="6:4", command=lambda: set_aspect(1800, 1200))
        self.aspect6_4Button.grid(row=1, column=0, padx=53, pady=(20, 0), sticky=NW)

        # ** 7:5 ratio **
        self.aspect7_5Button = Button(self.master, text="7:5", command=lambda: set_aspect(2100, 1500))
        self.aspect7_5Button.grid(row=1, column=0, padx=83, pady=(20, 0), sticky=NW)

        # ** 2:3 ratio **
        self.aspect2_3Button = Button(self.master, text="2:3", command=lambda: set_aspect(600, 900))
        self.aspect2_3Button.grid(row=1, column=0, padx=23, pady=(50, 0), sticky=NW)

        # ** 4:6 ratio **
        self.aspect4_6Button = Button(self.master, text="4:6", command=lambda: set_aspect(1200, 1800))
        self.aspect4_6Button.grid(row=1, column=0, padx=53, pady=(50, 0), sticky=NW)

        # ** 5:7 ratio **
        self.aspect5_7Button = Button(self.master, text="5:7", command=lambda: set_aspect(900, 600))
        self.aspect5_7Button.grid(row=1, column=0, padx=83, pady=(50, 0), sticky=NW)

        # ** default ratio **
        self.aspectDefaultButton = Button(self.master, text="Default", command=lambda: set_aspect(700, 400))
        self.aspectDefaultButton.grid(row=1, column=0, padx=40, pady=(80, 0), sticky=NW)

        # ** display ratio **
        self.aspectPresent = Label(self.master)

        def update_ratio():
            self.aspectPresent.destroy()

            self.aspectPresent = Label(self.master, text=str(self.aspect_x) + ":" + str(self.aspect_y) + "px")
            self.aspectPresent.configure(background='LightGrey')
            self.aspectPresent.grid(row=1, column=0, padx=150, pady=(0, 0), sticky=NW)

        update_ratio()  # present default ratio on startup

        # *** Aspect Ratios ***

        self.imagePresent = Label(self.master)

        def create_url_image(url):
            image_accessor = urlopen(url)
            raw = image_accessor.read()
            image_accessor.close()

            self.img = ImageTk.PhotoImage(data=raw)
            self.imagePresent = Label(self.master, image=self.img)
            self.imagePresent.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)

        def delete_image():
            self.imagePresent.destroy()

        def default_url_image():
            delete_image()
            default_image_url = 'https://i.imgur.com/86DUwF5.png'
            create_url_image(default_image_url)

        default_url_image()  # present default image on startup

        def no_image_image():
            delete_image()
            no_image_url = 'https://i.imgur.com/lC0Rslm.jpg'
            create_url_image(no_image_url)

        # **** DEFAULTS ****

        # **** PARAMETERS ****
        # ** text above all parameters *
        self.parameterSliderText = Label(self.master, text="Parameter Configuration:")
        self.parameterSliderText.configure(background='LightGrey')
        self.parameterSliderText.grid(row=0, column=2, padx=0, pady=(20, 0), sticky=W)

        # *** Horizontal Lines ***
        self.hLineSliderText = Label(self.master, text="Number of horizontal lines:")
        self.hLineSliderText.configure(background='LightGrey')
        self.hLineSliderText.grid(row=1, column=2, padx=0, pady=(0, 0), sticky=NW)

        def h_line_get():
            return '{: .2f}'.format(h_line.get())

        def h_line_changed(event):  # event is being used, do not delete argument
            # print(self.hLineDisplay.get())  # print line to console
            self.hLineSliderReading.configure(text=h_line_get())

        h_line = tkinter.IntVar()  # variable defining number of horizontal lines
        self.hLineDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=h_line,
                                      command=h_line_changed)
        self.hLineDisplay.grid(row=1, column=2, padx=3, pady=(20, 0), sticky=NW)

        self.hLineSliderReading = Label(self.master, text=h_line_get())
        self.hLineSliderReading.configure(background='LightGrey')
        self.hLineSliderReading.grid(row=1, column=2, padx=110, pady=(23, 0), sticky=NW)
        # *** Horizontal Lines ***

        # *** Vertical Lines ***
        self.vLineSliderText = Label(self.master, text="Number of vertical lines:")
        self.vLineSliderText.configure(background='LightGrey')
        self.vLineSliderText.grid(row=1, column=2, padx=0, pady=(50, 0), sticky=NW)

        def v_line_get():
            return '{: .2f}'.format(v_line.get())

        def v_line_changed(event):  # event is being used, do not delete argument
            # print(self.vLineDisplay.get()) # print line to console
            self.vLineSliderReading.configure(text=v_line_get())

        v_line = tkinter.IntVar()  # variable defining number of vertical lines
        self.vLineDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=v_line,
                                      command=v_line_changed)
        self.vLineDisplay.grid(row=1, column=2, padx=3, pady=(70, 0), sticky=NW)

        self.vLineSliderReading = Label(self.master, text=v_line_get())
        self.vLineSliderReading.configure(background='LightGrey')
        self.vLineSliderReading.grid(row=1, column=2, padx=110, pady=(73, 0), sticky=NW)
        # *** Vertical Lines ***

        # ** Color Distribution **
        self.cdSliderText = Label(self.master, text="Color Distribution:")
        self.cdSliderText.configure(background='LightGrey')
        self.cdSliderText.grid(row=1, column=2, padx=0, pady=(100, 0), sticky=NW)

        def cd_get():
            return '{: .2f}'.format(color_dist.get())

        def cd_changed(event):
            self.cdSliderReading.configure(text=cd_get())

        color_dist = tkinter.IntVar()
        self.cdDisplay = ttk.Scale(self.master, from_=1, to=10, orient='horizontal', variable=color_dist,
                                   command=cd_changed)
        self.cdDisplay.grid(row=1, column=2, padx=3, pady=(120,0), sticky=NW)

        self.cdSliderReading = Label(self.master, text=cd_get())
        self.cdSliderReading.configure(background='LightGrey')
        self.cdSliderReading.grid(row=1, column=2, padx=110, pady=(123, 0), sticky=NW)

        # *** Line Thickness ***
        # also known as the thicc boi parameter

        self.lsSliderText = Label(self.master, text="Line Thickness:")
        self.lsSliderText.configure(background='LightGrey')
        self.lsSliderText.grid(row=1, column=2, padx=0, pady=(150, 0), sticky=NW)

        def lt_get():
            return '{: .2f}'.format(line_thickness.get())

        def lt_changed(event):
            self.ltSliderReading.configure(text=lt_get())

        line_thickness = tkinter.IntVar()
        self.ltDisplay = ttk.Scale(self.master, from_=0, to=20, orient='horizontal', variable=line_thickness,
                                   command=lt_changed)
        self.ltDisplay.grid(row=1, column=2, padx=3, pady=(170, 0), sticky=NW)

        self.ltSliderReading = Label(self.master, text=lt_get())
        self.ltSliderReading.configure(background='LightGrey')
        self.ltSliderReading.grid(row=1, column=2, padx=110, pady=(173, 0), sticky=NW)

        # *** Line Spacing ***

        self.lsSliderText = Label(self.master, text="Line Spacing:")
        self.lsSliderText.configure(background='LightGrey')
        self.lsSliderText.grid(row=1, column=2, padx=0, pady=(200, 0), sticky=NW)

        def ls_get():
            return '{: .2f}'.format(line_spacing.get())

        def ls_changed(event):
            self.lsSliderReading.configure(text=ls_get())

        line_spacing = tkinter.IntVar()
        self.lsDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=line_spacing,
                                   command=ls_changed)
        self.lsDisplay.grid(row=1, column=2, padx=3, pady=(220, 0), sticky=NW)

        self.lsSliderReading = Label(self.master, text=ls_get())
        self.lsSliderReading.configure(background='LightGrey')
        self.lsSliderReading.grid(row=1, column=2, padx=110, pady=(223, 0), sticky=NW)

        # **** PARAMETERS ****

        # **** NEW IMAGE GENERATION ****

        def preview_image():
            delete_image()
            new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))

            self.photoImageNewImage = ImageTk.PhotoImage(new_image)
            self.imageTest = Label(self.master, image=self.photoImageNewImage)
            self.imageTest.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)

        def generate_image():
            delete_image()
            new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))

            with (new_image as canvas):
                paint = ImageDraw.Draw(canvas)
                # *** Create color list and populate it ***
                # First six colors are colors from Mondrian's original works always
                color_list = [(45, 45, 46), (179, 34, 48), (42, 66, 106), (164, 167, 209), (240, 211, 45), (255, 255,
                                                                                                            255)]
                i = 0
                while i < 4:
                    color_list.append(((random.randrange(0, 255)), (random.randrange(0, 255)),
                                                                 (random.randrange(0, 255))))
                    i += 1

                # *** Generate Lines ***

                paint.line((10, 10, self.aspect_x-10, 10), fill=(0, 0, 0), width=int(float(lt_get())))
                paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                           width=int(float(lt_get())))
                paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 0), width=int(float(lt_get())))
                paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                           width=int(float(lt_get())))

                i = 0
                while i < int(float(h_line_get())):
                    random_pos = random.randrange(10, self.aspect_y - 10)
                    paint.line((10, random_pos, self.aspect_x - 10, random_pos),
                               fill=(0, 0, 0), width=int(float(lt_get())))
                    i += 1
                i = 0
                while i < int(float(v_line_get())):
                    random_pos = random.randrange(10, self.aspect_x - 10)
                    paint.line((random_pos, 10, random_pos, self.aspect_y - 10),
                               fill=(0, 0, 0), width=int(float(lt_get())))
                    i += 1

                # *** Detect Rectangles and apply color ***

                point_x = 10
                point_y = 10

                # Starts top left of image
                while point_x != self.aspect_x - 10 and point_y != self.aspect_y - 10:
                    # Save top left position of rectangle
                    x_1 = point_x
                    y_1 = point_y

                    # Position at bottom left of rectangle
                    point_y += 1
                    while new_image.getpixel((point_x+1, point_y)) != (0, 0, 0):
                        point_y += 1
                    # Position at bottom right of rectangle
                    point_x += 1
                    while new_image.getpixel((point_x, point_y+1)) != (0, 0, 0) and new_image.getpixel(
                            (point_x, point_y-1)) != (0, 0, 0):
                        point_x += 1

                    # Save bottom right position of rectangle
                    x_2 = point_x
                    y_2 = point_y

                    # Fill rectangle with color
                    paint.rectangle((x_1, y_1, x_2, y_2), fill=color_list[random.randrange(0, int(float(cd_get())))],
                                    outline=(0, 0, 0), width=1)

                    # Position back to bottom right of rectangle
                    point_x -= 1
                    while new_image.getpixel((point_x, point_y+1)) != (0, 0, 0) and new_image.getpixel(
                            (point_x, point_y-1)) != (0, 0, 0):
                        point_x -= 1

                    # If at end of rectangle column
                    if point_y == self.aspect_y - 10:
                        # Position bottom right of rectangle
                        point_x += 1
                        while new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and new_image.getpixel(
                                (point_x, point_y - 1)) != (0, 0, 0):
                            point_x += 1
                        # Position at top of next rectangle set
                        while point_y != 10:
                            point_y -= 1
                # i = 1
                # j = 1
                # Generates rectangles/squares and lines based on the line count selected
                """while i < int(float(h_line_get())) or j < int(float(v_line_get())):
                    random_pos_x = random.randrange(1,self.aspect_x)
                    random_pos_y = random.randrange(1,self.aspect_y)
                    random_pos_x_2 = random_pos_x + random.randrange(5,100)
                    random_pos_y_2 = random_pos_y + random.randrange(5, 100)
                    paint.rectangle((random_pos_x, random_pos_y, random_pos_x_2, random_pos_y_2),
                                    fill=color_list[random.randrange(0, int(float(cd_get())))],
                                    outline=(0, 0, 0), width=int(float(lt_get())))

                    if i < int(float(h_line_get())):
                        paint.line((0, random_pos_y, self.aspect_x, random_pos_y), fill=(0, 0, 0),
                                   width=int(float(lt_get())))
                        i += 1
                    if i < int(float(h_line_get())):
                        paint.line((0, random_pos_y_2, self.aspect_x, random_pos_y_2), fill=(0, 0, 0),
                                   width=int(float(lt_get())))
                        i += 1
                    if j < int(float(v_line_get())):
                        paint.line((random_pos_x, 0, random_pos_x, self.aspect_y), fill=(0, 0, 0),
                                   width=int(float(lt_get())))
                        j += 1
                    if j < int(float(v_line_get())):
                        paint.line((random_pos_x_2, 0, random_pos_x_2, self.aspect_y), fill=(0, 0, 0),
                                   width=int(float(lt_get())))
                        j += 1
"""
            self.photoImageNewImage = ImageTk.PhotoImage(new_image)
            self.imageTest = Label(self.master, image=self.photoImageNewImage)
            self.imageTest.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)

        # ** Generate Button **
        self.generateButton = Button(self.master, text="Generate", command=generate_image)
        self.generateButton.grid(row=1, column=2, padx=0, pady=(0, 0), sticky=SW)

        # ** Reset Button **
        self.resetButton = Button(self.master, text="Reset Image", command=no_image_image)
        self.resetButton.grid(row=1, column=2, padx=65, pady=(0, 0), sticky=SW)

        # **** NEW IMAGE GENERATION ****


if __name__ == '__main__':
    tkRoot = Tk()
    aiArtGui = FrontEnd(tkRoot)
    tkRoot.mainloop()
