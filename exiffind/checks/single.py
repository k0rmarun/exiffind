def check(tags: dict, key: str, value: str) -> bool:
    if value is None:
        return True
    if key in tags:
        _value = str(tags[key]).lower()
        if _value.find(value.lower()) > -1:
            return True
    return False
