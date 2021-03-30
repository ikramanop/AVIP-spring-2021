import numpy as np
from PIL import Image, ImageDraw

from work_1.semitone.semitone import semitone
from work_1.binarization.Otsu_binarization import Otsu_binarization
from work_1.binarization.simple_binarization import simple_binarization


def __sharr_operator_helper(img, new_image, x, y, type):
    z = img[y - 3 // 2:y + 3 // 2 + 1,
            x - 3 // 2:x + 3 // 2 + 1]

    if type == 'x':
        new_image[y, x] = (3*z[0, 0] + 10*z[1, 0] + 3*z[2, 0]) - \
                          (3*z[0, 2] + 10*z[1, 2] + 3*z[2, 2])
    elif type == 'y':
        new_image[y, x] = (3*z[0, 0] + 10*z[0, 1] + 3*z[0, 2]) - \
            (3*z[2, 0] + 10*z[2, 1] + 3*z[2, 2])
    elif type == 'xy':
        new_image[y, x] = abs((3*z[0, 0] + 10*z[1, 0] + 3*z[2, 0]) -
                              (3*z[0, 2] + 10*z[1, 2] + 3*z[2, 2])) + \
            abs((3*z[0, 0] + 10*z[0, 1] + 3*z[0, 2]) -
                (3*z[2, 0] + 10*z[2, 1] + 3*z[2, 2]))
    else:
        raise Exception("Unsupported type")


def sharr_operator(img, type):
    semi = semitone(img)
    new_img = np.zeros(shape=semi.shape)

    x, y = 1, 1
    while y < semi.shape[0] - 1:
        if y % 2 == 0:
            while x + 1 < semi.shape[1] - 1:
                __sharr_operator_helper(semi, new_img, x, y, type)
                x += 1
        else:
            while x - 1 > 1:
                __sharr_operator_helper(semi, new_img, x, y, type)
                x -= 1
        y += 1

    new_img = new_img * 255 / new_img.max()

    if type == 'xy':
        return Otsu_binarization(new_img, semitone_needed=False)
    elif type == 'x' or type == 'y':
        return new_img.astype(np.uint8)
    else:
        raise Exception("Unsupported type")


if __name__ == '__main__':
    image_name = 'integral.jpg'
    method_prefix = 'Sharr_Operator'
    type = 'xy'
    img_src = Image.open(f'pictures_src/{image_name}').convert('RGB')
    img_src_arr = np.array(img_src)

    img = Image.fromarray(
        sharr_operator(
            img=img_src_arr,
            type=type
        ),
        'L'
    )

    img.show()
    # img.save(
    #     f"pictures_results/work_3/{image_name.split('.')[0]}_{method_prefix}_{type}.png"
    # )
