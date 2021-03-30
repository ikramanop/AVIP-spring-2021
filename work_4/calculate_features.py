from PIL import Image, ImageDraw
import numpy as np
import csv
from static import KZ_LETTERS


def calculate_features(img, letter):
    img_b = np.zeros(shape=img.shape)

    img_b[img != 255] = 1

    weight = img_b.sum()
    rel_weight = weight / img_b.shape[0] * img_b.shape[1]

    x_avg = 0
    for x, column in enumerate(img_b.T):
        x_avg += sum((x + 1) * column)
    rel_x_avg = (x_avg-1)/(weight-1)

    y_avg = 0
    for y, row in enumerate(img_b):
        y_avg += sum((y + 1) * row)
    rel_y_avg = (y_avg-1)/(weight-1)

    iner_x = 0
    for y, row in enumerate(img_b):
        iner_x += sum((y + 1 - y_avg)**2 * row)
    rel_iner_x = iner_x/(img_b.shape[0]**2 + img_b.shape[1]**2)

    iner_y = 0
    for x, column in enumerate(img_b.T):
        iner_y += sum((x + 1 - x_avg)**2 * column)
    rel_iner_y = iner_y/(img_b.shape[0]**2 + img_b.shape[1]**2)

    return {
        'letter': letter,
        'weight': weight,
        'rel_weight': rel_weight,
        'center': (x_avg, y_avg),
        'rel_center': (rel_x_avg, rel_y_avg),
        'inertia': (iner_x, iner_y),
        'rel_inertia': (rel_iner_x, rel_iner_y)
    }


if __name__ == '__main__':
    method_prefix = 'Image_Features'

    with open('work_4/out/data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['letter', 'weight', 'rel_weight', 'center',
                                                     'rel_center', 'inertia', 'rel_inertia'])
        writer.writeheader()

        for i, letter in enumerate(KZ_LETTERS):
            img_src = Image.open(f'work_4/alphabet/{i+1}.png').convert('L')
            img_src_arr = np.array(img_src)

            writer.writerow(calculate_features(img_src_arr, letter))
