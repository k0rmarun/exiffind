import os
import exifread
import argparse
import dateutil.parser as du
import sys


def main(args):
    parser = argparse.ArgumentParser(description="Find images by their EXIF data")
    parser.add_argument("dir", type=str, help="base dir to search in")
    parser.add_argument("--before", type=str, help="date to be digitized before in format YY-MM-DD")
    parser.add_argument("--after", type=str, help="date to be digitized after in format YY-MM-DD")
    parser.add_argument("--ext", nargs=1, type=str, help="search only for files with $EXT extensions")
    parser.add_argument("--orientation", type=str, choices=["horizontal", "vertical"])
    parser.add_argument("--author", type=str)
    parser.add_argument("--software", type=str)

    args = dict(parser.parse_args(args).__dict__)
    check(args)


def check(args: dict):
    for dir, file in enumerate_files(args.get("dir", "."), args.get("ext", None)):
        with open(os.path.join(dir, file), "rb") as f:
            tags = exifread.process_file(f, details=False)
            if len(tags) is 0:
                continue

            ok = True
            ok &= check_daterange(  tags, args.get("before", None), args.get("after", None))
            ok &= check_orientation(tags, args.get("orientation", None))
            ok &= check_author(     tags, args.get("author", None))
            ok &= check_software(   tags, args.get("software", None))
            if ok is True:
                print(os.path.join(dir, file))


def check_ext(file: str, exts: list = None):
    if exts is None:
        return True
    for ext in exts:
        if ext:
            _ext = file[-len(ext):].lower()
            if _ext == ext.lower():
                return True
    return False


def check_daterange(tags, before:str=None, after:str=None):
    def _check(dat):
        if before is not None:
            if dat >= before:
                return False
        if after is not None:
            if dat <= after:
                return False
        return True

    if before is None and after is None:
        return True

    before = du.parse(before) if before is not None else before
    after = du.parse(after) if after is not None else after

    date_args = ("EXIF DateTimeDigitized", "EXIF DateTimeOriginal", "Image DateTime")
    for arg in date_args:
        if arg in tags:
            value = str(tags[arg])
            if not value:
                continue
            if value.count(":") > 3:
                value = value.replace(":", "-", 2)
            value = du.parse(value)
            if value and _check(value):
                return True
    return False


def check_tag(tags: dict, key: str, value: str) -> bool:
    if value is None:
        return True
    if key in tags:
        _value = str(tags[key]).lower()
        if _value.find(value.lower()) > -1:
            return True
    return False


def check_orientation(tags, orientation: str = None):
    return check_tag(tags, "Image Orientation", orientation)


def check_author(tags, author: str = None):
    author_args = ("Image Artist", "Image XPAuthor")
    for arg in author_args:
        if check_tag(tags, arg, author):
            return True
    return False


def check_software(tags, software: str = None):
    return check_tag(tags, "Image Software", software)


def enumerate_files(dir: str, exts: list = None):
    for root, _, files in os.walk(dir):
        for file in files:
            if check_ext(file, exts):
                yield root, file


if __name__ == '__main__':
    main(sys.argv)
