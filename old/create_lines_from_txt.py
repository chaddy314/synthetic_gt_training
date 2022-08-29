import sys
import random
from create_lines_from_wikipedia import split_list

def main():
    txt_file = sys.argv[1]
    line_count = int(sys.argv[2])
    lang = sys.argv[3]

    lines = create_lines_from_txt(txt_file, line_count, 5, 13)
    print(len(lines))

    with open("corpora_training_" + lang + "_10k.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[:10000])

    with open("corpora_training_" + lang + "_25k.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[:25000])

    with open("corpora_training_" + lang + "_50k.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[:50000])

    with open("corpora_test_" + lang + "_10.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[50000:52000])

    with open("corpora_test_" + lang + "_125.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[50000:55000])

    with open("corpora_test_" + lang + "_150.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[50000:60000])

    with open("corpora_eval_" + lang + ".txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines[80000:])


def create_lines_from_txt(txt_file, line_count, min_word, max_word):
    lines = []
    length_range = list(range(min_word, max_word))

    with open(txt_file) as f:
        for line in f:
            line = line.replace('\n', ' ')
            if line == "\n" or line == "":
                continue
            words = line.split(' ')
            new_lines = []
            while len(words) > max_word:
                line_words, words = split_list(words, random.choice(length_range))
                line = " ".join(line_words).rstrip().lstrip()
                if len(line) > 5 and line.count('=') < 3 and "http" not in line:
                    new_lines.append(line)
            #print(new_lines)
            lines.extend(new_lines)
            if len(lines) > line_count:
                break
    return lines[0:line_count]


if __name__ == "__main__":
    main()
