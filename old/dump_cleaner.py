import glob
import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom

def main():
    xml_file = sys.argv[1]

    tree = ET.parse(xml_file)
    ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
    root = tree.getroot()

    children = list(root)
    for child in root.findall("path"):

        weight = ET.Element("weight")
        weight.text = "0"
        enabled = ET.Element("enabled")
        enabled.text = "0"
        group_id = ET.Element("group_id")
        group_id.text = "0"
        child.append(weight)
        child.append(enabled)
        child.append(group_id)

        print(prettify(child))

    tree.write("/home/chaddy/dump_re.xml")




def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

if __name__ == "__main__":
    main()