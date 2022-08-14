import streamlit as st
from streamlit_ace import st_ace

st.title("Hello Streamlit ACE Code Editor")

st.write(f"Demo self-editing file: {__file__}")

# use st.form:
# with st.form(key="ace_editor"):
#     content = st_ace(
#         value=open(__file__).read(),
#         language = 'python',
#         theme = 'pastel_on_dark',
#         readonly  = False)
#     if st.form_submit_button("Save"):
#         with open(__file__, "w") as f:
#             f.write(content)

# No need to use st.form
content = st_ace(
        value=open(__file__).read(),
        language = 'python',
        theme = 'pastel_on_dark',
        readonly  = False)
if content:
    open(__file__, "w").write(content)


with st.expander("Show code"):
    st.code(open(__file__).read())