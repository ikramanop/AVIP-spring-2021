import sys
sys.path.insert(0, '/Users/l.marder/Documents/Coding/AVIP-spring-2021/work_1')

from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
from math import ceil
from simple_binarization import simple_binarization
import numpy as np


font = TTFont("work_4/fonts/times_kz.ttf")
cmap = font['cmap']
t = cmap.getcmap(3, 1).cmap
s = font.getGlyphSet()
units_per_em = font['head'].unitsPerEm


def get_text_width(text, point_size):
    total = 0
    for c in text:
        if ord(c) in t and t[ord(c)] in s:
            total += s[t[ord(c)]].width
        else:
            total += s['.notdef'].width
    total = total*float(point_size)/units_per_em
    return total


KZ_LETTERS = [
    'А', 'Ә', 'Б', 'В', 'Г', 'Ғ', 'Д', 'Е', 'Ё',
    'Ж', 'З', 'И', 'Й', 'К', 'Қ', 'Л', 'М', 'Н',
    'Ң', 'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ұ',
    'Ү', 'Ф', 'Х', 'Һ', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
    'Ы', 'І', 'Ь', 'Э', 'Ю', 'Я'
]


font = ImageFont.truetype("work_4/fonts/times_kz.ttf", 52)

for i, letter in enumerate(KZ_LETTERS):
    width = get_text_width(letter, 52)

    img = Image.new(mode="RGB", size=(ceil(width), 52), color="white")

    draw = ImageDraw.Draw(img)

    draw.text((0, 0), letter, (0, 0, 0), font=font)

    Image.fromarray(simple_binarization(np.array(img), 75), 'L').save(f"work_4/alphabet/base/{i+1}.png")
