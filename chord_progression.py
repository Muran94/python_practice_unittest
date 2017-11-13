def get_key(key):
    key = key.upper()
    if key in ["C", "CM", "D", "E", "F", "G", "A", "B"]:
        if key[-1].upper() == "M":
            format_key = key[0] + key[-1].lower()
        else:
            format_key = key[0]
        return "Key: {0}".format(format_key)
    else:
        raise ValueError("存在しないKeyです。")
