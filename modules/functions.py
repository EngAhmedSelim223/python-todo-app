FILE_PATH = "todos.txt"
# STEP: Get Todos function
def get_todos(filename = FILE_PATH):
    """ 
        function used to read the text file
        and return a to-do list
    """
    with open(filename, "r") as read_file:
        todos = read_file.readlines()
    return todos
# STEP: Update Todos function
def update_todos(filename = FILE_PATH, todos = None):
    """ 
        function to write to-do item list
        to the text file
    """
    with open(filename, "w") as write_file:
        write_file.writelines(todos)

if __name__ == "__main__":
    print("Hello From functions file")