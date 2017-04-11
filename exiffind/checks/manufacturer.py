from .single import check as _check


def check(tags, args):
    return _check(tags, "Image Make" , args.get("author"))