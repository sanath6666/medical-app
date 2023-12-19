import streamlit as st
import openai

# Configure your OpenAI API key
api_key = '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'
openai.api_key = api_key

def get_openai_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100  # Adjust the number of tokens for the response length
    )
    return response.choices[0].text.strip()

def main():
    st.title("Medical AI Chatbot")

    st.write("Welcome! Ask me any medical-related questions.")

    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        if user_input:
            chatbot_response = get_openai_response(user_input)
            st.text_area("Chatbot:", chatbot_response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()


