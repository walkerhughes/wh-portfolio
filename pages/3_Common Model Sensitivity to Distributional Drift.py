import streamlit as st 

st.set_page_config(
    page_title = "Model Sensitivity", 
    page_icon = ":scales:",
)

st.write("#### :scales: Let's Compare Common ML Models' Sensitivities to Shifts in Feature Distributions")

st.write("""
    Distributional shift refers to when the distribution of data that a model is trained on differs significantly from the data it encounters in the 
    real world or during the testing phase. This can lead to poor model performance, unexpected results, or even business decisions made on bad information.

    The impact of distributional shift is not uniform across all types of models though. Some models may be more robust to certain shifts, while others 
    might be highly sensitive to minor distribution changes. Understanding these dynamics can help in selecting the right model for a specific 
    problem and in designing systems that remain reliable under changing conditions.
         
    To explore this concept, I train several models, including OLS (Ordinary Least Squares), Lasso, and Ridge regressions, on a dataset with 
    well-understood characteristics. **After training, I intentionally introduce a shift in the distribution of one of the test dataset's columns.** 
    This manipulation simulates a scenario where the model might encounter data that differs from its training set. We'll then look at the test RMSE for each 
    of these models before and after the distribution shift.
         
    **Objective**:\n
    Our primary goal is to measure the test RMSE (Root Mean Square Error) of each model after the distributional shift. RMSE provides a clear metric for comparing model performance, where a lower RMSE indicates a model that predicts more accurately.

    **Procedure**:\n
    ***Train Models***: Initially, we train our selected models on the dataset without any manipulation, establishing a baseline performance metric for each.\n
    ***Introduce Shift***: We then modify the distribution of a specific column, simulating a real-world scenario where the data's underlying distribution changes after the model has been deployed.\n
    ***Re-evaluate Performance***: After introducing the shift, we measure each model's test RMSE to assess how the distributional shift affects their performance.
""")



def main(): 

    column = st.selectbox(
        'Pick a column to test :point_down:', 
        ("col 1", "col 2", "col 3")
    )
    
if __name__ == "__main__": 
    main() 