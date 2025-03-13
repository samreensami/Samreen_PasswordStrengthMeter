import re
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS for background color
st.markdown(
    """
    <style>
    /* Background color for full page */
    .stApp {
        background-color: lightblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔏 Password Strength Checker")
st.markdown("""
## Welcome To Password Strength Checker!🛠  
This password strength checker tool helps you evaluate the security of your password ✨
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) > 8:
        score += 1

else:
    feedback.append("🥵 password should be atleast 8 charactors long.")

if re.search(r'[A-Z]',password) and re.search(r'a-z' , password):

    score += 1
else:
    feedback.append("😡 password should be contain both upper and lower case.")

if re.search(r'[!@#$%^&*]',password):
    score += 1
else:
    feedback.append("🤬 password should contain at least one special character(!@#$%^&*).")

if score == 4:
    feedback.append("🔒 your password is strong!🎉")
elif score == 3:
    feedback.append("your password is medium strenth. It could be strong.")
else:
    feedback.append("❌your password is weak. Please make it stronger.")
if feedback:
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
else:
    st.info("✨Please enter your password to get started.")        


