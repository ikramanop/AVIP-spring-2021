from PIL import Image, ImageDraw
import numpy as np


def bilinear_interpolate(im, x, y):
    Ia = im[y0, x0]
    Ib = im[y1, x0]
    Ic = im[y0, x1]
    Id = im[y1, x1]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    return wa*Ia + wb*Ib + wc*Ic + wd*Id


if __name__ == '__main__':
    image_name = 'spiral.png'
    method_prefix = 'Bilinear_resampling'
    scale = 3
    img_src = Image.open('pictures_src/' + image_name).convert('RGB')
    img_src_arr = np.array(img_src)

    width = img_src.size[0]
    height = img_src.size[1]
    new_width = round(scale * img_src.size[0])
    new_height = round(scale * img_src.size[1])

    img_1_array = np.zeros(shape=(new_height, new_width, 4))

    for x in range(new_width):
        for y in range(new_height):
            x0 = np.floor(x).astype(int)
            x1 = x0 + 1
            y0 = np.floor(y).astype(int)
            y1 = y0 + 1

            wa = (x1-x) * (y1-y)
            wb = (x1-x) * (y-y0)
            wc = (x-x0) * (y1-y)
            wd = (x-x0) * (y-y0)

            img_1_array[y, x] = wa*img_src_arr[y0, x0] + wb * \
                img_src_arr[y1, x0] + wc*img_src_arr[y0, x1] + \
                wd*img_src_arr[y1, x1]

    img_1 = Image.fromarray(img_1_array.astype(np.uint8), 'RGB')

    img_1.show()
