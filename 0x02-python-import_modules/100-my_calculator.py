#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def my_calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Invalid input. Please provide valid integers for <a> and <b>")
        sys.exit(1)

    result = 0

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    print(f"{a} {operator} {b} = {result}")
    sys.exit(0)

if __name__ == "__main__":
    my_calculator()

