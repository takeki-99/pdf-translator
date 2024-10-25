import pymupdf

INPUT_FILE = './sample/input/sample.pdf'

doc = pymupdf.open(INPUT_FILE)

for page in doc:
    print(page.get_text("blocks", sort=True))
    
