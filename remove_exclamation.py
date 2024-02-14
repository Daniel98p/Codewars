def remove(st, n):
    return st.replace("!", "", n)


if __name__ == "__main__":
    print(remove("!!!Hi !!hi!!! !hi", 100))
