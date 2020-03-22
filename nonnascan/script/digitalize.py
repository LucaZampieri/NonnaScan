import glob
import argparse
import subprocess
import os


def main():
    parser = argparse.ArgumentParser(description="Digitalize a bunch of images.")
    parser.add_argument("--data", type=str, default="../../data/nonna_paola/", help="")
    parser.add_argument("-l", "--lang", type=str, default="eng", help="")
    args = parser.parse_args()
    data_folder = args.data
    files = glob.glob(data_folder + "/*")
    print(f"Analysing {files}")
    processed_files = []
    for file in files:
        file = os.path.abspath(file)
        processed_files.append(digitalize_file(file, lang=args.lang))
    for i, _ in enumerate(files):
        print(f"File {i} --- results ---")


def digitalize_file(file_path, lang=""):

    # TODO accept many languages
    language = f"-l {lang}"  # "-l eng" # pass as an argument
    result_file = os.path.dirname(file_path) + "/tmp"

    print(result_file)
    tesseract_cmd = f"tesseract {file_path} {result_file} {language}"

    subprocess.call(tesseract_cmd.split())
    with open(result_file + ".txt", "r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    main()
