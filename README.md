# Image Anonymizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://privacy-protection.streamlit.app/)

## Description

This is a simple Streamlit app that allows users to upload an image and apply one of three filters to anonymize faces in the image. The filters are:

- Blur: applies a Gaussian blur to  the faces in the image
- Black Rectangle: covers the eyes of the faces in the image with a black rectangle

## Installation

To run the app, you'll need to have Python 3 and pip installed. You can install the required Python packages by running:

```console
pip3 install -r requirements.txt
```

## Usage

To run the app, simply run the following command:

```console
streamlit run app.py
```
This will start the app and open it in your default web browser. You can then upload an image and choose a filter to apply.

## Libraries Used

This app uses the following open-source libraries:

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

