import streamlit as st
from chatbot import get_chatbot_response

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Student Helpdesk Bot",
    page_icon="🎓",
    layout="centered"
)

# ----------------------------
# SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:

    st.title("🎓 Student Helpdesk")

    st.write("### I can help with")

    st.markdown("""
- 📋 Admissions
- 📚 Course Registration
- 💰 Tuition Fees
- 🎓 Scholarships
- 🏫 Campus Services
- 🕒 Office Hours
""")

    st.divider()

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    st.divider()

    with st.expander("About"):

        st.write("""
This chatbot answers questions about:

- Admissions
- Fees
- Scholarships
- Courses
- Campus Services

Powered by **Ollama (Llama 3.2)**.
""")

    st.divider()

    if st.button("🗑️ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ----------------------------
# TITLE
# ----------------------------

st.markdown(
    """
<h1 class="main-title">
🎓 Student Helpdesk Bot
</h1>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<p class="subtitle">
Ask questions about admissions, fees,
scholarships, course registration and campus services.
</p>
""",
    unsafe_allow_html=True
)

# ----------------------------
# WELCOME
# ----------------------------

if len(st.session_state.messages) == 0:

    st.info("""
👋 **Welcome!**

I'm your Student Helpdesk Assistant.

I can help you with:

- Admissions
- Course Registration
- Tuition Fees
- Scholarships
- Campus Services
- Timetables

Choose a quick question below or ask your own.
""")

# ----------------------------
# QUICK QUESTIONS
# ----------------------------

quick_question = None

if len(st.session_state.messages) == 0:

    st.subheader("🚀 Quick Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📋 Admissions", use_container_width=True):
            quick_question = "How do I apply for admission?"

        if st.button("🎓 Scholarships", use_container_width=True):
            quick_question = "What scholarships are available?"

        if st.button("🏫 Campus Services", use_container_width=True):
            quick_question = "What campus services are available?"

    with col2:

        if st.button("💰 Tuition Fees", use_container_width=True):
            quick_question = "How can I pay my tuition fees?"

        if st.button("📚 Course Registration", use_container_width=True):
            quick_question = "How do I register for courses?"

# ----------------------------
# PROCESS QUICK QUESTION
# ----------------------------

if quick_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": quick_question
        }
    )

    with st.spinner("Thinking..."):

        response = get_chatbot_response(
            st.session_state.messages
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()

# ----------------------------
# CHAT HISTORY
# ----------------------------

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(
            message["content"].replace("\n", "\n\n")
        )

# ----------------------------
# USER INPUT
# ----------------------------

user_input = st.chat_input(
    "Ask your question..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(user_input)

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner("Thinking..."):

            response = get_chatbot_response(
                st.session_state.messages
            )

            st.markdown(
                response.replace("\n", "\n\n")
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ----------------------------
# FOOTER
# ----------------------------

st.divider()

st.caption(
    "Built by Abdullah Javed • Streamlit • Ollama • Llama 3.2"
)