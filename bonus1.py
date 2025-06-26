name = input("Enter your name: ").lower().strip()
match name:
    case "ahmed":
        print("You are 30 years old")
    case "mahmoud":
        print("You are 26 years old")
    case "thanaa":
        print("you are 23 years old")
    case "zaki" | "alyaa":
        print("you are 20 years old")
    case _:
        print("i don't know your age")