def check(tags, args):
    height = args.get("height")
    if height is None:
        return True

    comp = "="

    if height[0] in "<>=":
        comp = height[0]
        height = height[1:]
        height = int(height)
    else:
        height = int(height)

    w_args = ("EXIF ExifImageHeight", "EXIF ImageHeight", "EXIF Height", "EXIF ExifImageLength", "EXIF ImageLength", "EXIF Length")
    for arg in w_args:
        if arg in tags:
            value = tags[arg]
            if value is None:
                continue
            value = int(str(value))

            if comp == "<" and value < height:
                return True
            if comp == ">" and value > height:
                return True
            if comp == "=" and value == height:
                return True
    return False