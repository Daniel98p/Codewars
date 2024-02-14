def isomorph(a, b):
    characters_map = {}
    if len(a) != len(b):
        return False
    for ch, c in zip(a, b):
        if ch not in characters_map.keys() and c not in characters_map.values():
            characters_map.update({ch: c})
    for ch, c in zip(a, b):
        if ch not in characters_map.keys() or characters_map[ch] != c:
            return False
    return True


if __name__ == "__main__":
    print(isomorph("AB", "CC"))