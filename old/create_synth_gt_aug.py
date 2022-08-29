import glob
import os
import random
import sys
import argparse
import time
import re
import requests
from trdg.generators import GeneratorFromStrings
from trdg.generators import GeneratorFromWikipedia
from bs4 import BeautifulSoup


def main():
    lines = []
    lines_start = 0
    if sys.argv[4]:
        lines_start = int(sys.argv[4])
    with open(sys.argv[3]) as f_in:
        lines = (line.rstrip() for line in f_in)
        lines = list(line for line in lines if line)  # Non-blank lines in a list
    lines_length = len(lines)
    print(str(lines_length))
    print(str(1234).zfill(len(str(len(lines)))))
    font_list = [f for f in sorted(glob.glob('fonts/50font/*/' + '*' + '.ttf'))]
    print("fonts: " + str(len(font_list)))
    max_count = 5000
    max_count = int(sys.argv[2])
    # random_start = random.randrange(0, lines_length - max_count, 1)
    # lines = lines[random_start:(random_start+max_count)]
    lines = lines[lines_start:lines_start + max_count]
    # generator = GeneratorFromStrings(lines, language='en', skewing_angle=0, random_skew=False, blur=0,
    #                                  random_blur=False, fonts=font_list, size=48)

    if max_count > lines_length:
        max_count = lines_length
    count = 1

    output_dir = "test/"
    output_dir = sys.argv[1]
    # output_dir = sys.argv[1]
    # for img, lbl in generator:
    #     if count > max_count:
    #         break
    #     name = str(count).zfill(len(str(lines_length)))
    #     img.save(output_dir + name + '.png')
    #     with open(output_dir + name + '.gt.txt', 'w') as f:
    #         f.write(lbl)
    #     print("{:.1f}".format(((count/max_count)*100)) + '%\t' + lbl)
    #     count = count + 1

    for line in lines:
        font = font_list[random.randint(0, len(font_list) - 1)]
        # TEST AREA BEGIN
        #font = font_list.pop()
        # TEST ARE END
        generator = GeneratorFromStrings([line], language='en', skewing_angle=1, random_skew=True, blur=1,
                                         random_blur=True, fonts=[font], size=48, distorsion_type=3)
        img, lbl = generator.next()

        if count > max_count:
            break
        if line == "" or line == "\n":
            continue
        name = str(count).zfill(len(str(lines_length)))
        img.save(output_dir + name + '.png')
        with open(output_dir + name + '.gt.txt', 'w') as f:
            f.write(lbl)
        with open(output_dir + name + '.font.txt', 'w') as f:
            f.write(font)
        print("{:.1f}".format(((count / max_count) * 100)) + '%\t' + lbl)
        count = count + 1


if __name__ == "__main__":
    main()
