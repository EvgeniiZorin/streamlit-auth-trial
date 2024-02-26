import streamlit as st

# State management -----------------------------------------------------------

# I like to use state instead of the long form 
state = st.session_state

def init_state(key, value):
  if key not in state:
    state[key] = value

# generic callback to set state
def _set_state_cb(**kwargs):
    for state_key, widget_key in kwargs.items():
        val = state.get(widget_key, None)
        if val is not None or val == "":
            setattr(state, state_key, state[widget_key])

def _set_login_cb(username, password):
    state.login_successful = login(username, password)  

def _reset_login_cb():
    state.login_successful = False
    state.username = ""
    state.password = "" 

init_state('login_successful', False)
init_state('username', '')
init_state('password', '')

# -----------------------------------------------------------------------------

# Function to check login credentials
def login(username, password):
    return username == "a" and password == "b"

# Main function
def main():
    st.title("My App")

    # If login is successful, display "Hello"
    if state.login_successful:
        st.subheader("My Page")
        st.write("Hello")
        st.button("Logout", on_click=_reset_login_cb)
    else:
        st.subheader("Login")
        # Display login form
        st.text_input(
            "Username:", value=state.username, key='username_input',
            on_change=_set_state_cb, kwargs={'username': 'username_input'}
        )
        st.text_input(
            "Password:", type="password", value=state.password, key='password_input',
            on_change=_set_state_cb, kwargs={'password': 'password_input'}
        )

        # st.write(state.username)
        # st.write(state.password)
        
        # Check login credentials
        if not state.login_successful and st.button("Login", on_click=_set_login_cb, args=(state.username, state.password)):
            st.warning("Wrong username or password.")

if __name__ == "__main__":
    main()

