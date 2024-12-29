import functions
import streamlit as st
# Terminal: streamlit run web.py
# Local URL: http://localhost:8501
# Network URL: http://192.168.1.235:8501
# pip freeze > requirements.txt
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo']=""


# MAIN PROGRAM
st.title("My ToDo App")
st.subheader("Overview of your todo list")
st.write("Select a todo when completed:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


new_todo = st.text_input(label="Add a new todo", key="new_todo", on_change=add_todo)


# st.session_state

