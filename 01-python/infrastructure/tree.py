from PIL import Image, ImageDraw
import os
import tkinter
import io

def draw_tree():

    img = Image.open(os. getcwd() + '/images/tree.jpeg')
    img.thumbnail((1200, 800))

    img.show()

    print(img.format)
    print(img.size)
    print(img.palette)
    return

draw_tree()