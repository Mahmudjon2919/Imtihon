while True:
  try:
    user_input = int(input("Butun son kiriting: "))
    print(f"Kiritilgan son: {user_input}")
    break
  except ValueError:
    print("Xato. Iltimos butun son kiriting.")

print("dastur tugadi.")