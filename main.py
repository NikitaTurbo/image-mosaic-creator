import math
from PIL import Image

SIZE = 10 
NAME = input()
FOLDER_NAME = "dataset"
NUMBER_OF_IMAGES = 14331
IMAGE_EXTENSION = ".jpg"

def mean_color(image):
    image = image.convert("RGB")        
    width, height = image.size
    pixels = list(image.getdata())
    total_pixels = width * height
    r, g, b = [sum(channel) for channel in zip(*pixels)]
    return tuple(value / total_pixels for value in (r, g, b))

def dist(color1, color2):
    return math.sqrt(sum((a - b) ** 2  for a, b in list(zip(color1, color2))))

x = 0
img = Image.open(f"{NAME}{IMAGE_EXTENSION}")
width, height = img.size
number = [0, (width * height) // (SIZE * SIZE)]
mean_colors = {i: mean_color(Image.open(f"{FOLDER_NAME}/{i}{IMAGE_EXTENSION}")) for i in range( (NUMBER_OF_IMAGES + 1))}

while x < width:
    y = 0
    while y < height:
        crop = Image.open(f"{NAME}{IMAGE_EXTENSION}").crop((x, y, x + SIZE, y + SIZE))
    
        mean_color_crop = mean_color(crop)
        ind = min(mean_colors.keys(), key=lambda key: dist(mean_color_crop, mean_colors[key]))

        paste = Image.open(f"{FOLDER_NAME}/{ind}{IMAGE_EXTENSION}").resize((SIZE, SIZE))
        img.paste(paste, (x, y))

        number[0] += 1
        print(*number, sep="/", end="\r")

        y += SIZE

    x += SIZE

img.show()