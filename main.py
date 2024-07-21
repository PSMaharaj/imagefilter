import streamlit as st
import cv2
import numpy as np
from PIL import Image

def photo():
    camera = cv2.VideoCapture(0)
    button_count=0
    while True:
        ret, image = camera.read()
        if ret:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_placeholder.image(image, channels="RGB")
            button_k=f'capture_button{button_count}'
            button_count+=1
            if st.button('Capture', key='button_k'):
                cv2.imwrite('opencv.png', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                break
    camera.release()
    cv2.destroyAllWindows()

def sketch():
    image = cv2.imread("opencv.png")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=200.0)
    return pencil_sketch

st.title("Photo to Pencil Sketch App")

if st.button('Start Camera'):
    img_placeholder = st.empty()
    photo()

if 'opencv.png' in st.session_state:
    if st.button('Generate Sketch'):
        pencil_sketch_image = sketch()
        st.image(pencil_sketch_image, caption='Pencil Sketch', use_column_width=True)
else:
    st.info("Capture a photo first")