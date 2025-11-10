import streamlit as st
import google.generativeai as genai

# -----------------------------
# APP CONFIGURATION
# -----------------------------
st.set_page_config(page_title="AI Career Guidance Assistant", page_icon="🎯", layout="centered")

st.title("🎯 AI Career Guidance Assistant")
st.write("This AI-powered app helps you explore suitable career paths based on your interests and skills.")

# -----------------------------
# USER INPUT
# -----------------------------
name = st.text_input("Enter your name:")
interests = st.text_area(
    "Describe your interests and skills:", 
    placeholder="e.g. I like data analysis, coding, and creative problem-solving."
)
career_goal = st.text_input(
    "Enter your career goal (optional):", 
    placeholder="e.g. Data Scientist, Software Engineer, Product Manager"
)

# -----------------------------
# CONFIGURE GEMINI SDK
# -----------------------------
# Replace with your actual API key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Initialize the Gemini model
gemini_model = genai.GenerativeModel('gemini-2.5-flash')

# -----------------------------
# FUNCTION TO GENERATE CAREER GUIDANCE
# -----------------------------
def generate_career_guidance(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        # The response object has a .text attribute
        return response.text
    except Exception as e:
        return f"An error occurred while generating content: {e}"

# -----------------------------
# SUBMIT BUTTON
# -----------------------------
if st.button("Get Career Guidance"):
    if not interests.strip():
        st.warning("Please describe your interests and skills first.")
    else:
        with st.spinner("Analyzing your profile and generating guidance..."):
            prompt = (
                f"Based on the following interests and skills, suggest 3 suitable career paths. "
                f"For each path, include required skills and recommended learning resources.\n\n"
                f"Interests and skills: {interests}\n"
                f"Career goal: {career_goal if career_goal else 'Not specified'}"
            )
            result = generate_career_guidance(prompt)
        
        st.subheader(f"Career Guidance for {name if name else 'You'}:")
        st.write(result)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Developed by Clive Lawrence Xavier | Streamlit + Google Gemini SDK")
