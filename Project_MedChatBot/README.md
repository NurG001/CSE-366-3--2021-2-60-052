# MedChatBot

MedChatBot is a Streamlit-based application that provides medicine recommendations based on user-reported symptoms. The bot uses natural language processing to understand the symptoms and match them with a comprehensive list of medicines.

## Repository Contents

1. **MedChatBot.py**: The main Python script that runs the MedChatBot application.
2. **comprehensive_medicine_list_with_symptoms.csv**: The dataset containing the comprehensive list of medicines along with their associated symptoms.
3. **MedChatBot-Final-Project-Report.pdf**: The final project report documenting the development and functionality of the MedChatBot.
4. **instruction.txt**: Instructions on how to run the MedChatBot and install the necessary libraries.

## Getting Started

### Prerequisites

To run the MedChatBot, you need to have the following libraries installed:
- pandas
- streamlit
- spacy

You can install these libraries using pip:

```bash
pip install pandas streamlit spacy
python -m spacy download en_core_web_sm
```
Run the code using Streamlit:
```bash
streamlit run MedChatBot.py
```

## Usage
1. Enter your symptoms in the input field on the main page (Example: Cough, Fever).
2. Click on the predefined symptoms buttons on the sidebar for quick input(Optional).
3. View the recommended medicines based on your symptoms.
4. Clear the chat history if needed using the "Clear History" button.
