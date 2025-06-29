
with open("todos.txt", "r") as read_file:
    todos = read_file.readlines()
    
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    
    if "add" in user_action or "new" in user_action:
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
            
    elif "show" in user_action or "get" in user_action:
        for index, item in enumerate(todos):
            print(f"{index + 1}- {item.strip()}")
            
    elif "exit" in user_action:
        print("Bye! :)")
        break
    
    elif "edit" in user_action:
        todo_index = int(user_action.strip()[-1]) - 1
        new_todo = input("Enter the new todo: ") + "\n"
        todos[todo_index] = new_todo
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
    
    elif "complete" in user_action or "done" in user_action:
        todo_index = int(user_action.strip()[-1]) - 1
        removed_todo = todos.pop(todo_index)
        print(f"this todo: [{removed_todo.strip()}] is removed from the list")
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
    else:
        print("Command is not valid..")

