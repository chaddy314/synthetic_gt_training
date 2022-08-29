from lxml import etree
import os
import sys
import glob

def main():
    xml_dir = sys.argv[1]
    pred_xml_ext = sys.argv[2]
    gt_xml_ext = sys.argv[3]
    target_xml_ext = ".xml"
    pred_xml_files = glob.glob(xml_dir + "*" + pred_xml_ext)
    pred_gt_files = glob.glob(xml_dir + "*" + gt_xml_ext)

    if len(pred_gt_files) == len(pred_gt_files):
        for pred_xml_file in pred_xml_files:
            pred_xml = etree.parse(pred_xml_file)
            #gt_xml = etree.parse(pred_xml_file.replace(pred_xml_ext, gt_xml_ext))
            pred_root = pred_xml.getroot()
            gt_root = etree.parse(pred_xml_file.replace(pred_xml_ext, gt_xml_ext)).getroot()
            pred_lines = pred_root.findall(".//{*}TextLine")
            gt_lines = gt_root.findall(".//{*}TextLine")
            for pred_line in pred_lines:
                line_id = pred_line.attrib["id"]
                gt_line = gt_root.find('.//{*}TextLine[@id="' + line_id + '"]')

                pred_text = pred_line.find("./{*}TextEquiv")
                pred_text.attrib["index"] = "1"
                gt_text = gt_line.find(".//{*}TextEquiv")
                if gt_text is not None and pred_text is not None:
                    pred_line.append(gt_text)
                else:
                    print(pred_text)
                    print(gt_text)
                    print(line_id)
                    print(pred_xml_file)

            pred_xml.write(pred_xml_file.replace(pred_xml_ext, target_xml_ext))

    else:
        print("The number of files should be the same")





if __name__ == "__main__":
    main()
