FILEPATH="vnev/todos.txt"
#def get_todos(filepath=FILEPATH):
def get_todos(filepath=FILEPATH):
    #doc string
    """ this is called as documentation string and use it for every function"""
    # def get_todos(filepath="todos.txt"):
    with open(filepath,"r") as file_local:
        todos_local=file_local.readlines()
        return todos_local
print(help(get_todos))

#def write_todos(odos_arg,filepath=FILEPATH):
def write_todos(todos_arg,filepath=FILEPATH):
# def write_todos(filepath="todos.txt", todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#if __name__=="__custFunctions__"
 #   print("hello")
 #  print(get_todos())