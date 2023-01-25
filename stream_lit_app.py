import streamlit as st
import os
import requests
import numpy
from urllib.error import URLError
from streamlit_image_select import image_select

st.title('My Parents New Healthy Diner')
list_imgs = []
def ubdate_selector():
    global list_imgs
    list_imgs = [f"./images/{i}" for i in os.listdir(r"./images")]
    # return list_imgs

# img = st.empty()
ubdate_selector()
img = image_select("Label", list_imgs)

st.image(img)

def save_uploadedfile(uploadedfile):
    path_new_file = os.path.join("images",uploadedfile.name)
    with open(path_new_file,"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to images".format(path_new_file.split('/'[-1])))



image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    save_uploadedfile(image_file)
    ubdate_selector()
