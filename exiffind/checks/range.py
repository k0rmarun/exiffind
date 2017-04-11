def check(tags: dict, key: str, value: str) -> bool:
    def number(num:str):
        if "/" in num:
            num = num.split("/")
            return number(num[0])/number(num[1])

        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except:
                return 0

    if value is None:
        return True

    #print(tags,key, value)


    if key in tags:
        _value = tags[key]
        if _value is None:
            return False
        _value = number(str(_value))

        if value[0] in "<>=!":
            comp = value[0]
            value = value[1:]
            value = number(value)

            if comp == "<" and _value < value:
                return True
            if comp == ">" and _value > value:
                return True
            if comp == "=" and _value == value:
                return True
            if comp == "!" and _value != value:
                return True
        else:
            if ":" in value:
                value = value.split(":")
                if len(value) < 2:
                    return False
                _min = number(value[0])
                _max = number(value[1])

                if _min > _max:
                    _min, _max = _max, _min

                if _min <= _value <= _max:
                    return True
            else:
                value = number(value)
                return value == _value
    return False
