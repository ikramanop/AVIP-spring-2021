from work_5.text_selection import calculate_profiles
from PIL import Image
from PIL.ImageOps import invert
import numpy as np


def get_symbol_boxes(img):
    profiles = calculate_profiles(img)
    borders = []

    i = 0
    while i < profiles['x'].shape[0]:
        current = profiles['x'][i]
        if current != 0:
            x1, x2 = None, None
            x1 = i
            count = 0
            while profiles['x'][i + count] != 0:
                count += 1
            i += count
            x2 = i
            borders.append((x1, x2))
        i += 1

    return borders


if __name__ == '__main__':
    img_src = Image.open(f'work_5/out/sentence/1.png').convert('L')
    img_src_arr = np.array(img_src)

    img_arr = np.zeros(shape=img_src_arr.shape)
    img_arr[img_src_arr == 0] = 1
    img_arr[img_src_arr == 255] = 0

    for i, (x1, x2) in enumerate(get_symbol_boxes(img_arr)):
        invert(Image.fromarray(img_src_arr[:, x1:x2])).save(
            f"pictures_results/work_5/symbols/{i+1}.png")
