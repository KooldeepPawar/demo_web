import streamlit as st


name = st.text_input("Enter your Name ")
fname = st.text_input("Enter your Father's Name ")
Address = st.text_input("Enter your Complete Address ")

classdata = st.selectbox("Enter your class ",(1,2,3,4,5,5))
button = st.button("Done")

if button :
    st.markdown(f"name : {name} Father Name : {fname} Address : {Address} Class : {classdata}")



