import attr, os
from PIL import Image

@attr.s
class ImageNormalizer(object):
    def standardize(self, image_path, width, height):
        canvas = (width, height)
        scene = Image.new('RGB', canvas, (100,100,100))

        image = Image.open(image_path)
        image = image.convert('RGB')

        resize_size = self.get_resized_dimensions(image, width)
        offsets_to_center = self.get_offset_to_center(resize_size, (width, height))
        image= image.resize(resize_size, Image.ANTIALIAS)
        scene.paste(image, offsets_to_center)

        save_file = image_path.replace('data/training/images/raw/', 'data/training/images/cropped_and_reduced/')
        save_path = '/'.join(save_file.split('/')[0:-1])
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        scene.save(save_file)

    def get_offset_to_center(self, size, canvas_size):
        w, h = size
        c_w, c_h = canvas_size

        off_w = int((c_w - w)/2)
        off_h = int((c_h - h)/2)
        return (off_w, off_h)

    def get_resized_dimensions(self, image, width):
        w, h = image.size
        print(w, h)
        if w >  h:
            new_h = width
            new_w = (w * new_h)/h
        else:
            new_w = width
            new_h = (h * new_w)/w

        return (int(new_w), int(new_h))
