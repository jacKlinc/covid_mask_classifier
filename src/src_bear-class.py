from fastai.learner import load_learner
from fastai.vision.core import PILImage

import streamlit as st
from PIL import Image

# @st.cache
def load_image(image):
    return Image.open(image)

def predict_img(img):
    if img is not None:
        return learner_inf.predict(pil_img)

'Import the pickle file'
learner_inf = load_learner('./export.pkl')

# Upload
pic = st.file_uploader("Upload Files")

probs = []
pred_idx = 1
pred = 'n/a'

# Display image
if pic is not None:
    img = load_image(pic)
    st.image(img)
    
    # Parse image
    pil_img = PILImage.create(pic)

    # Predict category
    pred,pred_idx,probs = predict_img(pil_img)

# Classify
if st.button('Classify'):
    'Prediction: ', pred 
    'Probability: ', probs[pred_idx].item()