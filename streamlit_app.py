import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyBPLV8i1farv2S4T99VltnyHfZrDxyjg24")

model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(Input,Image,prompt):
    response=model.generate_content([Input,Image[0],prompt])
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    
st.set_page_config("Prachi's invoice generator")
st.sidebar.header('RoboBill')
st.sidebar.write("Made by Prachi")
st.sidebar.write('powered by google gemini')
st.header("RoboBill")
st.subheader("Made by Prachi")
st.subheader("manage your expenses with RoboBill")
input= st.text_input("what do you want me to do?",key="input")
uploaded_file = st.file_uploader("choose an image",type=["jpg.", "jpeg", "png"])
image= ""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)
    
ssubmit=st.button("Let's Go!")
    
input_prompt = """
    you are an expert at calculus. please solve the question uploaded and give the solution in a
    detailed manner.
    """
    #button prog
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)

#thanks for visiting!
