def draw_road():
    print("road not found")
    return


from PIL import Image

# Read image
img = Image.open('road.jpg')

# Output Images
img.show()

# prints format of image
print(img.format)

# prints mode of image
print(img.mode)