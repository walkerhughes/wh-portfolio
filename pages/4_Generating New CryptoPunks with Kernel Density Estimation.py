import io 
import joblib 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

from utils.page6_utils import generate

st.set_page_config(
    page_title="Generating \'CryptoPunks\'", 
    page_icon=":robot_face:"
)

st.title(":robot_face: Generating CryptoPunk-like Images with Kernel Density Estimators")

kde = joblib.load("./models/kde_model_compressed.joblib")

url = "https://cryptopunks.app/"
st.write("The CryptoPunks, created by [LarvaLabs](%s), are some of the most famous NFTs out there. They are all very simple and similar in style, \
         but each is unique. There are 10,000 original CryptoPunks and taking a look at them, they look perfect for Kernel Density Estimators. \
         \n\nKDEs are used to estimate the joint distributions of various data, and then can produce random samples from the estimated distribution. To study applications of KDEs more, \
         I used the **sklearn.neighbors.KernelDensity** class to fit a KDE to .png files of the original 10,000 CryptoPunks to see if I could create new CryptoPunk-inspired \
         images by drawing random samples from the resulting estimated distribution of the original images' pixels.\
         \n\nClick below to reveal the rest of this post and generate some original CryptoPunk-inspired images with my KDE embedded in the background :point_down:" % url)

if __name__ == "__main__": 
    if st.button("generate original images"): 
        generate(kde) 

        st.write("**What are Kernel Density Estimators?** \
                \n\nKernel Density Estimation (KDE) is a non-parametric statistical tool that helps us understand the underlying distribution of a dataset. \
                Instead of just looking at individual points or bars in a histogram, KDE gives us a smoother, continuous line that shows where the data \
                is most concentrated. \n\n") 
        
        st.write("**Understanding KDEs** \
                \n\nTo understand KDE, imagine you have a set of data points—like the scores on a test. A histogram might show you how many scores \
                fall into different ranges, but it can be a bit choppy and depends a lot on how you choose the ranges. KDE takes a different approach.\
                It places a smooth curve, often shaped like a bell, on top of each data point. Then, it adds all these curves together to make one \
                smooth, continuous line. This line shows you not just where the data points are, but how they spread out and where the \'hot spots\' of data \
                concentration are.\n\n")
        
        st.write("**How KDE Works**\n \
                \n\nKDE works by applying a \'kernel function\' to each data point. This function is a bit like a weighting function—it gives a weight to the \
                points around it, with the highest weight at the data point itself and lower weights as you move away. By adding up all these weighted functions, \
                KDE produces a smooth curve that reflects the density of data points across the dataset. The shape and width of the kernel function are important. \
                They determine how smooth or wavy the final density estimate will be. If the kernel is too wide, the estimate will be very smooth, and you might miss \
                some interesting details in the data. If it's too narrow, the estimate might be too bumpy, capturing random noise in the data as if it were important patterns.\n\n")
            
        st.write("**Estimating Joint Distributions**\n \
                \n\nKDE isn't just for looking at one variable at a time. It can also estimate the joint distribution of two or more variables. This is like looking at how \
                two factors, such as age and income, interact across your dataset. By applying KDE to two-dimensional data, you can see not just the individual distributions \
                of age and income, but also how they relate to each other—are higher incomes more common at certain ages, for example?\n\n \
                ")
        
        st.write("**Using KDE**\n \
                \n\nKDE is widely used in data science for exploratory data analysis. It helps identify where the data is concentrated and can reveal clusters or \
                patterns that might not be obvious from just looking at the raw data or histograms. KDE is also useful in machine learning for tasks like anomaly detection, where understanding \
                the distribution of \'normal\' data helps identify outliers")
