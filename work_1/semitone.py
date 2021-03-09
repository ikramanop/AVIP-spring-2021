from PIL import Image, ImageDraw
import numpy as np


def semitone(old_image):
    return (0.3 * old_image[:, :, 0] + 0.59 * old_image[:, :, 1] + 0.11 * old_image[:, :, 2]).astype(np.uint8)


if __name__ == '__main__':
    image_name = 'japan.png'
    method_prefix = 'Semitone'
    img_src = Image.open('pictures_src/' + image_name).convert('RGB')
    img_src_arr = np.array(img_src)

    Image.fromarray(semitone(img_src_arr).astype(np.uint8), 'L').show()
