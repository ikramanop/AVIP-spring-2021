from PIL import Image
import numpy as np


def get_haraliks_matrix(d, diag=False):
    matrix = np.zeros(shape=(256, 256))

    for y in range(d, img_src_arr.shape[0] - d):
        for x in range(d, img_src_arr.shape[1]-d):
            if diag:
                matrix[img_src_arr[y-d, x-d], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y+d, x+d], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y+d, x-d], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y-d, x+d], img_src_arr[y, x]] += 1
            else:
                matrix[img_src_arr[y, x-d], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y, x+d], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y+d, x], img_src_arr[y, x]] += 1
                matrix[img_src_arr[y-d, x], img_src_arr[y, x]] += 1

    return matrix, matrix / np.max(matrix) * 255


def get_haraliks_sigmas(matrix):
    p_j = matrix.sum(axis=0)
    p_i = matrix.sum(axis=1)

    mean_i = (np.arange(1, 257) * p_i).sum()
    mean_j = (np.arange(1, 257) * p_j).sum()

    sigma_i, sigma_j = 0, 0
    for i in range(1, 257):
        sigma_i += (i - mean_j)**2 * p_i[i-1]
        sigma_j += (i - mean_i)**2 * p_j[i-1]

    return sigma_i, sigma_j


if __name__ == "__main__":
    image_name = 'textures/dirt.jpg'

    img_src = Image.open(f'pictures_src/{image_name}').convert('L')
    img_src_arr = np.array(img_src)

    matrix, n_matrix = get_haraliks_matrix(3, diag=True)

    print(get_haraliks_sigmas(matrix))

    Image.fromarray(n_matrix).show()
