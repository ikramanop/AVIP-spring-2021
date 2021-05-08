from work_1.binarization.simple_binarization import simple_binarization
from work_4.static import KZ_LETTERS
import numpy as np
from math import ceil
from fontTools.ttLib import TTFont
from PIL import Image, ImageFont, ImageDraw


class FontUtil:
    def __init__(self, font_path):
        self.font = TTFont(font_path)
        self.cmap = self.font['cmap']
        self.t = self.cmap.getcmap(3, 1).cmap
        self.s = self.font.getGlyphSet()
        self.units_per_em = self.font['head'].unitsPerEm

    def get_text_width(self, text, point_size):
        total = 0
        for c in text:
            if ord(c) in self.t and self.t[ord(c)] in self.s:
                total += self.s[self.t[ord(c)]].width
            else:
                total += self.s['.notdef'].width
        total = total * float(point_size)/self.units_per_em
        return total


if __name__ == '__main__':
    util = FontUtil(font_path="work_4/fonts/times_kz.ttf")
    font = ImageFont.truetype("work_4/fonts/times_kz.ttf", 52)

    for i, letter in enumerate(KZ_LETTERS):
        width = util.get_text_width(letter, 52)

        img = Image.new(mode="RGB", size=(ceil(width), 52), color="white")

        draw = ImageDraw.Draw(img)

        draw.text((0, 0), letter, (0, 0, 0), font=font)

        Image.fromarray(simple_binarization(np.array(img), 75),
                        'L').save(f"work_4/alphabet/base/{i+1}.png")
