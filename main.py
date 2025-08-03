import streamlit as st

st.set_page_config(page_title="Toolbelt", page_icon="logo.png")

logo, title = st.columns([1,5])

with logo:
    st.image("logo.png", width=100)
with title:
    st.title("Mitchware Toolbelt")
    github, linkedin, streamlit, space = st.columns([1,1,1,1.5])
    with github:
        st.link_button("GitHub", url='https://github.com/mitchtasso', icon='💻', use_container_width=True)
    with linkedin:
        st.link_button("LinkedIn", url='https://www.linkedin.com/in/mitchell-tasso-91504a283', icon='💼', use_container_width=True)
    with streamlit:
        st.link_button("Streamlit", url='https://share.streamlit.io/user/mitchtasso', icon='🐍', use_container_width=True)
    with space:
        st.write("")

description = st.container(border=True)
description.write("Hello, welcome to my toolbox! " \
"This is a list of all my web apps deployed with Streamlit. " \
"I have also included my GitHub for source code, LinkedIn for connections and my Streamlit profile for an overview. " \
"Thank you for checking my page out!")

t = st.container(border=True)
tools, applications = t.columns(2)
with tools:
    st.subheader("Tools:")
    st.link_button(label="Password Generator", url="https://mitchware-passwordgenerator.streamlit.app/")
    st.link_button(label="QR Code Generator", url="https://mitchware-qr-code-generator.streamlit.app/")
with applications:
    st.subheader("Applications:")
    st.link_button(label="RepRange", url="https://reprange.streamlit.app/")
