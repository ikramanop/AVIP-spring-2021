from PIL import Image, ImageDraw
from semitone import semitone
from Otsu_binarization import calculate_threshold
import numpy as np


def calculate_mean(data, threshold):
    data_ft = data.flatten()
    data_1 = data_ft[data_ft >= threshold]
    data_2 = data_ft[data_ft < threshold]
    mean_1 = data_1.mean() if data_1.size > 0 else 0
    mean_2 = data_2.mean() if data_2.size > 0 else 0
    return mean_1, mean_2


def __Eykvel_binarization_helper(x, y, r_step, R_step, old_image, new_image, diff):
    s_window = old_image[y:min(y + r_step, old_image.shape[0]),
                         x:min(x + r_step, old_image.shape[1])]
    l_window = old_image[max(y - R_step // 2 + 1, 0):min(y + R_step // 2 + r_step - 1, old_image.shape[0]),
                         max(x - R_step // 2 + 1, 0):min(x + R_step // 2 + r_step - 1, old_image.shape[1])]

    t = calculate_threshold(l_window)
    m1, m2 = calculate_mean(l_window, t)

    if abs(m1 - m2) >= diff:
        new_image[y:min(y + r_step, old_image.shape[0]),
                  x:min(x + r_step, old_image.shape[1])][s_window > t] = 255
    else:
        center = s_window[s_window.shape[0] // 2, s_window.shape[1] // 2]
        if abs(m1 - center) < abs(m2 - center):
            new_image[y:min(y + r_step, old_image.shape[0]),
                      x:min(x + r_step, old_image.shape[1])] = 255


def Eykvel_binarization(old_image, diff, r_step, R_step):
    semi = semitone(old_image)
    new_image = np.zeros(shape=semi.shape)

    x, y = 0, 0
    while y + r_step <= semi.shape[0]:
        if y % 2 == 0:
            while x + r_step < semi.shape[1]:
                __Eykvel_binarization_helper(
                    x, y, r_step, R_step, semi, new_image, diff)
                x += r_step
        else:
            while x - r_step > 0:
                __Eykvel_binarization_helper(
                    x, y, r_step, R_step, semi, new_image, diff)
                x -= r_step

        y += r_step

    return new_image.astype(np.uint8)


if __name__ == '__main__':
    image_name = 'chess.png'
    method_prefix = 'semitone'
    img_src = Image.open('pictures_src/' + image_name).convert('RGB')
    img_src_arr = np.array(img_src)

    Image.fromarray(Eykvel_binarization(
        img_src_arr, 15, 3, 15), 'L').show()
