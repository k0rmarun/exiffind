from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF ISOSpeed", "EXIF ISOSpeedRatings"
    ]
    return _check(tags, keys, args.get("speed"))
