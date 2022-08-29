import glob
import sys
import csv


def main():
    csv_file = sys.argv[1]
    target_dir = sys.argv[2]
    i = 1
    with open(csv_file, newline='') as f:
        reader = csv.reader(f, delimiter=";", quotechar='\"')
        for row in reader:
            if row[0] != "" and row[1] != "" and row[2] != "":
                i_string = str(i).zfill(4)
                with open(target_dir + i_string + ".preda.txt", 'w', encoding='utf-8') as f:
                    f.write(row[0])
                with open(target_dir + i_string + ".gt.txt", 'w', encoding='utf-8') as f:
                    f.write(row[1])
                with open(target_dir + i_string + ".predt.txt", 'w', encoding='utf-8') as f:
                    f.write(row[2])
                i += 1


if __name__ == "__main__":
    main()