
with open("todos.txt", "r") as read_file:
    todos = read_file.readlines()
    
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    
    if user_action.startswith("add") :
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)
            
    elif user_action.startswith("show"):
        for index, item in enumerate(todos):
            print(f"{index + 1}- {item.strip()}")
            
    elif user_action.startswith("exit"):
        print("Bye! :)")
        break
    
    elif user_action.startswith("edit"):
        
        try:
            todo_index = int(user_action.strip()[-1]) - 1
            new_todo = input("Enter the new todo: ") + "\n"
            todos[todo_index] = new_todo
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)
        except ValueError:
            print("Invalid command Pleas enter edit + todo number")
            
    elif user_action.startswith("complete"):
        try:
            
            todo_index = int(user_action.strip()[-1]) - 1
            removed_todo = todos.pop(todo_index)
            print(f"this todo: [{removed_todo.strip()}] is removed from the list")
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)
        except ValueError:
            print("invalid command please enter complete + todo number")
    else:
        print("Command is not valid..")
