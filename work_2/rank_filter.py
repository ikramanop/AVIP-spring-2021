from PIL import Image
import numpy as np


def __rank_filter_helper(img, new_image, x, y, size, threshold):
    aperture = img[max(y - size // 2, 0):min(y + size // 2 + 1, img.shape[0]),
                   max(x - size // 2, 0):min(x + size // 2 + 1, img.shape[1])]

    ones = (aperture == 255).sum()

    if ones >= threshold:
        new_image[y, x] = 255


def rank_filter(img, size, threshold):
    if size % 2 == 0:
        raise Exception("Only even size of aperture is supported")

    new_img = np.zeros(shape=img.shape)

    x, y = 0, 0
    while y + size <= img.shape[0]:
        if y % 2 == 0:
            while x + 1 < img.shape[1]:
                __rank_filter_helper(img, new_img, x, y, size, threshold)
                x += 1
        else:
            while x - 1 > 0:
                __rank_filter_helper(img, new_img, x, y, size, threshold)
                x -= 1

        y += 1

    return new_img.astype(np.uint8)


if __name__ == '__main__':
    image_name = 'nando_binary.png'
    method_prefix = 'rank'
    img_src = Image.open('pictures_src/' + image_name).convert('L')
    img_src_arr = np.array(img_src)

    for i in range(1, 10):
        Image.fromarray(
            rank_filter(
                img=img_src_arr,
                size=3,
                threshold=i
            ),
            'L'
        ).save(f"pictures_results/work_2/{image_name.split('_')[0]}/{i}_of_9.png")
