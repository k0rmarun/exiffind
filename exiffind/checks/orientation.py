from .single import check as _check


def check(tags, args):
    return _check(tags, "Image Orientation", args.get("orientation"))