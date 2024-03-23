class CalcInPy:
    def __init__(self) -> None:
        self.primary_number = 0
        self.second_number = 0
        self.option_calc = 0

    def input_number(self):
        self.primary_number = int(input())
        self.second_number = int(input())  # campo para inserir os números

    def calc_choice(self):
        self.option_calc = int(input(""))

        if self.option_calc == 1:
            return self.calc_sum()
        elif self.option_calc == 2:
            return self.calc_subtraction() # botões para escolha do tipo de calculo
        elif self.option_calc == 3:
            return self.calc_division()
        elif self.option_calc == 4:
            print("Exiting the calculator")

    def check_numbers(self):
        if self.primary_number > 0 and self.second_number > 0:
            return self.calc_choice()  # retorna o calculo
        else:
            print("Numbers must be greater than zero.")  # tela de aviso sobre os números serem maior que zero

    def calc_sum(self):
        result = self.primary_number + self.second_number
        return result

    def calc_subtraction(self):
        result = self.primary_number - self.second_number
        return result                                    # campo para retornar o calculo

    def calc_division(self):
        result = self.primary_number / self.second_number
        return result


calc = CalcInPy()
calc.input_number()
result = calc.check_numbers()
print(result)
