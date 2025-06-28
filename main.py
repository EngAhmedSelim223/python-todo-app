
with open("todos.txt", "r") as read_file:
    todos = read_file.readlines()
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}- {item.strip()}")
        case "exit":
            print("Bye! :)")
            break
        case "edit":
            print(todos)
            todo_number = int(input("Enter the number of todo to edit: "))
            new_todo = input("Enter the new todo: ") + "\n"
            todos[todo_number - 1] = new_todo
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)
        
        case "complete":
            todo_number = int(input("Enter the number of todo to complete: "))
            removed_todo = todos.pop(todo_number - 1)
            print(f"this todo: [{removed_todo.strip()}] is removed from the list")
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)
        case _:
            print("Unknown action...")

