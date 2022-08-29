import sys


def main():
    text_file = sys.argv[1]
    word_count = 0
    char_count = 0
    line_count = 0
    with open(text_file) as f:

        for line in f:
            line_count += 1
            word_count += len(line.split(" "))
            char_count += len(list(line.replace(" ", "")))

    print("average char count: ", str(char_count/line_count))
    print("average word count: ", str(word_count/line_count))
    print("average word length: ", str(char_count / word_count))


if __name__ == "__main__":
        main()