from pdf_create.creater import create_pdf
import argparse

if __name__ == "__main__":
    # INPUT_FILE_NAME = "sample/input/sample.pdf"
    # OUTPUT_FILE_NAME = "sample/output/sample.pdf"
    
    parser = argparse.ArgumentParser(description='Translate PDF file')
    parser.add_argument('-i', '--input', help='input file name', required=True, type=str)
    parser.add_argument('-o', '--output', help='output file name', required=True, type=str)
    parser.add_argument('-l', '--lang', help='target language', required=True, type=str, choices=["JA", "ZH", "EN"])
    args = parser.parse_args()
    
    print(f"\nargs: input:{args.input}, output:{args.output}, lang:{args.lang}", end = "\n\n")
    create_pdf(args.input, args.output, args.lang)