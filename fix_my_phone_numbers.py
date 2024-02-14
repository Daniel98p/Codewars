def is_it_a_num(s: str) -> str:
    phone_number = [value for value in s if value.isdigit()]
    return "".join(phone_number) if len(phone_number) == 11 and phone_number[0] == "0" else "Not a phone number"


if __name__ == "__main__":
    print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
