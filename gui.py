from modules import functions 
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events = True, size = [45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
    ]

window = sg.Window("My To-Do App",
                   layout= layout,
                   font=("Helvetica", 12))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            functions.update_todos(todos = todos)
        
        case "Edit":
           try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.update_todos(todos = todos)
                window['todos'].Update(values = todos)
           except IndexError:
               sg.popup("Please Select an item First")
               
        case "todos":
            window['todo'].Update(value = values['todos'][0])
        
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.update_todos(todos = todos)
                window["todos"].Update(values = todos)
            except IndexError:
               sg.popup("Please Select an item First")
        
        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break
window.close()