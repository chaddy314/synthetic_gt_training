import sys
import random
from create_lines_from_wikipedia import split_list
from create_lines_from_txt import  create_lines_from_txt
import random

def main():
    txt_1 = sys.argv[1]
    txt_2 = sys.argv[2]
    line_count_1 = int(sys.argv[3])
    line_count_2 = int(sys.argv[4])
    lang = sys.argv[5]

    lines_1 = create_lines_from_txt(txt_1, line_count_1, 5, 13)
    lines_2 = create_lines_from_txt(txt_2, line_count_2, 5, 13)

    lines = lines_1 + lines_2

    print(len(lines))
    random.shuffle(lines)

    with open("corpora_training_" + lang + "_25k.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[:31250])


if __name__ == "__main__":
    main()
