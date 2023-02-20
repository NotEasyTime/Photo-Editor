from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from PIL import Image, ImageFilter
import numpy as np
import sys


root = Tk()

list1 = []
list2 = []
list3 = ()
list4 = []
list5 = []

img1pxl = []
img2pxl = []

np.set_printoptions(threshold=sys.maxsize)

def openFile():
    filename = fd.askopenfilename()
    print(filename)
    # Create a photoimage object of the image in the path
    global image1
    image1 = Image.open(filename)
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.pack()

    width = image1.width
    height = image1.height

   
    for i in range(height):
        temp = []
        for j in range(width):
            cor = x, y = j, i
            pixel = image1.getpixel(cor)
            temp.append(pixel)
        img1pxl.append(temp)

    
def make_image(li):

    array = np.array(li, dtype=np.uint8)
    print(array)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')
    new_image.show()

def blur():
    global im2
    im2 = image1.filter(ImageFilter.GaussianBlur(radius = 5))

    test1 = ImageTk.PhotoImage(im2)

    label2 = Label(image=test1)
    label2.image = test1
    label2.pack()

    global width
    global height
    width = im2.width
    height = im2.height

    for i in range(height):
        temp = []
        for j in range(width):
            cor = x, y = j, i
            pixel = im2.getpixel(cor)
            temp.append(pixel)
        img2pxl.append(temp)
    


def subtraction():
    for i in range(height):
        list3 = []
        list4 = []
        x = img1pxl[i]
        y = img2pxl[i]

        for j in range(width):
            list3 = ()
            x1 = x[j]
            y1 = y[j]
            
            for k in range(3):
                x2 = x1[k]
                y2 = y1[k]
                z = x2 - y2

                if z < 0:
                    list3 = list3 + (0,)
                else:
                    list3 = list3 + (z,)
            list4.append(list3)
        list5.append(list4)
    make_image(list5)


frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)


    
B = Button(frame, text ="Blur", command=blur)
B.grid(row=0, column=1, sticky="we")

A = Button(frame, text ="Subtraction", command=subtraction)
A.grid(row=0,column=2, sticky="we")

C = Button(frame, text ="Import", command=openFile)
C.grid(row=0,column=0, sticky="we")

frame.pack()


cor = x, y = 100, 200
#print(image1.getpixel(cor))



# Position image




root.mainloop()