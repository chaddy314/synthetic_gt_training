import fitz
import sys
import os
import xml.etree.ElementTree as ET



def main():
    pdf_path = sys.argv[1]
    xml_folder = sys.argv[2]
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            # page number is 0 based
            page_no = page.number + 1
            #print("page no: " + str(page.number))
            page_content = page.get_text("text").strip()
            #print(page_content)
            lines = page_content.split("\n")
            lines = list(filter(None, lines))
            xml_path = xml_folder + str(page_no).zfill(4) + ".xml"

            #print(xml_path)
            ET.register_namespace('', "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15")
            tree = ET.parse(xml_path)
            root = tree.getroot()
            #print(root)
            a = root.find('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Page')
            b = a.find('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextRegion')
            #print(a)
            text_lines = b.findall('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextLine')
            if len(text_lines) != len(lines):
                print("something probably went wrong when segmenting")
                print(page_no)
                print("text regions: " + str(len(text_lines)))
                print("lines: " + str(len(lines)))
                print("--------------------------")
                print("\n".join(lines))
                print("--------------------------")
            else:
                for region, line in zip(text_lines, lines):

                    t_eq = ET.Element('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}TextEquiv')
                    t_eq.set('index', "0")
                    unicode = ET.Element('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Unicode')
                    #unicode = t_eq.find('{http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15}Unicode')
                    unicode.text = line.strip()
                    t_eq.append(unicode)
                    region.append(t_eq)
                tree.write(xml_path)


if __name__ == "__main__":
    main()
