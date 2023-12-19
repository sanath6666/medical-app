import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Your existing code for data loading and model building
# ...

# Function to get severity dictionary, description list, and precaution dictionary from CSV files
# ...

# Function to handle the chatbot logic
def handle_chatbot():
    st.write("-----------------------------------HealthCare ChatBot-----------------------------------")
    st.write("\nYour Name?")
    name = st.text_input("", "")
    st.write(f"Hello, {name}")
    
    st.write("\nEnter the symptom you are experiencing:")
    disease_input = st.text_input("", "")
    num_days = st.number_input("From how many days?", min_value=1, step=1)

    # Existing logic for the chatbot function
    # ...

    # Output the results
    st.write("----------------------------------------------------------------------------------------")

# Create the Streamlit app
def main():
    st.title("Medical AI Chatbot")
    handle_chatbot()

if __name__ == "__main__":
    main()


