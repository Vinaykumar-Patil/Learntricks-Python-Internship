'''Chat Application: Develop a basic chat application that allows users to send and 
receive messages in real-time using sockets or a simple web interface.'''

import streamlit as st

# Defining Function to display chat interface
def chat_interface():
    st.title("Simple Chat Application")

    # Text area to enter messages
    message = st.text_input("Enter message:", "")

    # Button to send message
    if st.button("Send"):
        st.write("You:", message)
        # You can write code here to send the message to other users or a server

# Defining Main function to run the Streamlit app
def main():
    chat_interface()

if __name__ == "__main__":
    main()
