import attr, re
from PIL import Image

@attr.s
class ImageSequencer(object):

    """
    Sequences an image into text tokens for colors
    """
    def sequence_image_to_text(self, image):
        print('sequencing...')
        image = image.convert('RGB')
        color_strings = []

        for y in range(0, image.size[1]):
            for x in range(0, image.size[0]):
                r, g, b = image.getpixel((x, y))
                color_token = "{r}-{g}-{b}".format(r=r, g=g, b=b)
                color_strings.append(color_token)

        image_txt = ' '.join(color_strings)

        return image_txt

    def convert_text_to_image(self, text, width, height):
        canvas = (width, height)
        scene = Image.new('RGB', canvas, (100,100,100,0))
        pixel_data = scene.load()

        color_strings = text.split()

        y = -1
        for pixel in range(0, width * height):
            r, g, b = color_strings[pixel].split('-')
            x = pixel % width
            if x == 0:
                y = y+1
            pixel_data[x, y] = (int(r), int(g), int(b))

        return scene
