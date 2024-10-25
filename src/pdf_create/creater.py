import pymupdf
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from translate.translator import translate_text

# idoc をもとに, output_file_name に PDF を作成する
def create_pdf(i_doc: pymupdf.Document, output_file_name: str):
    o_doc = pymupdf.Document()
    for i_page in i_doc:
        new_page = o_doc.new_page(width=i_page.rect.width, height=i_page.rect.height)
        for block in i_page.get_text("blocks"):
            if block[6] == 1:
                print(f"image was skipped. block_num: {block[5]}")
                continue
            translated_text = translate_text(block[4], "JA")
            print(type(translated_text))
            new_page.insert_text(point=(block[0], block[1]),text=translated_text)
        break
    # save
    o_doc.save(output_file_name)
    o_doc.close()
    i_doc.close()

if __name__ == "__main__":
    INPUT_FILE_NAME = "sample/input/sample.pdf"
    OUTPUT_FILE_NAME = "sample/output/sample.pdf"
    i_doc = pymupdf.Document(INPUT_FILE_NAME)
    create_pdf(i_doc, OUTPUT_FILE_NAME)