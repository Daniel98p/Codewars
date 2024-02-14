def longest(st):
    st_lst = st.split(" ")
    st_lst.sort(key=lambda x: (len(x), x))
    return " ".join(st_lst)
