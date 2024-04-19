#program to create webbased app
import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
     todo=st.session_state["new_todo"]+"\n"
     todos.append(todo)
     functions.write_todos(todos)


st.title("Rakesh TODO App")
st.subheader("rock daily activities ")
st.write("this app helps with productivity")
 
for index, todo in enumerate(todos):
     checkbox=st.checkbox(todo,key=todo)
     if checkbox:
         todos.pop(index)
         functions.write_todos(todos)
         del st.session_state[todo]
         st.experimental_rerun()


     
st.text_input(label="",placeholder="Add new todo acitivity...",
              on_change=add_todo,key="new_todo")

st.session_state

#st.checkbox(" meeting at 10")