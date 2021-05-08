from math import ceil

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from work_1.binarization.simple_binarization import simple_binarization
from work_4.generate import FontUtil

SENTENCE = "АҒАЙЫНМЕН АЛЫСТАН СЫЙЛАСҚАН ЖАҚСЫ"

if __name__ == '__main__':
    util = FontUtil(font_path="work_4/fonts/times_kz.ttf")
    font = ImageFont.truetype("work_4/fonts/times_kz.ttf", 40)

    width = util.get_text_width(SENTENCE, 40) + 20

    img = Image.new(mode="RGB", size=(ceil(width), 56), color="white")

    draw = ImageDraw.Draw(img)

    draw.text((10, 2), SENTENCE, (0, 0, 0), font=font)

    Image.fromarray(simple_binarization(np.array(img), 120),
                    'L').save(f"work_5/out/sentence/2.png")
