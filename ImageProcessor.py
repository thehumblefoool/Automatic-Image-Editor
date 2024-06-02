from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'Automatic-Image-Editor/imgs'
pathOut = '/Automatic-Image-Editor/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Apply a filter (e.g., blur for aesthetic effect)
    img = img.filter(ImageFilter.GaussianBlur(2))

    # Enhance the color    
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.5)

    # Save the edited image
    clean_name = os.path.splitext(filename) [0]

    img.save(f'.{pathOut}/{clean_name}_edited.jpg')