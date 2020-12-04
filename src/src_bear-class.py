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

'## COVID-19 Mask Classifier'
'Upload a picture of someone'
learner_inf = load_learner('./covid_mask.pkl')

# Upload
pic = st.file_uploader("Upload Files")

'Click Classify to find out if there wearing a mask'

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
    if str(pred) == 'peoples faces':
        pred = 'no mask'
    else:
        pred = 'has mask'
    'Prediction: ', pred
    'Probability: ', str(round(probs[pred_idx].item(), 5))