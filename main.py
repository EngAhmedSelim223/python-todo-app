read_file = open("todos.txt", "r")
todos = read_file.readlines()
read_file.close()
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            write_file = open("todos.txt", "w")
            write_file.writelines(todos)
            write_file.close()
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}- {item.strip()}")
        case "exit":
            print("Bye! :)")
            break
        case "edit":
            print(todos)
            todo_number = int(input("Enter the number of todo to edit: "))
            new_todo = input("Enter the new todo: ")
            todos[todo_number - 1] = new_todo
            write_file = open("todos.txt", "w")
            write_file.writelines(todos)
            write_file.close()
        
        case "complete":
            todo_number = int(input("Enter the number of todo to complete: "))
            todos.pop(todo_number - 1)
            write_file = open("todos.txt", "w")
            write_file.writelines(todos)
            write_file.close()
        case _:
            print("Unknown action...")

