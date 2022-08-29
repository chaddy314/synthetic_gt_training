import sys
import os
import csv
import lzma


def main():
    text_archive = sys.argv[1]
    csv_file = sys.argv[2]

    glyph_dict = {}
    total = 0
    read_lines = 1
    line_count = 10000000

    with lzma.open(text_archive, mode='rt', encoding='utf-8') as f:
        for line in f:
            if line != "\n" and line != '' and line != ' ':
                chars = list (line)
                for char in chars:
                    if char != " " and char not in glyph_dict.keys():
                        glyph_dict[char] = 1
                        #print(char, ": ", str(glyph_dict[char]))
                        total += 1
                    elif char in glyph_dict.keys():
                        glyph_dict[char] += 1
                        #print(char, ": ", str(glyph_dict[char]))
                        total += 1
                read_lines += 1
            if read_lines > line_count:
                break


    print("total: ", str(total))
    with open(csv_file, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL, delimiter=";", escapechar='\\')
        for key, value in glyph_dict.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    main()