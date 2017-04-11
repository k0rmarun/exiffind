from .multirange import check as _check


def check(tags, args):
    keys = [
        "Image XResolution"
    ]
    return _check(tags, keys, args.get("xresolution"))