from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF ExifImageHeight",
        "EXIF ImageHeight",
        "EXIF Height",
        "EXIF ExifImageLength",
        "EXIF ImageLength",
        "EXIF Length"
    ]
    return _check(tags, keys, args.get("height"))