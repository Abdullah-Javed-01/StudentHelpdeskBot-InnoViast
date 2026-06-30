from openai import OpenAI
from prompts import SYSTEM_PROMPT

# Connect to local Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# Keywords related to the chatbot's domain
STUDENT_KEYWORDS = [
    "admission", "admissions",
    "course", "courses",
    "registration", "register",
    "fee", "fees", "tuition",
    "scholarship", "scholarships",
    "student", "students",
    "campus",
    "library",
    "hostel",
    "office",
    "faculty",
    "timetable",
    "schedule",
    "exam",
    "semester",
    "department",
    "helpdesk",
    "service",
    "services"
]

FALLBACK_RESPONSE = """
I'm a **Student Helpdesk Assistant**, so I can only answer questions related to:

- Admissions
- Course Registration
- Tuition & Fees
- Scholarships
- Timetables
- Campus Services
- Student Services

Please ask a question about one of these topics.
"""

def is_in_scope(message):
    message = message.lower()

    return any(keyword in message for keyword in STUDENT_KEYWORDS)


def get_chatbot_response(chat_history):

    # Latest user message
    latest_message = chat_history[-1]["content"]

    # Check if the question is in scope
    if not is_in_scope(latest_message):
        return FALLBACK_RESPONSE

    try:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(chat_history)

        response = client.chat.completions.create(
            model="llama3.2:latest",
            messages=messages,
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"