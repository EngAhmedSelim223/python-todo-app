from modules import functions as func
import time
print(f"It's {time.strftime("%b %d, %Y")}")
todos = func.get_todos()

while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    # STEP: Add to-do
    if user_action.startswith("add") :
        todo = user_action[4:] + "\n"
        todos.append(todo)
        func.update_todos(todos = todos)
    # STEP: Show to-do
    elif user_action.startswith("show"):
        for index, item in enumerate(todos):
            print(f"{index + 1}- {item.strip()}")
    # STEP: Exit the program    
    elif user_action.startswith("exit"):
        print("Bye! :)")
        break
    # STEP: Edit a to-do
    elif user_action.startswith("edit"):
        
        try:
            todo_index = int(user_action.strip()[-1]) - 1
            new_todo = input("Enter the new todo: ") + "\n"
            todos[todo_index] = new_todo
            func.update_todos(todos = todos)
        except ValueError:
            print("Invalid command Pleas enter edit + todo number")
    # STEP: complete a to-do
    elif user_action.startswith("complete"):
        try:
            
            todo_index = int(user_action.strip()[-1]) - 1
            removed_todo = todos.pop(todo_index)
            print(f"this todo: [{removed_todo.strip()}] is removed from the list")
            func.update_todos(todos = todos)
        except ValueError:
            print("invalid command please enter complete + todo number")
    else:
        print("Command is not valid..")
