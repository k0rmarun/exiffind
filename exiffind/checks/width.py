from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF ExifImageWidth", "EXIF ImageWidth", "EXIF Width"
    ]
    return _check(tags, keys, args.get("width"))