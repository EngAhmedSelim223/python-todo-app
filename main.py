todos = []
while True:
    user_action = input("Type add, show, edit or exit: ").lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(f"{len(todos) + 1}- {todo}")
        case "show":
            for item in todos:
                print(item)
        case "exit":
            print("Bye! :)")
            break
        case "edit":
            print(todos)
            todo_number = int(input("Enter the number of todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todos[todo_number - 1] = f"{todo_number}- {new_todo}"
        case _:
            print("Unknown action...")

