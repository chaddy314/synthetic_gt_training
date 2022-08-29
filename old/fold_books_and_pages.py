import glob
import os
import random
import sys
import shutil

def main():
    book_index = sys.argv[1]
    book_dir = sys.argv[2]
    page_fold_dir = sys.argv[3]
    book_fold_dir = sys.argv[4]
    book_pages = []
    page_files = glob.glob(book_dir + "*.bin.png")
    page_files.sort()
    #print(page_files)
    with open(book_index) as f:
        book_pages = f.readlines()

    book_dict = {}
    for book in book_pages:
        #6
        book_dict[book] = book[:6]
    page_dict = {}
    for book, page in zip(book_pages, page_files):
        #print(book.replace("\n", "") + " =: " + page)
        page_dict[page] = book_dict[book]

    book_list = []
    book_index = {}
    for key, value in page_dict.items():
        #print(value + " =: " + key)
        if value not in book_list:
            book_list.append(value)
            book_index[value] = []
        book_index[value].append(key)

    for key in book_index.keys():
        print(key + " =: " + str(book_index[key]))
    #print(book_list)

    random.shuffle(page_files)
    page_folds = chunks(page_files, 5)
    k = 0
    #for fold in page_folds:
    #    for file in page_files:
    #        fold_dir_eval = page_fold_dir + "fold_" + str(k) + "/eval/"
    #        fold_dir_train = page_fold_dir + "fold_" + str(k) + "/train/"
    #        if file in fold:
    #            dest = file.replace(book_dir, fold_dir_eval)
    #        else:
    #            dest = file.replace(book_dir, fold_dir_train)
    #        os.makedirs(os.path.dirname(dest), exist_ok=True)
    #        shutil.copy(file, dest)
    #        shutil.copy(file.replace(".bin.png", ".xml"), dest.replace(".bin.png", ".xml"))
    #        shutil.copy(file.replace(".nrm.png", ".xml"), dest.replace(".nrm.png", ".xml"))
    #    k += 1

    random.shuffle(book_list)
    book_folds = chunks(book_list, 5)
    k = 0
    for fold in book_folds:
        print(fold)
        for book in fold:
            for file in page_files:
                fold_dir_eval = book_fold_dir + "fold_" + str(k) + "/eval/"
                fold_dir_train = book_fold_dir + "fold_" + str(k) + "/train/"

                if file in book_index[book]:
                    dest = file.replace(book_dir, fold_dir_eval)
                else:
                    dest = file.replace(book_dir, fold_dir_train)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(file, dest)
                shutil.copy(file.replace(".bin.png", ".xml"), dest.replace(".bin.png", ".xml"))
                shutil.copy(file.replace(".bin.png", ".nrm.png"), dest.replace(".bin.png", ".nrm.png"))
        k += 1


def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]


if __name__ == "__main__":
        main()