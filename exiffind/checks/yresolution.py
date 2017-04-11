from .multirange import check as _check


def check(tags, args):
    keys = [
        "Image YResolution"
    ]
    return _check(tags, keys, args.get("yresolution"))