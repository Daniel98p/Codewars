def solution(pairs):
    st = ""
    for key, value in pairs.items():
        st += f"{key}: {value},"
    st = st[:-1]
    return st
