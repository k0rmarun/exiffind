from .multirange import check as _check


def check(tags, args):
    keys = [
        "EXIF ExposureTime"
    ]
    return _check(tags, keys, args.get("exposure"))