import dateutil.parser as du


def check(tags: dict, args: dict) -> bool:
    if "after" not in args:
        return True
    if args["after"] is None:
        return True

    after = du.parse(args["after"])

    date_args = ("EXIF DateTimeDigitized", "EXIF DateTimeOriginal", "Image DateTime")
    for arg in date_args:
        if arg in tags:
            value = str(tags[arg])
            if not value:
                continue
            if value.count(":") > 3:
                value = value.replace(":", "-", 2)
            value = du.parse(value)
            if value and value > after:
                return True
    return False
