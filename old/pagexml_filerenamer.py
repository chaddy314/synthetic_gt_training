import os, fnmatch, sys


def main():
    directory = sys.argv[1]
    print(directory)
    find = sys.argv[2]
    print(find)
    replace = sys.argv[3]
    print(replace)
    file_pattern = sys.argv[4]
    print(file_pattern)

    find_replace(directory, find, replace, file_pattern)


def find_replace(directory, find, replace, file_pattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, file_pattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)


if __name__ == "__main__":
    main()
