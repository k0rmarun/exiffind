from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF ApertureValue"
    ]
    return _check(tags, keys, args.get("exposure"))