import streamlit as st
import re  
import string
import random

# Browser tab Title 
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

# Title for web app 
st.title("🗝 Password Strength Checker")

# Sidebar section
st.sidebar.title("⚙️ Features")

# Store previous passwords and generated password
if "previous_passwords" not in st.session_state:
    st.session_state.previous_passwords = []

if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

# Markdown is a way for representing text
st.markdown("""Welcome to my  **Welcome to My Password Strength Meter App! 🔒💪** """)

# Subheading
st.markdown("## 🔹 Suggestions for Next Sections:")

# Next Section (Password Strength Rules)
st.markdown("""
##### ✅ Password Strength Rules

Display rules like:
- ✅ Minimum **8** characters  
- ✅ At least **one uppercase** letter  
- ✅ At least **one number**  
- ✅ At least **one special character**  
""")    

# Function to check password strength
def check_password_strength(password):
    if len(password) < 6:
        return "😞 Weak", "red"
    elif len(password) < 8 or not any(char.isdigit() for char in password):
        return "🤔 Medium", "orange"
    elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
        return "💪 Strong", "green"
    else:
        return "🤨 Fair", "blue"

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(chars, k=length))



# Password Input Field (Pre-fills if a strong password is generated)
password = st.text_input("🔑 Enter your password:", value=st.session_state.generated_password, type="password")

# Button to generate strong password
if st.button("🔄 Generate Strong Password"):
    st.session_state.generated_password = generate_strong_password()

# Show strength result
if password:
    strength, color = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:20px'>{strength}</span>", unsafe_allow_html=True)

    # Store password in history (Only keep last 5 passwords)
    if password not in st.session_state.previous_passwords:
        st.session_state.previous_passwords.append(password)
        if len(st.session_state.previous_passwords) > 5:
            st.session_state.previous_passwords.pop(0)  # Remove oldest password

# Sidebar: Previous Passwords
st.sidebar.write("### 🕒 Previous Passwords")
if st.session_state.previous_passwords:
    for prev_pwd in st.session_state.previous_passwords:
        st.sidebar.code(prev_pwd, language="plaintext")
else:
    st.sidebar.write("No previous passwords entered.")
