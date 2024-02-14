def reverse_number(n):
    n = str(n).rstrip("0") if len(str(n)) > 1 else str(n)
    if n.startswith("-"):
        n = "-" + n[:0:-1]
    else:
        n = n[::-1]
    return int(n)