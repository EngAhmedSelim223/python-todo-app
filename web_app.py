import streamlit as st
from modules import functions as func
st.title("My to-do APP")
st.subheader("Where you can manage your to-dos")
todos = func.get_todos()
st.set_page_config(layout = "wide")
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    func.update_todos(todos = todos)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key = todo)
    if checkbox:
        todos.pop(index)
        func.update_todos(todos = todos)
        del st.session_state[todo]
        st.rerun()
    
st.text_input(label = "Enter a to-do: ", placeholder = "Add New Todo...",
              on_change = add_todo, key = "new_todo")

