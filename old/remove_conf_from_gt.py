from lxml import etree
import sys
import glob

def main():
    confusions = {
                    "‘": "'",
                    "´": "'",
                    "’": "'",
                    "`": "'",
                    "–": "-",
                    "—": "-",
                    ". . .": "…",
                    "...": "…",
                    "‹": "<",
                    "›": ">",
                    "“": "\"",
                    "”": "\""
                }
    xml_dir = sys.argv[1]
    target_xml_ext = ".xml"
    xml_files = glob.glob(xml_dir + "*.xml")

    for xml_file in xml_files:
        xml = etree.parse(xml_file)
        root = xml.getroot()
        lines = root.findall(".//{*}TextLine")
        print(len(lines))
        for line in lines:
            if len(line.findall("./{*}TextEquiv")) == 1:
                textEquiv = line.find("./{*}TextEquiv")
                unicode = textEquiv.find("./{*}Unicode")
                if unicode is not None:
                    for key, value in confusions.items():
                        if key in unicode.text:
                            print(unicode.text)
                            unicode.text = unicode.text.replace(key, value)

            elif len(line.findall("./{*}TextEquiv")) > 1:
                print("more than one TextEquiv found")
                print(xml_file)
                print(line)

        xml.write(xml_file)






if __name__ == "__main__":
    main()
