import pymupdf
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from translate.translator import translate_text

def get_font_name(lang: str) -> str:
    if lang == "JA":
        return "japan-s"
    if lang == "ZH":
        return "china-ts"
    return "Helvetica"

# input_file_name をもとに, output_file_name に PDF を作成する
def create_pdf(input_file_name: str, output_file_name: str, lang: str):
    i_doc = pymupdf.Document(input_file_name)
    o_doc = pymupdf.Document()
    try:
        for i_page in i_doc:
            new_page = o_doc.new_page(width=i_page.rect.width, height=i_page.rect.height)
            # text
            for block in i_page.get_text("blocks", sort=True):
                x_0, y_0, x_1, _, text, block_num, block_type = block
                if block_type == 1:
                    print(f"image was skipped. block_num: {block_num}")
                    continue
                # todo font_size
                font_size = 6
                translated_text = translate_text(text, lang, x_1 - x_0, font_size)
                font_name = get_font_name(lang)
                new_page.insert_text(
                    point=(x_0, y_0),
                    text=translated_text,
                    fontname=font_name,
                    fontsize=font_size)
            # todo image
    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt was raised. {e}")
        o_doc.save(output_file_name)
        i_doc.close()
        o_doc.close()
        return
    except Exception as e:
        print(f"Unexpected error was raised. {e}")
        o_doc.save(output_file_name)
        i_doc.close()
        o_doc.close()
        return
    # save
    o_doc.save(output_file_name)
    o_doc.close()
    i_doc.close()
    print(f"output file was saved as {output_file_name}", end="\n\n")
