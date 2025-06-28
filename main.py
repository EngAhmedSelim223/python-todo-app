
with open("todos.txt", "r") as read_file:
    todos = read_file.readlines()
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    if "add" in user_action:
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
    if "show" in user_action:
        for index, item in enumerate(todos):
            print(f"{index + 1}- {item.strip()}")
    if "exit" in user_action:
        print("Bye! :)")
        break
    if "edit" in user_action:
        print(todos)
        todo_number = int(input("Enter the number of todo to edit: "))
        new_todo = input("Enter the new todo: ") + "\n"
        todos[todo_number - 1] = new_todo
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
    
    if "complete" in user_action:
        todo_number = int(input("Enter the number of todo to complete: "))
        removed_todo = todos.pop(todo_number - 1)
        print(f"this todo: [{removed_todo.strip()} is removed from the list")
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)

