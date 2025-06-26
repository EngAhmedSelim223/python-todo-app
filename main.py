todos = []
while True:
    user_action = input("Type add or show or exit: ").lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            print("Bye! :)")
            break
        case _:
            print("Unknown action...")

