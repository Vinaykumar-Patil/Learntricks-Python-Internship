'''Simple Blog System: Create a simple blog system where users can write, edit, and 
delete blog posts. Store blog posts in text files or a lightweight database.'''

import streamlit as st
import os

# Defining Function to get all blog posts
def get_all_posts():
    if not os.path.exists("posts"):
        os.makedirs("posts")
    posts = []
    for filename in os.listdir("posts"):
        with open(os.path.join("posts", filename), 'r') as f:
            posts.append({
                'id': filename.split('.')[0],  # Extracting post ID from filename
                'content': f.read()  # Reading post content
            })
    return posts

# Defining Main function
def main():
    st.title("Simple Blog System")

    # Sidebar options
    options = ['Home', 'Create New Post']
    choice = st.sidebar.radio("Navigation", options)

    # Display all blog posts
    if choice == 'Home':
        st.header("All Blog Posts")
        posts = get_all_posts()
        for post in posts:
            st.write(f"**Post ID:** {post['id']}")
            st.write(post['content'])
            if st.button(f"Delete Post {post['id']}"):
                delete_post(post['id'])

    # Creating new post
    elif choice == 'Create New Post':
        st.header("Create New Post")
        content = st.text_area("Enter your blog post here:")
        if st.button("Create Post"):
            create_post(content)

# Defining Function to create a new post
def create_post(content):
    if not os.path.exists("posts"):
        os.makedirs("posts")
    post_id = len(os.listdir("posts")) + 1
    with open(os.path.join("posts", f"{post_id}.txt"), 'w') as f:
        f.write(content)
    st.success("Post created successfully!")

# Defining Function to delete a post
def delete_post(post_id):
    os.remove(os.path.join("posts", f"{post_id}.txt"))
    st.success(f"Post {post_id} deleted successfully!")

if __name__ == "__main__":
    main()

