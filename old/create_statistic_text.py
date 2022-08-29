import sys
import csv
import random
from numpy.random import choice


def main():
    csv_path = sys.argv[1]
    output = sys.argv[2]
    line_count = int(sys.argv[3])

    char_dict = {}
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file, quoting=csv.QUOTE_ALL, delimiter=";", escapechar='\\')
        char_dict = dict(reader)

    total_chars = 0
    for value in char_dict.values():
        total_chars += int(value)

    # average char count: 49.04148
    # average word count: 8.50496

    probality_dict = {}
    for key in char_dict.keys():
        probality_dict[key] = int(char_dict[key])/total_chars
        print(int(char_dict[key])/total_chars)

    char_list = list(probality_dict.keys())
    probality_list = list(probality_dict.values())

    lines = []
    draw = random.choices(char_list, probality_list, k=2)
    print(draw)
    for i in range(line_count):
        line = ""
        line_word_count = random.choice(list(range(3, 12)))
        words = []
        for j in range(line_word_count):
            word_char_count = random.choice(list(range(3, 10)))
            chars = [''] * word_char_count
            #draw = choice(char_list, word_char_count, p=probality_list)
            draw = random.choices(char_list, probality_list, k=word_char_count)
            #print(draw)
            ded = ''.join(draw)
            words.append(ded)
        line = ' '.join(words)
        lines.append(line)
    print("total_chars: ", str(total_chars))
   # print("average word count: ", str(word_count/line_count))


    with open(output, 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines)


if __name__ == "__main__":
        main()