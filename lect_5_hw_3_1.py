import unittest


def leap_year(year):
    year_4 = year % 4
    year_400 = year % 400
    year_100 = year % 100

    if year_4 != 0:
        return False
    elif year_100 == 0:
        if year_400 == 0:
            return True
        else:
            return False
    else:
        return False


class LeapYearTestCase(unittest.TestCase):
    def test_year_4(self):
        self.assertFalse(leap_year(2001))

    def test_year_400(self):
        self.assertTrue(leap_year(2000))

    def test_year_400_false(self):
        self.assertFalse(leap_year(2100))

    def test_year_4_false(self):
        self.assertFalse(leap_year(20))


if __name__ == '__main__':
    unittest.main()
