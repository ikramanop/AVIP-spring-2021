from work_5.symbol_selection import get_symbol_boxes
from PIL import Image
from work_4.calculate_features import calculate_features
import csv
import numpy as np
from math import sqrt


def load_features():
    with open('work_4/out/data.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        result = {}
        for row in reader:
            result[row['letter']] = {
                'rel_weight': float(row['rel_weight']),
                'rel_center': tuple(map(float, row['rel_center'][1:len(row['rel_center'])-1].split(', '))),
                'rel_inertia': tuple(map(float, row['rel_inertia'][1:len(row['rel_inertia'])-1].split(', ')))
            }

        return result


def feature_distance(features_1, features_2):
    return sqrt(
        (features_1['rel_weight'] - features_2['rel_weight'])**2 +
        (features_1['rel_center'][0] - features_2['rel_center'][0])**2 +
        (features_1['rel_center'][1] - features_2['rel_center'][1])**2 +
        (features_1['rel_inertia'][0] - features_2['rel_inertia'][0])**2 +
        (features_1['rel_inertia'][1] - features_2['rel_inertia'][1])**2
    )


def calculate_distance(features_global, features_local):
    result = {}
    for letter, features in features_global.items():
        result[letter] = feature_distance(features_local, features)

    _max = max(result.values())

    new_result = {}
    for letter, distance in result.items():
        new_result[letter] = (_max - distance) / _max

    return new_result


if __name__ == '__main__':
    img_src = Image.open(f'work_5/out/sentence/2.png').convert('L')
    img_src_arr = np.array(img_src)

    img_arr = np.zeros(shape=img_src_arr.shape)
    img_arr[img_src_arr != 255] = 1

    symbols = get_symbol_boxes(img_arr)
    features_global = load_features()

    file = open("work_6/out/data_2.txt", "w+")

    check = False
    for i, (left, right) in enumerate(symbols):
        symbol = img_src_arr[:, left:right]

        features_local = calculate_features(symbol)

        grades = calculate_distance(features_global, features_local)

        file.write(
            f"{i+1}: {dict(sorted(grades.items(), key=lambda item: item[1], reverse=True))}\n")

        letter = max(grades, key=grades.get)

        if letter == 'Ь':
            check = True
            continue

        if check:
            if letter == 'І':
                print('Ы', end=' ')
            else:
                print('Ь ', max(grades, key=grades.get), end=' ')
            check = False
            continue

        print(letter, end=' ')
    print()

    file.close()
