def check(tags, args):
    width = args.get("width")
    if width is None:
        return True

    comp = "="

    if width[0] in "<>=":
        comp = width[0]
        width = width[1:]
        width = int(width)
    else:
        width = int(width)

    w_args = ("EXIF ExifImageWidth", "EXIF ImageWidth", "EXIF Width")
    for arg in w_args:
        if arg in tags:
            value = tags[arg]
            if value is None:
                continue
            value = int(str(value))

            if comp == "<" and value < width:
                return True
            if comp == ">" and value > width:
                return True
            if comp == "=" and value == width:
                return True
    return False