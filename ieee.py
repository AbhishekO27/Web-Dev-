import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="IEEE Hackathon", page_icon=":robot_face:", layout="wide")


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottie("https://assets10.lottiefiles.com/packages/lf20_tfb3estd.json")


st.title("Welcome to the IEEE Hackathon :rocket:")
st.write("Explore innovation, learn new skills, and collaborate to solve real-world challenges.")


st.write("[📘 Learn More About IEEE](https://www.ieee.org) | [🌟 Explore Projects](https://github.com) | [🤝 Join Us](https://www.ieee.org/membership/join/index.html)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Why Participate in the Hackathon?")
        st.write("###")
        st.write(
            """
            - Collaborate with passionate individuals.
            - Solve problems using AI, ML, and cloud technologies.
            - Gain hands-on experience in cutting-edge fields.
            - Compete and learn from the best.
            """
        )
        st.write("### [🛠️ View Rules and Guidelines](https://www.ieee.org/communities/index.html)")
    
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Failed to load animation. Please check the URL.")


with st.container():
    st.write("---")
    st.header("Register for the Hackathon :memo:")
    st.write("###")

  
    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        organization = st.text_input("Organization/College")
        idea = st.text_area("Briefly describe your hackathon idea or area of interest")
        submitted = st.form_submit_button("Register")

      
        if submitted:
            if name and email:
                st.success(f"Thank you, {name}! You have successfully registered.")
            else:
                st.error("Please fill out all required fields!")


with st.container():
    st.write("---")
    st.subheader("Connect with Us!")
    st.write(
        """
        Have questions or suggestions? Reach out:
        - 📧 Email: hackathon@ieee.org
        - 🌐 Website: [IEEE Official Website](https://www.ieee.org)
        - 📱 Social Media: [LinkedIn](https://linkedin.com) | [Twitter](https://twitter.com)
        """
    )
