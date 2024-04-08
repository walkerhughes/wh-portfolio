import joblib 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import io 

def generate(kde): 

    new_image = kde.sample()
    reshaped = new_image.reshape(24, 24, 4).astype(np.float64)/255

    plt.figure(figsize=(10, 6), dpi=300)  
    plt.imshow(reshaped)  
    plt.axis("off")

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    buf.seek(0)

    st.image(
        buf, 
        use_column_width = True, 
        clamp = True, 
        caption = "Image created by randomly sampling estimated pixel distribution from KDE model"
    )