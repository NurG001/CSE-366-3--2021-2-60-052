import pandas as pd
import streamlit as st
import spacy

# Load the dataset
file_path = 'comprehensive_medicine_list_with_symptoms.csv'
medicine_data = pd.read_csv(file_path)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Dictionary for symptom synonyms
synonyms = {
    "fever": ["high temperature", "pyrexia"],
    "cough": ["coughing"],
    "sore throat": ["throat pain", "pharyngitis"],
    "runny nose": ["rhinorrhea", "nasal discharge"],
    "stomach ache": ["abdominal pain", "tummy ache"],
    "nausea": ["queasiness"],
    "vomiting": ["throwing up"],
    "diarrhea": ["loose stools"],
    "itchy eyes": ["ocular pruritus"],
    "rash": ["skin eruption"],
    "shortness of breath": ["dyspnea", "breathlessness"],
    "burning sensation when urinating": ["dysuria"],
    "urinate urgently": ["frequent urination", "urgency"]
}

# Function to preprocess the symptoms text using spaCy
def preprocess_text(text):
    doc = nlp(text.lower())  # Convert text to lowercase and process with spaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]  # Extract lemmatized tokens excluding stop words and punctuation
    phrases = [chunk.text for chunk in doc.noun_chunks]  # Extract noun phrases
    return tokens + phrases  # Combine tokens and noun phrases

# Function to expand symptoms with synonyms
def expand_with_synonyms(symptoms, synonym_dict):
    expanded_symptoms = symptoms.copy()  # Copy original symptoms
    for symptom in symptoms:
        for key, values in synonym_dict.items():
            if symptom in values or symptom == key:
                expanded_symptoms.append(key)  # Add the key (main symptom)
                expanded_symptoms.extend(values)  # Add all synonyms
    return list(set(expanded_symptoms))  # Remove duplicates and return as a list

# Function to find medicines based on symptoms
def find_medicines(symptom, data, synonym_dict):
    processed_symptom = preprocess_text(symptom)  # Preprocess the input symptom text
    expanded_symptom = expand_with_synonyms(processed_symptom, synonym_dict)  # Expand symptoms with synonyms
    
    # Filter matches
    matches = pd.DataFrame()  # Initialize an empty DataFrame for matches
    for word in expanded_symptom:
        word_matches = data[data['Indications (Symptoms)'].apply(lambda x: isinstance(x, str) and word in x)]  # Find rows where symptoms match
        matches = pd.concat([matches, word_matches])  # Concatenate matches to the DataFrame
    
    # Ensure only related medicines are shown
    if not matches.empty:
        matches = matches.drop_duplicates(subset=['Brand Name', 'Medicine Type', 'Strength', 'Generic Name', 'Drug Class', 'Manufacturer'])
    
    return matches[['Brand Name', 'Medicine Type', 'Strength', 'Generic Name', 'Drug Class', 'Manufacturer', 'Indications (Symptoms)']]  # Return relevant columns

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []  # Initialize chat history in session state

if 'temp_input' not in st.session_state:
    st.session_state.temp_input = ""  # Initialize temporary input in session state

def med_chatbot():
    st.title("MedChatBot")  # Set the title of the Streamlit app

    with st.sidebar:
        st.header("Common Symptoms")
        if st.button("Fever and Cough"):
            st.session_state.temp_input = "Fever, Cough" # Set pre-defined input for Fever, Cough
        if st.button("Headache"):
            st.session_state.temp_input = "Headache" # Set pre-defined input for Headache
        if st.button("Itching"):
            st.session_state.temp_input = "Itching" # Set pre-defined input for Itching
        if st.button("Skin Rash"):
            st.session_state.temp_input = "Rash"  # Set pre-defined input for Rash

    # Temporary variable to hold user input
    temp_user_input = st.text_input("Describe your symptoms:", value=st.session_state.temp_input, key='user_input')  # Get user input with pre-defined values if any

    # Clear history button
    if st.button("Clear History"):
        st.session_state.history = []  # Clear chat history
        st.session_state.temp_input = ""  # Clear temporary input
        st.experimental_rerun()  # Rerun the script to reload the page

    # Process user input
    if temp_user_input:
        st.session_state.history.append({"type": "user", "message": temp_user_input})  # Append user input to chat history
        results = find_medicines(temp_user_input, medicine_data, synonyms)  # Find medicines based on user input
        if not results.empty:
            st.session_state.history.append({"type": "bot", "message": results})  # Append results to chat history if matches found
        else:
            response = "No medicines found for the given symptoms. Please try describing your symptoms differently or more specifically."
            st.session_state.history.append({"type": "bot", "message": response})  # Append response if no matches found
        
        # Clear input after submission
        st.session_state.temp_input = ""  # Clear temporary input after processing

    # Display chat history
    for chat in st.session_state.history:
        if chat["type"] == "user":
            st.markdown(f"**You:** {chat['message']}")  # Display user message
        else:
            if isinstance(chat['message'], pd.DataFrame):
                st.markdown(f"**MedChatBot:** Here are some medicines that might help:")
                st.dataframe(chat['message'])  # Display DataFrame of medicines
            else:
                st.markdown(f"**MedChatBot:** {chat['message']}")  # Display bot response

if __name__ == "__main__":
    med_chatbot()  # Run the med_chatbot function
