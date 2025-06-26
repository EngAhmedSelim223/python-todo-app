todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}- {item}")
        case "exit":
            print("Bye! :)")
            break
        case "edit":
            print(todos)
            todo_number = int(input("Enter the number of todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todos[todo_number - 1] = new_todo
        
        case "complete":
            todo_number = int(input("Enter the number of todo to complete: "))
            todos.pop(todo_number - 1)
        case _:
            print("Unknown action...")

