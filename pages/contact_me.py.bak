import streamlit as st  # pip install streamlit
import requests,time
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/anantharamu.avinash@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <input type="hidden" name="_next" value="https://naashonomics-streamlit-cloud-streamlit-app-tgu0tp.streamlitapp.com">
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		

local_css("pages/contact_form_style.css")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_url_hello = "https://assets3.lottiefiles.com/private_files/lf30_vrcurbxk.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")