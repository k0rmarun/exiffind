import dateutil.parser as du


def check(tags: dict, args: dict) -> bool:
    if "before" not in args:
        return True
    if args["before"] is None:
        return True

    before = du.parse(args["before"])

    date_args = ("EXIF DateTimeDigitized", "EXIF DateTimeOriginal", "Image DateTime")
    for arg in date_args:
        if arg in tags:
            value = str(tags[arg])
            if not value:
                continue
            if value.count(":") > 3:
                value = value.replace(":", "-", 2)
            value = du.parse(value)
            if value and value < before:
                return True
    return False
