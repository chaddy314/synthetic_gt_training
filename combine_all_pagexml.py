from lxml import etree
import os
import sys
import glob
from pathlib import Path

def main():
    clean_dir = sys.argv[1]

    clean_gt_files = glob.glob(clean_dir + "*" + ".gt.xml")
    voting_pred_files = glob.glob(clean_dir + "*" + ".pred98.xml")
    clean_pred_files = glob.glob(clean_dir + "*" + ".pred81.xml")

    clean_gt_map = {}
    for file in clean_gt_files:
        clean_gt_map[os.path.basename(file).split('.')[0]] = file

    voting_pred_map = {}
    for file in voting_pred_files:
        voting_pred_map[os.path.basename(file).split('.')[0]] = file

    clean_pred_map = {}
    for file in clean_pred_files:
        clean_pred_map[os.path.basename(file).split('.')[0]] = file

    # pages
    page_pred_files = glob.glob(clean_dir + "*" + ".pred84.xml")
    page_pred_map = {}
    for file in page_pred_files:
        page_pred_map[os.path.basename(file).split('.')[0]] = file

    synth_page_pred_files = glob.glob(clean_dir + "*" + ".pred85.xml")
    synth_page_pred_map = {}
    for file in synth_page_pred_files:
        synth_page_pred_map[os.path.basename(file).split('.')[0]] = file

    # book
    book_pred_files = glob.glob(clean_dir + "*" + ".pred72.xml")
    book_pred_map = {}
    for file in book_pred_files:
        book_pred_map[os.path.basename(file).split('.')[0]] = file

    synth_book_pred_files = glob.glob(clean_dir + "*" + ".pred70.xml")
    synth_book_pred_map = {}
    for file in synth_book_pred_files:
        synth_book_pred_map[os.path.basename(file).split('.')[0]] = file

    print(len(clean_gt_map.items()))
    print(len(voting_pred_map.items()))
    print(len(clean_pred_map.items()))
    print(len(page_pred_map.items()))
    print(len(synth_page_pred_map.items()))
    print(len(book_pred_map.items()))
    print(len(synth_book_pred_map.items()))



    for key in clean_gt_map.keys():
        gt_xml = etree.parse(clean_gt_map[key])
        gt_root = gt_xml.getroot()
        voting_pred_root = etree.parse(voting_pred_map[key]).getroot()
        clean_pred_root = etree.parse(clean_pred_map[key]).getroot()
        page_pred_root = etree.parse(page_pred_map[key]).getroot()
        synth_page_pred_root = etree.parse(synth_page_pred_map[key]).getroot()
        book_pred_root = etree.parse(book_pred_map[key]).getroot()
        synth_book_pred_root = etree.parse(synth_book_pred_map[key]).getroot()

        voting_pred_lines = voting_pred_root.findall(".//{*}TextLine")
        clean_pred_lines = clean_pred_root.findall(".//{*}TextLine")
        page_pred_lines = page_pred_root.findall(".//{*}TextLine")
        synth_page_pred_lines = synth_page_pred_root.findall(".//{*}TextLine")
        book_pred_lines = book_pred_root.findall(".//{*}TextLine")
        synth_book_pred_lines = synth_book_pred_root.findall(".//{*}TextLine")

        gt_lines = gt_root.findall(".//{*}TextLine")

        for clean_gt_line in gt_lines:
            line_id = clean_gt_line.attrib["id"]
            voting_pred_line = voting_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')
            clean_pred_line = clean_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')
            page_pred_line = page_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')
            synth_page_pred_line = synth_page_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')
            book_pred_line = book_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')
            synth_book_pred_line = synth_book_pred_root.find('.//{*}TextLine[@id="' + line_id + '"]')

            gt_text = clean_gt_line.find(".//{*}TextEquiv")

            voting_pred_text = voting_pred_line.find('./{*}TextEquiv[@index="0"]')
            voting_pred_text.attrib["index"] = "1"
            clean_pred_text = clean_pred_line.find('./{*}TextEquiv[@index="0"]')
            clean_pred_text.attrib["index"] = "2"
            page_pred_text = page_pred_line.find('./{*}TextEquiv[@index="0"]')
            page_pred_text.attrib["index"] = "3"
            synth_page_pred_text = synth_page_pred_line.find('./{*}TextEquiv[@index="0"]')
            synth_page_pred_text.attrib["index"] = "4"
            book_pred_text = book_pred_line.find('./{*}TextEquiv[@index="0"]')
            book_pred_text.attrib["index"] = "5"
            synth_book_pred_text = synth_book_pred_line.find('./{*}TextEquiv[@index="0"]')
            synth_book_pred_text.attrib["index"] = "6"

            if gt_text is not None \
                    and voting_pred_text is not None \
                    and clean_pred_text is not None \
                    and page_pred_text is not None \
                    and synth_page_pred_text is not None \
                    and book_pred_text is not None \
                    and synth_book_pred_text is not None:

                clean_gt_line.append(voting_pred_text)
                clean_gt_line.append(clean_pred_text)
                clean_gt_line.append(page_pred_text)
                clean_gt_line.append(synth_page_pred_text)
                clean_gt_line.append(book_pred_text)
                clean_gt_line.append(synth_book_pred_text)
            else:
                print(gt_text)
                print(voting_pred_text)
                print(clean_pred_text)
                print(page_pred_text)
                print(synth_page_pred_text)
                print(book_pred_text)
                print(synth_book_pred_text)
                print(line_id)
                print(clean_gt_map[key])

        gt_xml.write(clean_gt_map[key].replace(".gt.xml", ".xml"))


if __name__ == "__main__":
    main()
