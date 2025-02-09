import PIL
from PIL import Image

image1 = PIL.Image.open("/home/tejash/Downloads/01.jpeg")
image2 = PIL.Image.open("/home/tejash/Downloads/images.jpeg")

width, height = image1.size
width1, height2 = image2.size

print(f'{width} X {height}')
print(f'{width1} X {height2}')
