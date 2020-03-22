"""
Might use https://cloud.google.com/vision/docs/handwriting instead
"""
import glob
import argparse
import subprocess
import os

from PIL import Image

# import Image


def main():
    parser = argparse.ArgumentParser(description="Digitalize a bunch of images.")
    parser.add_argument("--data", type=str, default="../../data/nonna_paola/", help="")
    parser.add_argument("-l", "--lang", type=str, default="eng", help="")
    args = parser.parse_args()
    data_folder = args.data
    files = glob.glob(data_folder + "/*.jpeg")

    print("Preprocessing")
    preprocessed_files = []
    for file in files:
        out_file = os.path.dirname(file) + "/../tmp/" + os.path.basename(file)
        print(out_file)
        adapt_dpi(file, out_file, 300)
        preprocessed_files.append(out_file)

    print(f"Analysing {preprocessed_files}")
    processed_files = []
    for file in preprocessed_files:
        file = os.path.abspath(file)
        content = digitalize_file(file, lang=args.lang)
        processed_files.append(content)
    for i, x in enumerate(processed_files):
        print(f"File {i} --- results ---")
        print(x)


def digitalize_file(file_path, lang=""):

    # TODO accept many languages
    language = f"-l {lang}"  # "-l eng" # pass as an argument
    result_file = file_path[: file_path.rfind(".")]

    print(result_file)
    tesseract_cmd = f"tesseract {file_path} {result_file} {language}"

    subprocess.call(tesseract_cmd.split())
    with open(result_file + ".txt", "r") as f:
        content = f.read()
    return content


def adapt_dpi(in_file, out_file, dpi=300):
    im = Image.open(in_file)
    im.save(out_file, dpi=(dpi, dpi))


if __name__ == "__main__":
    main()
