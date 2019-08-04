import Class_example

if __name__ == '__main__':
    person1 = Class_example.Person('Daniel', 'Michalik', 'Im learning python')
    print(person1.get_name())
    print(person1.get_surname())
    print(person1.get_sentence())
    person1.set_sentence('Im playing football')
    print(person1.get_sentence())


