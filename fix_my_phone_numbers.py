def is_it_a_num(s: str) -> str:
    phone_number = [value for value in s if value.isdigit()]
    return "".join(phone_number) if len(phone_number) == 11 and phone_number[0] == "0" else "Not a phone number"


class Person:
    def __init__(self, age: int, height: int) -> None:
        self.age = age
        self.height = height

    def is_old(self) -> bool:
        return True if self.age > 70 else False


class Man(Person):
    def __init__(self, age: int, height: int, has_bread: bool) -> None:
        super().__init__(age, height)
        self.has_bread = has_bread

    def is_older_than_other_person(self, other_person: Person):
        return self.age > other_person.age


if __name__ == "__main__":
    print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
