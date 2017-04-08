import os
import exifread
import argparse
import sys

import checks as efc

from pprint import pprint

__all__ = ["main", "check"]


def main(args):
    parser = argparse.ArgumentParser(description="Find images by their EXIF data")
    parser.add_argument("dir", help="base dir to search in")
    parser.add_argument("--before", type=str, help="date to be digitized before in format YY-MM-DD")
    parser.add_argument("--after", type=str, help="date to be digitized after in format YY-MM-DD")
    parser.add_argument("--ext", nargs=1, type=str, help="search only for files with $EXT extensions")
    parser.add_argument("--orientation", type=str, choices=["horizontal", "vertical"])
    parser.add_argument("--author", type=str)
    parser.add_argument("--software", type=str)
    parser.add_argument("--width", type=str)
    parser.add_argument("--height", type=str)

    args = dict(parser.parse_args(args).__dict__)
    print(args)
    if "dir" not in args or len(args["dir"]) == 0:
        parser.print_help()
    else:
        for file in check(args):
            print(file)


def check(args: dict):
    tests = (efc.before, efc.after, efc.width, efc.height, efc.author, efc.software, efc.orientation)
    for dir, file in enumerate_files(args.get("dir", "."), args.get("ext", None)):
        with open(os.path.join(dir, file), "rb") as f:
            tags = exifread.process_file(f, details=False)
            if len(tags) is 0:
                continue

            ok = True
            for test in tests:
                ok &= test(tags, args)
                if not ok:
                    break

            if ok is True:
                yield os.path.join(dir, file)


def check_ext(file: str, exts: list = None):
    if exts is None:
        return True
    for ext in exts:
        if ext:
            _ext = file[-len(ext):].lower()
            if _ext == ext.lower():
                return True
    return False


def enumerate_files(dir: str, exts: list = None):
    for root, _, files in os.walk(dir):
        for file in files:
            if check_ext(file, exts):
                yield root, file


if __name__ == '__main__':
    main(sys.argv[1:])
