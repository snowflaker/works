import datetime

class Person:
    def __init__(self, full_name, year):
        self.full_name = full_name
        self.year = year

    def first_name(self):
        f_name = self.full_name
        f_name = f_name.split(" ")
        return f_name[0]

    def last_name(self):
        l_name = self.full_name
        l_name = l_name.split(" ")
        return l_name[1]

    def how_old(self, year=None):
        if year is None:
            now = datetime.datetime.now()
            age_now = now.year - self.year
            return age_now
        else:
            age_future = year - self.year
            return age_future

if __name__ == "__main__":
    p = Person("Valeriy Onikienko", 1989)
    print(p.last_name(), p.first_name())
    print(p.how_old())







