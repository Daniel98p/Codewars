def proofread(st):
    if st == "":
        return ""
    st = st.lower()
    st = st.replace("ie", "ei")
    st = st[0].upper() + st[1:]
    indices = [i for i in range(len(st)) if st.startswith(". ", i)]
    for index in indices:
        st = st[:index + 2] + st[index + 2].upper() + st[index + 3:]
    return st


if __name__ == '__main__':
    print(proofread("SHe went canoeing."))
