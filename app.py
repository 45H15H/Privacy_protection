import streamlit as st

import numpy as np

import cv2

from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# take image input from user
uploaded_file = st.file_uploader("Upload Image")

# wait for the user to upload an image
if uploaded_file is not None:

    original_image = Image.open(uploaded_file)

    # convert the original image such that it can be processed by opencv
    opencv_image = np.array(original_image.convert('RGB'))

    # convert the image into grayscale
    gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))

    # draw a rectangle around the face
    for (x, y, w, h) in faces:
        # draw a rectangle around the face
        cv2.rectangle(opencv_image, (x, y), (x+w, y+h), (255, 255, 0), 2)
        # fill the rectangle with black color arond the eyes
        cv2.rectangle(opencv_image, (x+int(w/6), y+int(h/5)),
                      (x+w-int(w/6), y+h-int(h/2)), (0, 0, 0), -1)

    # display the output image
    st.image(opencv_image, caption="Face Detection", use_column_width=True)






# if image is not None:
#     image_ = str(image)
#     img = cv2.imread(image_, 1) # read image in BGR format

#     # resize the image
#     img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

#     # convert image to grayscale
#     gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # detect faces
#     faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))

#     # draw a rectangle around the face
#     for (x, y, w, h) in faces:
#         # draw a rectangle around the face
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
#         # fill the rectangle with black color arond the eyes
#         cv2.rectangle(img, (x+int(w/6), y+int(h/5)),
#                       (x+w-int(w/6), y+h-int(h/2)), (0, 0, 0), -1)

# # display the output image
# st.image(img, caption="Face Detection", use_column_width=True)

# # give download option
# cv2.imwrite("output.jpg", img)

# st.download_button(label="Download", data="output.jpg", file_name="output.jpg")