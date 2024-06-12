def naughty_or_nice(data):
    naughty = 0
    nice = 0
    for month in data:
        for value in data.get(month).values():
            if value == "Naughty":
                naughty += 1
            else:
                nice += 1
    return "Naughty!" if naughty > nice else "Nice!"
