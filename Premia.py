def experience_bonus(experience, salary):
    if experience <= 1:
        bonus = 0.05 * salary
    elif experience <= 5:
        bonus = 0.10 * salary
    else:
        bonus = 0.15 * salary
    return bonus


def salary_bonus(salary):
    if 1000 <= salary <= 2000:
        second_bonus = 0.12 * salary
    elif 2000 <= salary <= 10000:
        second_bonus = 0.08 * salary
    else:
        second_bonus = 0
    return second_bonus


def name_bonus(name, salary):
    if len(name) > 5:
        third_bonus = 0.2 * salary
    elif len(name) > 10:
        third_bonus = 0.3 * salary
    else:
        third_bonus = 0
    return third_bonus


def calculate_best_bonus (name, salary, experience):
    if experience_bonus(experience, salary) > salary_bonus(salary) and experience_bonus(experience, salary) > name_bonus(name, salary):
        best_bonus = experience_bonus(experience, salary)
    elif experience_bonus(experience, salary) < salary_bonus(salary) and salary_bonus(salary) > name_bonus(name, salary):
        best_bonus = salary_bonus(salary)
    elif experience_bonus(experience, salary) < name_bonus(name, salary) and salary_bonus(salary) < name_bonus(name, salary):
        best_bonus = name_bonus(name, salary)
    return best_bonus


if __name__ == '__main__':
    my_name = input("Enter the name of employee: ")
    my_experience = int(input('Enter work experience: '))
    my_salary = float(input('Enter current salary: '))
    print(experience_bonus(my_experience, my_salary))
    print(salary_bonus(my_salary))
    print(name_bonus(my_name, my_salary))
    print(calculate_best_bonus(my_name, my_salary, my_experience))


