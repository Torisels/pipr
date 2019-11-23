# Zaprojektuj klasy osoba, student i doktorant.
#
# Przyporzadkuj atrybuty do klas: imię, nazwisko, średnia skumulowana, pensum, kierunek, pesel.
# Napisz metodę wyliczenia wieku.
# Napisz metodę okreslenia płci na podstawie peselu.


import re
import datetime
from dateutil.relativedelta import relativedelta


class Pesel:
    """
    This class is based on https://obywatel.gov.pl/dokumenty-i-dane-osobowe/czym-jest-numer-pesel

    """
    PERSONAL_NUMBER_LENGTH = 11
    FIRST_MONTH_DIGIT_POS = 2
    GENDER_DIGIT_POS = 9
    VALIDATION_WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, number):
        self.number = self.validate(number)
        self.birthday = self.determine_date_of_birth()
        self.gender = self.determine_gender()

    def validate(self, number):
        number = str(number)
        if len(number) != self.PERSONAL_NUMBER_LENGTH:
            raise ValueError("PESEL has to have 11 characters!")
        if re.match(r"^[0-9]{11}$", number) is None:
            raise ValueError("PESEL has to contain digits only!")
        if self.control_digit_validation(number) is False:
            raise ValueError("PESEL is not valid. Control sums don't match!")
        return number

    def determine_date_of_birth(self):
        month_subtrahend = 0
        fm_digit = int(self.number[self.FIRST_MONTH_DIGIT_POS])

        if fm_digit is 0 or fm_digit is 1:
            base_year = 1900
        elif fm_digit is 2 or fm_digit is 3:
            base_year = 2000
            month_subtrahend = 20
        elif fm_digit is 4 or fm_digit is 5:
            base_year = 2100
            month_subtrahend = 40
        elif fm_digit is 6 or fm_digit is 7:
            base_year = 2200
            month_subtrahend = 60
        else:
            base_year = 1800
            month_subtrahend = 80

        year = int(self.number[0:2]) + base_year
        month = int(self.number[2:4]) - month_subtrahend
        day = int(self.number[4:6])

        return datetime.date(year=year, month=month, day=day)

    def determine_gender(self):
        gender_digit = int(str(self.number)[self.GENDER_DIGIT_POS])
        return "Female" if gender_digit % 2 == 0 else "Male"

    @staticmethod
    def control_digit_validation(number):
        control_digit = int(number[-1])
        weighted_digits = [(int(number[i]) * Pesel.VALIDATION_WEIGHTS[i]) % 10 for i in range(0, 10)]
        return control_digit == 10 - sum(weighted_digits) % 10


class Person:

    def __init__(self, first_name, last_name, personal_number):
        self.first_name = first_name
        self.last_name = last_name
        try:
            pesel = Pesel(personal_number)
            self.personal_number = pesel.number
            self.gender = pesel.determine_gender()
            self.date_of_birth = pesel.birthday
        except ValueError as e:
            print(e)
            raise ValueError("Couldn't parse PESEL number!")

    def how_old(self):
        return relativedelta(datetime.date.today(), self.date_of_birth).years


class Student(Person):
    def __init__(self, first_name, last_name, personal_number, cumulative_average, course):
        super().__init__(first_name, last_name, personal_number)
        self.cumulative_average = cumulative_average
        self.course = course


class GraduateStudent(Student):
    def __init__(self, first_name, last_name, personal_number, cumulative_average, course, teaching_hours):
        super().__init__(first_name, last_name, personal_number, cumulative_average, course)
        self.teaching_hours = teaching_hours
