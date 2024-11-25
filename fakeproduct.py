import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Fake Review Detection System",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_main = load_lottie("https://lottie.host/7da1cac5-120f-4e4e-8efa-4e641018cfd2/eiJQdParg2.json")
lottie_form = load_lottie("https://lottie.host/bf1145e7-3365-4c0a-9dd3-4afc1b133cb4/kZCc6JrXUX.json")


st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a section:", ["About the Project", "Try the Detection System", "Team and Contact"])


st.markdown(
    """
    <style>
        .header {
            text-align: center;
            color: #4CAF50;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<h1 class="header">Fake Product Review Detection System</h1>', unsafe_allow_html=True)
st.write("**An initiative by Team MLDev** to enhance online shopping experiences using AI and ML.")


if options == "About the Project":
    st.write("---")
    st.header("About the Project")
    
    with st.container():
        left_column, right_column = st.columns(2)
        
        with left_column:
            st.subheader("The Problem")
            st.write(
                """
                Fake reviews can mislead customers and harm businesses:
                - Sellers post fake positive reviews to boost sales.
                - Competitors post fake negative reviews to harm reputations.
                """
            )
            st.subheader("Our Solution")
            st.write(
                """
                - Use NLP and ML algorithms to detect fake reviews.
                - Ensure genuine feedback for better customer experiences and product development.
                """
            )
        
        with right_column:
            if lottie_main:
                st_lottie(lottie_main, height=400, key="main")
            else:
                st.error("Failed to load animation.")

elif options == "Try the Detection System":
    st.write("---")
    st.header("Try the Fake Review Detection System")
    
    with st.container():
        st.subheader("Analyze a Review or Upload a Dataset")
        left_column, right_column = st.columns([2, 1])
        
        with left_column:
            with st.form("detection_form"):
                review_input = st.text_area("Enter a product review:")
                dataset_upload = st.file_uploader("Or upload a CSV file with reviews:", type=["csv"])
                submitted = st.form_submit_button("Analyze")
                
                if submitted:
                    if review_input:
                        st.success(f"Analyzing the review: {review_input}")
                        # ML yaha par integrate hoga
                    elif dataset_upload:
                        st.success("Dataset uploaded successfully! Analysis will begin shortly.")
                        # Data set inetegration
                    else:
                        st.error("Please provide a review or upload a dataset.")
        
        with right_column:
            if lottie_form:
                st_lottie(lottie_form, height=250, key="form")
            else:
                st.error("Failed to load animation.")

elif options == "Team and Contact":
    st.write("---")
    st.header("Meet the Team")
    
    with st.container():
        st.write("### Team MLDev")
        st.write(
            """
            - **Dev Goyal (Team Leader)**  
              Email: gdev6886@gmail.com | Phone: 7617641909
            - **Abhishek Bora**  
              Email: Abhishekbora244@gmail.com | Phone: 6397588606
            - **Aditya Prakash**  
              Email: adityaprakash7968@gmail.com | Phone: 9546831797
            """
        )
    st.write("### Contact Us")
    st.write("Have questions or want to collaborate? Reach out to us at **hackathon@ieee.org**.")


st.write("---")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        &copy; 2024 Team MLDev | Made with ❤️ and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
