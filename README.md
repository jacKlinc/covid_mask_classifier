# COVID-19 Mask Detector
Upload a picture of someone to determine whether or not they're wearing a mask. Uses model trained using FastAI and image data retreived via Bing Search API.  

The notebook used to train the model used on streamlit is ```notebooks/mdl_train-mask-classifier.ipynb```. I recommend using a cloud GPU to save time.

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/jacklinc/covid_mask_classifier/main/src/src_bear-class.py)


Here's the Medium [article](https://jack-harding.medium.com/mask-detector-w-fastai-and-streamlit-sharing-62448b4cb7b6).

## Beard Skew
So I sent my friend the link to my live web app to classify images into the mask and non-mask categories. He has a beard. The model didn't like this and said he had a mask when he didn't. This is an interesting issue as it could reappear in the form of ethnicity or gender.

The next step is to tell the model to recognise that our bushy friends are not wearing a mask. I added a new category: beards, this helped the model distinguish the two.
