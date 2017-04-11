from .range import check as _check


def check(tags: dict, keys: list, value: str) -> bool:
    if value is None:
        return True
    for key in keys:
        if _check(tags, key, value):
            return True
    return False
