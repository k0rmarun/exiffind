from .multiple import check as _check


def check(tags, args):
    return _check(tags, ["Image Artist", "Image XPAuthor"], args.get("author"))