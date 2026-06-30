# 🎓 Student Helpdesk Bot

## 📌 Project Overview

Student Helpdesk Bot is an AI-powered conversational assistant developed as part of the INNOVIAST AI Solutions Engineering Internship (Week 1 Assignment).

The chatbot assists students by answering questions related to university student services such as admissions, course registration, tuition fees, scholarships, timetables, and campus facilities. It also politely refuses to answer questions outside its defined scope.

---

## ✨ Features

- AI-powered student helpdesk assistant
- Clean and interactive Streamlit chat interface
- Conversation memory
- Quick question buttons
- Reliable fallback behavior for out-of-scope questions
- Basic error handling
- New Chat functionality
- Sidebar with chatbot information
- Powered by Ollama using Llama 3.2

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Ollama
- Llama 3.2
- OpenAI Python SDK (used to communicate with Ollama's local API)

---

## 📂 Project Structure

```text
StudentHelpdeskBot-InnoViast/
│
├── app.py
├── chatbot.py
├── prompts.py
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── screenshots/
└── assets/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/StudentHelpdeskBot-InnoViast.git
```

### 2. Navigate to the project

```bash
cd StudentHelpdeskBot-InnoViast
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/download

### 5. Download the model

```bash
ollama pull llama3.2
```

### 6. Start Ollama

```bash
ollama serve
```

### 7. Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

https://drive.google.com/file/d/1YTgvMNO__StOnYb4ohAU-XiKjFCK_YkC/view?usp=drive_link

---

## 🎥 Demo Video

https://drive.google.com/file/d/1Ys1HH-A-WqoH7G4y4oaaNRk_jZlJuRy-/view?usp=drive_link

---

## 📌 Future Improvements

- University-specific knowledge base
- User authentication
- Voice interaction
- Multi-language support

---

## 👨‍💻 Developer

**Abdullah Javed**

Developed for the **INNOVIAST AI Solutions Engineering Internship – Week 1 Assignment**.
