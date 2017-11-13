def get_key(key):
    key = key.upper()
    if key in ["C", "D", "E", "F", "G", "A", "B"]:
        return "Key: {0}".format(key)
    else:
        raise ValueError("存在しないKeyです。")
