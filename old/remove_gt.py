import glob
import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom


def main():
    xml_files = sys.argv[1]


    print(xml_files)
    for xml_file in glob.glob(xml_files + "*.gt.xml"):
        ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
        tree = ET.parse(xml_file)
        ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
        root = tree.getroot()
        for el in root.find("{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Page").iter():

            if el.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextRegion":
                parent_map = {c: p for p in el.iter() for c in p}
                for line in el.iter():
                    if line.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextEquiv":
                        if "index" not in line.attrib or line.attrib["index"] != "1":
                            parent_map[line].remove(line)
                        elif line.attrib["index"] == "1":
                            line.attrib["index"] = "0"

        tree.write(xml_file)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

if __name__ == "__main__":
    main()