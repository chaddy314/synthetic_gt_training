import glob
import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom


def main():
    xml_files = sys.argv[1]


    print(xml_files)
    for xml_file in glob.glob(xml_files + "*.xml"):
        ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
        tree = ET.parse(xml_file)
        ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
        root = tree.getroot()
        print(root.findall("Glyph"))
        for el in root.find("{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Page").iter():

            if el.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextRegion":
                parent_map = {c: p for p in el.iter() for c in p}
                for line in el.iter():
                    if line.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextEquiv":
                        if "index" not in line.attrib or line.attrib["index"] != "0":
                            parent_map[line].remove(line)
                    elif line.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Word" or line.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Glyph":
                        parent_map[line].remove(line)

                    if line.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextLine":
                        for word in line.iter():
                            if word.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Word" or word.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Glyph":
                                parent_map[word].remove(word)


                #     for
                #     if "index" in child.attrib and child.attrib["index"] == "0":
                #         # print("fuck")
                #         pass
                #     else:
                #
                #         # uses textline instead textEquiv
                #
                #         # print(child)
                #         # print(xml_file)
                #         # print(prettify(child))
                #         if child.tag == "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Word":
                #             print("wow")
                #         line.remove(child)
                # else:
                #     line.remove(child)

        tree.write(xml_file)
        #print(xml_file)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

if __name__ == "__main__":
    main()