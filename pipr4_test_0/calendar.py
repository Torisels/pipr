class Calendar:
    MONTHS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
              "September": 30, "October": 31,
              "November": 30, "December": 31}

    def __init__(self, first_day_index):
        self.first_day_index = first_day_index
        self.week = 1

    def one_month_string(self, length):
        header = "Wk  Mo Tu We Th Fr Sa Su\n"
        week = f"{self.week:02}  "
        blank_spaces = " " * 3 * self.first_day_index
        output_string = [header, week, blank_spaces]
        for day in range(1, length + 1):
            output_string.append(f"{day:02} ")
            if self.first_day_index == 6:
                self.week += 1
                self.first_day_index = 0
                if day != length:
                    output_string.append("\n")
                    output_string.append(f"{self.week:02}{' '*2}")
            else:
                self.first_day_index += 1

        return "".join(output_string)

    def print_whole_year(self):
        output_str = []
        for month, length in self.MONTHS.items():
            output_str.append("\n")
            output_str.append(self.month_string(month))
            output_str.append("\n")
            output_str.append(self.one_month_string(length))
            output_str.append("\n")
        output_str.pop(0)
        print("".join(output_str))

    @staticmethod
    def month_string(month):
        length = 24
        equals = length - len(month)
        if equals % 2 == 0:
            eq = '=' * (equals//2)
            return f"{eq}{month}{eq}"
        else:
            return f"{'='*(equals//2)}{month}{'='*((equals//2)+1)}"