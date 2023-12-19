import streamlit as st

# Dictionary to store symptoms and possible diseases
symptom_diseases = {
    'cough': ['Common cold', 'Flu', 'Pneumonia'],
    'fever': ['Flu', 'COVID-19', 'Malaria'],
    # Add more symptoms and related diseases here
}

def symptom_checker(symptoms):
    possible_diseases = []
    for symptom in symptoms:
        if symptom in symptom_diseases:
            possible_diseases.extend(symptom_diseases[symptom])
    
    return list(set(possible_diseases))

def main():
    st.title('Healthcare Chatbot')
    st.write("Welcome! I'm here to help you with your health concerns.")

    # Sidebar for user input
    with st.sidebar:
        st.header('Symptom Checker')
        st.write('Enter your symptoms (comma-separated):')
        user_input = st.text_input('Example: cough, fever')

    if st.button('Check'):
        if user_input:
            symptoms = [s.strip().lower() for s in user_input.split(',')]
            possible_diseases = symptom_checker(symptoms)
            if possible_diseases:
                st.success(f"Possible diseases based on symptoms: {', '.join(possible_diseases)}")
            else:
                st.warning('No diseases found based on provided symptoms.')
        else:
            st.warning('Please enter some symptoms.')

if __name__ == "__main__":
    main()



