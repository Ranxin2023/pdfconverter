import sys

from pdf2docx import Converter


def convert():
    if len(sys.argv) != 3:
        return "Incorrect number of arguments", False

    pdf_file = sys.argv[1]
    target_docx = sys.argv[2]

    try:
        cv = Converter(pdf_file)
        cv.convert(docx_filename=target_docx, start=0, end=None)
        cv.close()
        return "Conversion successful", True
    except Exception as e:
        return str(e), False


def main():
    convert_res = convert()
    if not convert_res[1]:
        print("Error occurred:", convert_res[0])
    else:
        print(convert_res[0])


if __name__ == "__main__":
    main()
