import streamlit as st 

st.set_page_config(
    page_title = "Model Sensitivity", 
    page_icon = ":scales:",
)

st.write("#### :scales: Let's Compare Different Models' Sensitivity to Shifts in Feature Distributions")

def main(): 

    column = st.selectbox(
        'Pick a column to test :point_down:', 
        ("col 1", "col 2", "col 3")
    )
    
if __name__ == "__main__": 
    main() 