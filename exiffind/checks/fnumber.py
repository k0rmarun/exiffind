from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF FNumber"
    ]
    return _check(tags, keys, args.get("fnumber"))