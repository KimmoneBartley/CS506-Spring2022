
from PIL import Image, ImageDraw
import os
import tkinter
import io

def draw_power_plant():
    # power_image = Image.new('RGB', (500, 300), (128, 128, 128))
    # draw = ImageDraw.Draw(power_image)
    # draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    # draw.rectangle((300, 200, 500, 400), fill=(60, 90, 50), outline=(255, 255, 255))
    # power_image.save('power_example.png', quality=95)
    # img = Image.open("power_example.png")
    # img.show()

    img = Image.open(os.getcwd() + '/power.jpg')
    img.thumbnail((600, 400))
    img.show()
    return

draw_power_plant()