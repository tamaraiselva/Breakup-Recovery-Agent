
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def setup_page():
    st.set_page_config(
        page_title="Breakup Recovery Assistant",
        page_icon="💔",
        layout="wide"
    )

    st.markdown("""
        <style>
        .stTextInput>div>div>input {
            background-color: #ffffff;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #ff3333;
        }
        </style>
        """, unsafe_allow_html=True)

def display_header():
    st.title("💔 Breakup Recovery Assistant")
    st.markdown("""
        Welcome to your personal breakup recovery assistant. Share your feelings, get support,
        and receive personalized guidance to help you through this difficult time.
    """)

def display_support_sections(data):
    try:
        sections = [
            {"key": "therapist", "title": "🤝 Therapist's Support"},
            {"key": "closure", "title": "✉️ Closure Guidance"},
            {"key": "routine", "title": "📅 7-Day Recovery Plan"},
            {"key": "honesty", "title": "💪 Honest Feedback"}
        ]

        for section in sections:
            try:
                section_key = section["key"]
                section_title = section["title"]

                if section_key in data and "data" in data[section_key]:
                    section_content = data[section_key]["data"]
                    with st.expander(section_title, expanded=False):
                        st.markdown(section_content)
                else:
                    with st.expander(section_title, expanded=False):
                        st.warning(f"No data available for {section_title}")

            except Exception as e:
                with st.expander(section_title, expanded=False):
                    st.error(f"Error displaying {section_title}: {str(e)}")

    except Exception as e:
        st.error(f"Error displaying support sections: {str(e)}")

def process_user_input(user_input, uploaded_files):
    try:
        api_key = os.getenv("API_KEY")
        deployed_api_url = os.getenv("API_URL")
        api_url = deployed_api_url if deployed_api_url else "http://localhost:8000/analyze/"

        if not api_key:
            st.error("Missing API_KEY in .env file. Please check your configuration.")
            st.stop()
        if not user_input or not user_input.strip():
            st.error("Please provide some text about how you're feeling.")
            return None

        files = []
        if uploaded_files:
            try:
                for file in uploaded_files:
                    try:
                        file_content = file.getvalue()
                        files.append(("files", (file.name, file_content, file.type)))
                    except Exception as file_error:
                        st.warning(f"Could not process file {file.name}: {str(file_error)}")
                        continue
            except Exception as files_error:
                st.warning(f"Issue with uploaded files: {str(files_error)}")
        try:
            # Removed the connection message
            response = requests.post(
                api_url,
                data={
                    "user_input": user_input
                },
                files=files,
                timeout=120
            )
            if response.status_code == 200:
                try:
                    results = response.json()
                    if results.get("success", False):
                        if "data" in results:
                            return results["data"]
                        else:
                            st.error("API response is missing data field")
                    else:
                        error_msg = results.get("error", "Unknown error")
                        st.error(f"API returned an error: {error_msg}")
                except ValueError as json_error:
                    st.error(f"Could not parse API response as JSON: {str(json_error)}")
            else:
                st.error(f"API request failed with status code {response.status_code}: {response.text}")

        except requests.exceptions.Timeout:
            st.error("API request timed out. Please try again later.")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. Please check your internet connection.")
        except requests.exceptions.RequestException as req_error:
            st.error(f"API request error: {str(req_error)}")

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
    return None

def display_recovery_tips():
    st.subheader("Tips for Recovery")
    st.markdown("""
    - Allow yourself to feel your emotions
    - Practice self-care daily
    - Stay connected with friends and family
    - Focus on personal growth
    - Set new goals and challenges
    - Consider professional help if needed
    """)

def main():
    try:
        setup_page()
        display_header()

        try:
            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("How are you feeling?")
                user_input = st.text_area(
                    "Share your thoughts and feelings...",
                    height=150,
                    placeholder="I'm feeling..."
                )

                uploaded_files = st.file_uploader(
                    "Upload images (optional)",
                    type=["jpg", "jpeg", "png"],
                    accept_multiple_files=True
                )

                results_container = st.container()

                if st.button("Get Support"):
                    if not user_input or not user_input.strip():
                        st.error("Please share how you're feeling")
                    else:
                        with st.spinner("Analyzing your feelings and preparing support..."):
                            try:
                                data = process_user_input(user_input, uploaded_files)

                                if data:
                                    with results_container:
                                        display_support_sections(data)
                                else:
                                    st.warning("Could not generate support content. Please try again.")
                            except Exception as process_error:
                                st.error(f"Error processing your input: {str(process_error)}")

            with col2:
                try:
                    display_recovery_tips()
                except Exception as tips_error:
                    st.error(f"Error displaying recovery tips: {str(tips_error)}")

        except Exception as layout_error:
            st.error(f"Error with page layout: {str(layout_error)}")

        st.markdown("---")
        st.markdown("""
            <div style='text-align: center'>
                <p>Remember: Healing takes time. Be patient with yourself.</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("An unexpected error occurred in the application.")
        st.error(f"Error details: {str(e)}")

        if st.button("Restart Application"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
