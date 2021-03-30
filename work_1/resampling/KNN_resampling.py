from PIL import Image, ImageDraw
import numpy as np


def KNN_resampling(old_image, scale):
    width = old_image.shape[1]
    height = old_image.shape[0]
    new_width = round(scale * width)
    new_height = round(scale * height)

    new_image = np.zeros(shape=(new_height, new_width, old_image.shape[2]))

    for x in range(new_width):
        for y in range(new_height):
            src_x = min(
                int(round(float(x) / float(new_width) * float(width))), width - 1)
            src_y = min(
                int(round(float(y) / float(new_height) * float(height))), height - 1)

            new_image[y, x] = old_image[src_y, src_x]

    return new_image


if __name__ == '__main__':
    image_name = 'spiral.png'
    method_prefix = 'KNN_resampling'
    img_src = Image.open('pictures_src/' + image_name).convert('RGB')
    img_src_arr = np.array(img_src)

    img_1_array = KNN_resampling(img_src_arr, 3)
    img_2_array = KNN_resampling(img_1_array, 1/4)
    
    Image.fromarray(img_2_array.astype(np.uint8), 'RGB').show()
