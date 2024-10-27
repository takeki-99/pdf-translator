import pymupdf
import sys
import os
from tqdm import tqdm
import tempfile
import shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from translate.translator import translate_text

def get_font_name(lang: str) -> str:
    if lang == "JA":
        return "japan-s"
    if lang == "ZH":
        return "china-ts"
    return "Helvetica"

def remove_newline(text: str) -> str:
    return text.replace("\n", " ")

# main function
def create_pdf(input_file_name: str, output_file_name: str, lang: str):
    with tempfile.NamedTemporaryFile() as tmp:
        shutil.copy(input_file_name, tmp.name)
        translate_pdf(tmp.name, output_file_name, lang)

def translate_pdf(tmp_file_name: str, output_file_name: str, lang: str):
    doc = pymupdf.open(tmp_file_name)
    font_name = get_font_name(lang)
    try:
        for page in tqdm(doc, desc="page"):
            # text
            for block in tqdm(page.get_text("blocks", sort=True), desc="block"):
                block_type = block[-1]
                if block_type != 0:
                    print("block_type is not 0. skip")
                    continue
                x_0, y_0, x_1, y_1, text, block_num, block_type = block
                # remove newline
                text = remove_newline(text)

                translated_text = "comment out next line when debugging"
                translated_text = translate_text(text, lang)
                page.add_redact_annot((x_0, y_0, x_1, y_1), text=translated_text, cross_out=False, fontname=font_name)

            page.apply_redactions(
                images=pymupdf.PDF_REDACT_IMAGE_NONE,
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
    except KeyboardInterrupt as e:
        print(f"KeyboardInterrupt was raised. {e}")
        doc.close()
        return
    except Exception as e:
        print(f"Unexpected error was raised. {e}")
        doc.close()
        return
    # save
    doc.save(output_file_name)
    doc.close()
    print(f"output file was saved as {output_file_name}", end = "\n\n") 
