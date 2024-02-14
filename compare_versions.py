import itertools


def compare_versions(version1, version2):
    for value1, value2 in itertools.zip_longest(version1.split("."), version2.split(".")):
        if value2 is None:
            return True
        if value1 is None or int(value1) < int(value2):
            return False
    return True


if __name__ == "__main__":
    print(compare_versions("10.4", "10.4.8"))
