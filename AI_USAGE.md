# AI Usage Documentation

## AI Tool Used

- Ollama
- Llama 3.2
- ChatGPT (used during development and guidance)

---

## Purpose of AI

The AI model powers the Student Helpdesk Bot by generating conversational responses for student-related questions.

The chatbot is designed to answer only questions related to:

- Admissions
- Course Registration
- Tuition Fees
- Scholarships
- Timetables
- Campus Services

---

## System Prompt

The chatbot uses a system prompt to define:

- Assistant persona
- Scope of knowledge
- Professional tone
- Honest responses
- Fallback behavior

---

## Prompt Engineering

The following improvements were made:

- Defined chatbot persona
- Restricted responses to student services
- Added conversation memory
- Improved response formatting
- Added reliable fallback behavior
- Reduced hallucinations by preventing out-of-scope responses

---

## Manual Improvements

The following features were implemented manually:

- Streamlit chat interface
- Sidebar
- Quick question buttons
- Conversation history
- New Chat functionality
- Loading spinner
- Error handling
- Scope checking using keywords
- Custom UI styling

---

## Limitations

- Uses a local AI model instead of a university database
- Cannot access real-time university information
- Does not browse the internet
- Responses depend on the capabilities of the Llama 3.2 model

---

## Data Ethics

- No personal user data is stored.
- No API keys are included in the repository.
- The chatbot clearly states its limitations.
- The assistant avoids generating information outside its intended scope.
