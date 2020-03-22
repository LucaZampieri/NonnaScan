import glob
import argparse


def main():
    parser = argparse.ArgumentParser(description="Digitalize a bunch of images.")
    parser.add_argument("data", type=str, required=True, help="")
    args = parser.parse_args(["--data", "../../data/nonna_paola/"])
    data_folder = args.data
    files = glob.glob(data_folder + "/*")


if __name__ == "__main__":
    main()
