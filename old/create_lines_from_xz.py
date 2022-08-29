import sys
import lzma


def main():
    txt_file = sys.argv[1]
    line_count = int(sys.argv[2])

    lines = create_lines_from_xz(txt_file, line_count)
    print(len(lines))

    with open("corpora_eng.txt", 'w') as f_out:
        f_out.writelines(s + '\n' for s in lines)


def create_lines_from_xz(xz_file, line_count):
    lines = []

    read_lines = 1

    with lzma.open(xz_file, mode='rt', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', ' ')
            if line != "\n" and line != '' and line != ' ':
                lines.append(line)
                print(str(read_lines), ": ", line)
                read_lines += 1
            if read_lines > line_count:
                break
    return lines


if __name__ == "__main__":
    main()
