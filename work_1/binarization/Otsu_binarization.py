from PIL import Image
from work_1.semitone.semitone import semitone
import numpy as np


def calculate_threshold(image):
    bins = np.arange(image.min() - 1, image.max() + 1)
    hist, base = np.histogram(image, bins=bins, density=True)
    base = base[1:].astype(np.uint8)

    w0_raw = np.cumsum(hist)
    w1_raw = np.ones(shape=w0_raw.shape) - w0_raw
    t_rank = 0
    i_max = 0
    for i, (w0, w1) in enumerate(zip(w0_raw, w1_raw)):
        m0 = np.sum(base[:i] * hist[:i] / w0)
        m1 = np.sum(base[i + 1:] * hist[i + 1:] / w1)
        d0 = np.sum(hist[:i] * (base[:i] - m0)**2)
        d1 = np.sum(hist[i + 1:] * (base[i + 1:] - m1)**2)
        d_all = w0 * d0 + w1 * d1
        d_class = w0 * w1 * (m0 - m1)**2
        if d_all == 0:
            i_max = i
            break
        if d_class / d_all > t_rank:
            t_rank = d_class / d_all
            i_max = i

    return base[i_max]


def Otsu_binarization(old_image, semitone_needed=True):
    if semitone_needed:
        semi = semitone(old_image)
    else:
        semi = old_image

    new_image = np.zeros(shape=semi.shape)

    t = calculate_threshold(semi)

    new_image[semi > t] = 255

    return new_image.astype(np.uint8)


if __name__ == '__main__':
    image_name = 'kiwi.jpg'
    method_prefix = 'Otsu_binarization'
    img_src = Image.open('pictures_src/' + image_name).convert('RGB')
    img_src_arr = np.array(img_src)

    Image.fromarray(Otsu_binarization(
        img_src_arr), 'L').show()
