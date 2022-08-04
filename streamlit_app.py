import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('db.jpg'))

st.header('Avinash ')

st.info('Python and Azure  Advocate, Udemy Content Creator  with an interest in Cloud and Full Stack')

icon_size = 20

st_button('youtube', 'https://youtube.com/channel/UC5ASIl3Js_XSsb95sedH5kQ', 'Leet Code Solutions YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/edtech_nash/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/anantharamuavinash/', 'Follow me on LinkedIn', icon_size)
st_button('udemy', 'https://www.udemy.com/user/avinasha2/', 'Check my udemy store', icon_size)

 