from lect_5_hw_1 import Person

class Employee(Person):
    def __init__(self, full_name, year, position, experience, salary):
        Person.__init__(self, full_name, year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def full_information(self):
        if self.experience <= 3:
            junior = "Junior" + " " + self.position
            return junior
        if 3 < self.experience <= 6:
            middle = "Middle" + " " + self.position
            return middle
        else:
            senior = "Senior" + " " + self.position
            return senior

    def increase_salary(self, increase_sal):
        new_salary = self.salary + increase_sal
        return new_salary

if __name__ == "__main__":
    a = Employee("Alex Ustinov", 1986, "Developer", 6, 1000)
    print(a.full_information())
    print(a.increase_salary(200))