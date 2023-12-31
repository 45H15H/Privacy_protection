import streamlit as st

import numpy as np

import cv2

from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# change it to h2
st.markdown("<h2 style='text-align: center; color: red;'>Image Anonymizer</h2>", unsafe_allow_html=True)

st.caption("Protecting Privacy")


# take image input from user
uploaded_file = st.file_uploader("Upload Image", accept_multiple_files=False)

# choose between blur, pixelate and black rectangle
option = st.selectbox("Choose the type of filter", ("select","Blur", "Black Rectangle"), index=0)

# wait for the user to upload an image
if uploaded_file is not None:

    original_image = Image.open(uploaded_file)

    # convert the original image such that it can be processed by opencv
    opencv_image = np.array(original_image.convert('RGB'))

    # convert the image into grayscale
    gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))

    # if no option is selected
    if option == "select":
        st.warning("Please select an option from the dropdown menu")

    # if blur is selected
    elif option == "Blur":
        # draw a rectangle around the face
        for (x, y, w, h) in faces:
            # draw a rectangle around the face
            cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            # blur the face
            opencv_image[y:y+h, x:x+w] = cv2.blur(opencv_image[y:y+h, x:x+w], (61, 61))
        
    # if black rectangle is selected
    elif option == "Black Rectangle":
    # draw a rectangle around the face
        for (x, y, w, h) in faces:
            # draw a rectangle around the face
            cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            # fill the rectangle with black color arond the eyes
            cv2.rectangle(opencv_image, (x+int(w/6), y+int(h/5)), (x+w-int(w/6), y+h-int(h/2)), (0, 0, 0), -1)

    button = st.button("Generate")

    if button == True:
        # display the output image
        st.image(opencv_image, caption="masked face", use_column_width=True)
        
        # convert the image into RGB format
        rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        
        cv2.imwrite("masked_face.jpg", rgb_image)

        # success message
        st.success("Image Generated Successfully")

    # now download the image
    st.download_button(label="Download", data=open("masked_face.jpg", "rb").read(), file_name="masked_face.jpg", mime="image/jpg")

