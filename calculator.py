class Calculator:
    def addition(self, a, b):

        return a + b

    def subtraction(self, a, b):

        return a - b

    def multiplication(self, a, b):

        return a * b

    def division(self, a, b):

        if b != 0:
            return a / b
        else:
            return "Nolga bo'linib bo'lmaydi."

if __name__ == "__main__":
    calculator = Calculator()

    a = float(input("Son kiriting: "))
    b = float(input("Son kiriting: "))

    print(f"Addition: {calculator.addition(a, b)}")
    print(f"Subtraction: {calculator.subtraction(a, b)}")
    print(f"Multiplication: {calculator.multiplication(a, b)}")
    print(f"Division: {calculator.division(a, b)}")
