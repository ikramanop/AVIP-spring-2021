import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

from static import KZ_LETTERS


def write_profile(img, iter, type='x'):
    if type == 'x':
        profile_y = np.sum(img, axis=0)
        profile_x = np.arange(
            start=1, stop=img.shape[1] + 1).astype(int)

        plt.bar(x=profile_x, height=profile_y, width=0.9)

        plt.ylim(0, 52)

    elif type == 'y':
        profile_y = np.sum(img, axis=1)
        profile_x = np.arange(
            start=1, stop=img.shape[0] + 1).astype(int)

        plt.barh(y=profile_x, width=profile_y, height=0.9)

        plt.ylim(52, 0)

    else:
        raise Exception('Unsupported profile')

    plt.xlim(0, 55)

    plt.savefig(f'work_4/out/profile/{type}/{iter+1}.png')
    plt.clf()


if __name__ == '__main__':
    method_prefix = 'Image_Profiles'

    for i, letter in enumerate(KZ_LETTERS):
        img_src = Image.open(f'work_4/alphabet/{i+1}.png').convert('L')
        img_src_arr = np.array(img_src)

        img_src_arr[img_src_arr == 0] = 1
        img_src_arr[img_src_arr == 255] = 0

        write_profile(img_src_arr, i, type='x')
