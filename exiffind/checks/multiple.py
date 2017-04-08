from .single import check as _check


def check(tags: dict, keys: list, value: str) -> bool:
    for key in keys:
        if _check(tags, key, value):
            return True
    return False
