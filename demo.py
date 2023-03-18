from calculator import Calculator

calc = Calculator()
calc.reset()
calc.add(2)
print(calc.memory)
calc.multiply(3)
print(calc.memory)
calc.root(2)
print(calc.memory) # Output: 2.449
calc.reset()
calc.subtract(5)
calc.divide(2)
print(calc.memory) # Output: -2.5
