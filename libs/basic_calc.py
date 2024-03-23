from time import sleep


class CalcInPy:
    def __init__(self) -> None:
        self.primary_number = 0
        self.second_number = 0
        self.option_calc = 0

    def input_number(self):
        self.primary_number = int(input("Insert number for calculation: "))
        self.second_number = int(input("Insert second number for calculation: "))

    def calc_choice(self):
        self.option_calc = int(
            input(
                "Select a option for calculation with 1 for sum, 2 subtraction, 3 division, or 4 for exit for calc: "
            )
        )

        while True:
            if self.option_calc == 1:
                return self.calc_sum()
            elif self.option_calc == 2:
                return self.calc_subtraction()
            elif self.option_calc == 3:
                return self.calc_division()
            elif self.option_calc == 4:
                print("\nExiting the calculator...")
                sleep(2)
                return None

    def check_numbers(self):
        if self.primary_number > 0 and self.second_number > 0:
            return self.calc_choice()
        elif isinstance(self.primary_number, str) or isinstance(
            self.second_number, str
        ):
            print("Please, insert a number not a text")
        else:
            print("Numbers must be greater than zero.")

    def calc_sum(self):
        result = self.primary_number + self.second_number
        return result

    def calc_subtraction(self):
        result = self.primary_number - self.second_number
        return result

    def calc_division(self):
        result = self.primary_number / self.second_number
        return result
