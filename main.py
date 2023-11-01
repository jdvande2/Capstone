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

        # ** Future Parameters **
        self.renameMe = Label(self.master, text="Add new parameters here later:")
        self.renameMe.configure(background='LightGrey')
        self.renameMe.grid(row=1, column=2, padx=0, pady=(100, 0), sticky=NW)

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

            with new_image as canvas:
                paint = ImageDraw.Draw(canvas)
                i = 1
                while i < int(float(h_line_get())):
                    paint.line((self.aspect_x / i, 0, self.aspect_x / i, self.aspect_y), fill=128)
                    i += 1
                j = 1
                while j < int(float(v_line_get())):
                    paint.line((0, self.aspect_y / j, self.aspect_x, self.aspect_y / j), fill=128)
                    j += 1

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
