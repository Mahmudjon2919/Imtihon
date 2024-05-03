def is_even(number):

    return number % 2 == 0

number = int(input("Butun son kiriting: "))

if is_even(number):
    print(f"{number} juft son.")
else:
    print(f"{number} toq son.")
