import numpy as np
from PIL import Image
import cv2
import streamlit as st
import io

st.header("welcome to image resizer ")  
img=st.file_uploader("upload image",type=["jpg","png","jpeg"])
if img:
    img=Image.open(img)
    arr_img=np.array(img)
    st.image(arr_img,caption=["original image"],width=100)
    
    width=st.number_input("enter width",min_value=1,value=arr_img.shape[1])
    height=st.number_input("enter height",min_value=1,value=arr_img.shape[0])

    flip_value=st.selectbox("Direction",["None","Vertical","Horizontal"])

    if flip_value=="Vertical":
        flip_image=cv2.flip(arr_img,0)
        arr_img=flip_image

    elif flip_value:
        flip_image=cv2.flip(arr_img,1)
        arr_img=flip_image
    st.image(arr_img,caption="flipped image",width=100)



    if st.button("resize"):
        resized_img=cv2.resize(arr_img,(int(width),int(height)))
        st.image(resized_img,caption="resized image",width=150)

        buff=io.BytesIO()
        img_pil=Image.fromarray(resized_img)
        img_pil.save(buff,format="jpeg")
        st.download_button("download resized image",data=buff.getvalue(),file_name="resized_image.jpg",mime="image/jpeg")