print("=== Ritu's Calculator 2.0 ===")

while True:
    print("\n1. হিসাব করো")
    print("2. বের হয়ে যাও")
    choice = input("কি করবা? 1/2: ")
    
    if choice == "2":
        print("বাই বাই Ritu ভাই! 👋")
        break
        
    elif choice == "1":
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
            if num2 == 0:
                print("0 দিয়ে ভাগ হয় না ভাই!")
            else:
                print(f"ফলাফল: {num1 / num2}")
        else:
            print("ভুল অপারেটর দিছো ভাই")
    else:
        print("1 বা 2 চাপো ভাই")