from libs import basic_calc

calc = basic_calc.CalcInPy()
calc.input_number()
result = calc.check_numbers()
if result is not None:
    print(result)