# Zaprojektuj klasy osoba, student i doktorant.
#
# Przyporzadkuj atrybuty do klas: imię, nazwisko, średnia skumulowana, pensum, kierunek, pesel.
# Napisz metodę wyliczenia wieku.
# Napisz metodę okreslenia płci na podstawie peselu.


class Person:
    PERSONAL_NUMBER_LENGTH = 11
    GENDER_POSITION = 9
    VALIDATION_WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, first_name, last_name, personal_number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = personal_number
        self.gender = self.determine_gender()

    def validate_personal_number(self, number):
        if len(number) != self.PERSONAL_NUMBER_LENGTH:
            raise ValueError("Personal number has to have 11 digits!")
        return number

    def validate_with_control_digit(self):
        control_digit = int(self.number[-1])
        weighted_digits = [(int(self.number[i]) * self.VALIDATION_WEIGHTS[i]) % 10 for i in range(0, 10)]
        return control_digit == 10 - sum(weighted_digits) % 10

    def determine_gender(self):
        gender_digit = int(str(self.number)[self.GENDER_POSITION])
        return "Female" if gender_digit % 2 == 0 else "Male"
