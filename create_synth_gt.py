import glob
import os
import random
from trdg.generators import GeneratorFromStrings


def create_lines(text_file, lines_to_render, font_folder, output_dir, output_fonts, filter_confusions, check_caps, trdg_params, reverse_lines=False):
    confusions = {
        "‘": "'",
        "´": "'",
        "’": "'",
        "–-": "--",
        "—": "-",
        ". . .": "…",
        "...": "…",
        "‹": "<",
        "›": ">",
        "“": "\""
    }
    lines_start = 0
    with open(text_file) as f_in:
        lines = (line.rstrip() for line in f_in)
        lines = list(line for line in lines if line)  # Non-blank lines in a list
    if reverse_lines:
        lines.reverse()
    lines_length = len(lines)
    print(lines_length)
    font_list = [f for f in sorted(glob.glob(font_folder + '*/' + '*' + '.ttf'))]
    count = 1
    font_dirs = []
    for root, dirs, files in os.walk(r'fonts/50font'):
        if root != "fonts/50font":
            font_dirs.append(root)
    print(font_dirs)
    max_count = int(lines_length / len(font_dirs))
    for font_dir in font_dirs:
        if count >= lines_to_render:
            break
        font_list = [f for f in sorted(glob.glob(font_dir + '/*' + '.ttf'))]
        for line in lines[count:count + max_count]:

            if count >= lines_to_render:
                break
            if len(font_list) > 1:
                font = font_list[random.randint(0, len(font_list) - 1)]
            else:
                font = font_list[0]
            if check_caps and "_CAPS" in font_dir:
                line = line.upper()
            if filter_confusions:
                for key, value in confusions.items():
                    if key in line:
                        line = line.replace(key, value)
            font_size_range = list(range(trdg_params["line_heigth_range"][0], trdg_params["line_heigth_range"][1]))
            generator = GeneratorFromStrings([line], language='en', skewing_angle=trdg_params["skewing_angle"], random_skew=trdg_params["random_skew"], blur=trdg_params["blur"],
                                             random_blur=trdg_params["random_blur"], fonts=[font], size=random.choice(font_size_range),
                                             background_type=trdg_params["background_types"])
            img, lbl = generator.next()

            if line == "" or line == "\n":
                continue
            name = str(count).zfill(len(str(lines_length)))
            img.save(output_dir + name + '.png')
            with open(output_dir + name + '.gt.txt', 'w') as f:
                f.write(lbl)
            if output_fonts:
                with open(output_dir + name + '.font.txt', 'w') as f:
                    f.write(font)
            if count % 100 == 0:
                print("{:.1f}".format(((count / lines_length) * 100)) + '%\t' + font + " | " + lbl)
            count = count + 1

