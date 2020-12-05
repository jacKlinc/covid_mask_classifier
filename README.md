# COVID-19 Mask Detector
Upload a picture of someone to determine whether or not they're wearing a mask. Uses model trained using FastAI and image data retreived via Bing Search API.  

The notebook used to train the model used on streamlit is ```notebooks/mdl_train-mask-classifier.ipynb```. I recommend using a cloud GPU to save time.

[![Streamlit](https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e0a328bedb754beb8a973f9_logomark_website.png)](https://share.streamlit.io/jacklinc/covid_mask_classifier/main/src/src_bear-class.py)


## Beard Skew
So I sent my friend the link to my live web app to classify images into the mask and non-mask categories. He has a beard. The model didn't like this and said he had a mask when he didn't. This is an interesting issue as it could reappear in the form of ethnicity or gender.

The next step is to tell the model to recognise that our bushy friends are not wearing a mask. I added a new category: beards, this helped the model distinguish the two.