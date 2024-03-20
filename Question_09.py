'''Quiz Game: Create a quiz game with multiple-choice questions. Keep track of the 
player's score and provide feedback on their performance.'''

import streamlit as st

# Defining the quiz questions and their answers
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["London", "Paris", "Berlin", "Madrid"],
        'correct_answer': "Paris"
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
        'correct_answer': "William Shakespeare"
    },
    {
        'question': "What is the largest planet in our solar system?",
        'options': ["Mars", "Venus", "Jupiter", "Saturn"],
        'correct_answer': "Jupiter"
    }
]

# Defining Function to display the quiz
def display_quiz():
    st.title("Quiz Game")
    score = 0

    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['question']}")
        user_answer = st.radio("Select your answer:", options=question['options'])

        if user_answer == question['correct_answer']:
            score += 1

    st.write(f"Your score: {score}/{len(questions)}")
    if score == len(questions):
        st.success("Congratulations! You got all questions correct!")
    elif score >= len(questions) / 2:
        st.info("Not bad! You got some questions correct.")
    else:
        st.error("Better luck next time! You got most questions wrong.")

# Defining Main function to run the Streamlit app
def main():
    display_quiz()

if __name__ == "__main__":
    main()
