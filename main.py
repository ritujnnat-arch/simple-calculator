print("=== Ritu's Calculator ===")
num1 = float(input("প্রথম সংখ্যা: "))
op = input("কি করবা? + - * / : ")
num2 = float(input("দ্বিতীয় সংখ্যা: "))

if op == "+":
    print(f"ফলাফল: {num1 + num2}")
elif op == "-":
    print(f"ফলাফল: {num1 - num2}")
elif op == "*":
    print(f"ফলাফল: {num1 * num2}")
elif op == "/":
    print(f"ফলাফল: {num1 / num2}")
else:
    print("ভুল অপারেটর দিছো ভাই")
