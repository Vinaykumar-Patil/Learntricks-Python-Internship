'''File Organizer: Build a program that organizes files in a directory by grouping them 
into subdirectories based on file types (e.g., images, documents, videos).'''

import streamlit as st
import os
import shutil

# Defining Function to organize files into subdirectories
def organize_files(directory):
    # Creating subdirectories for different file types
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Others': []  # Default category for other file types
    }

    # Iterating through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Determine the file type
            file_extension = os.path.splitext(filename)[1].lower()
            category_found = False
            # Move the file to the appropriate subdirectory
            for category, extensions in categories.items():
                if file_extension in extensions:
                    category_found = True
                    dest_directory = os.path.join(directory, category)
                    if not os.path.exists(dest_directory):
                        os.makedirs(dest_directory)
                    shutil.move(file_path, dest_directory)
                    break
            # If file doesn't match any category, move it to 'Others' directory
            if not category_found:
                dest_directory = os.path.join(directory, 'Others')
                if not os.path.exists(dest_directory):
                    os.makedirs(dest_directory)
                shutil.move(file_path, dest_directory)

# Defining Main function for Streamlit app
def main():
    st.title("File Organizer")

    # File uploader
    uploaded_file = st.file_uploader("Upload Files", accept_multiple_files=True)

    # Creating Organize button
    if st.button("Organize Files"):
        if uploaded_file is not None:
            # Creating a temporary directory to store uploaded files
            tmp_directory = 'tmp'
            if not os.path.exists(tmp_directory):
                os.makedirs(tmp_directory)
            for file in uploaded_file:
                file_path = os.path.join(tmp_directory, file.name)
                with open(file_path, 'wb') as f:
                    f.write(file.getbuffer())
            # Organize files
            organize_files(tmp_directory)
            st.success("Files organized successfully!")
            # Remove temporary directory
            shutil.rmtree(tmp_directory)
        else:
            st.warning("Please upload files first.")

if __name__ == "__main__":
    main()
