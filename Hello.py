import streamlit as st

def run():
    st.set_page_config(
        page_title="Walker Hughes Portfolio",
        page_icon="👋",
        layout="wide"
    )

    st.write("# Welcome!")

    st.markdown("""
        I'm Walker :wave: I'm a machine learning engineer, mathematician, and Brazilian Jiu-Jitsu enthusiast. \
        I'm currently a Master's Student in Data Science at the University of San Francisco graduating in July 2025.
  
        **:point_left: Check out some interactive projects in the sidebar or scroll down for a full list :point_down:**
    """
    ) 

    st.code("""
        class about_me: 
            def __init__(self):
                self.name = "walker hughes"
                self.skills = {
                    "python", 
                    "machine learning",
                    "statistical modeling",
                    "data structures & algorithms"
                }
                self.experience = {
                    "machine learning engineer": "we consulting llc, sf",
                    "data solutions consultant": "addepar, mountain view", 
                    "data analyst": "cornerstone research, san francisco",
                    "machine learning researcher": "byu department of mathematics"
                }
                self.education = {
                    "university of san francisco, 2025": [
                        "ms in data science"
                    ], 
                    "brigham young university, 2021": [
                        "bs in computational mathematics", 
                        "bs in economics", 
                        "minor in portuguese studies"
                    ]
                }
        """,
    language="python")

    st.write("#### Machine Learning & Generative AI")
    st.write(":arrow_right: [[GitHub] LangChain RAG App for YouTube video Q&A](%s)" % "https://github.com/walkerhughes/rag_langchain/blob/main/RAG_langchain_model.ipynb")
    st.write(":arrow_right: [[Streamlit App] Generating Original CryptoPunk-style NFTs with Kernel Density Estimators](%s)" % "https://walkerhughes.streamlit.app/Generating_New_CryptoPunks_with_Kernel_Density_Estimation")
    st.write(":arrow_right: [[In the works] Idiom.ai: Chatbot game to learn foreign language expressions and figures of speech](%s)" % "https://walkerhughes.streamlit.app/Idiom.ai:_Learn_Portuguese_Idioms_with_GPT_3.5")
    st.write(":arrow_right: [[In the works] Comparing different regression models' sensitivities to distributional drift post-training](%s)" % "https://walkerhughes.streamlit.app/Common_Model_Sensitivity_to_Distributional_Drift")

    st.write("#### Topics in Applied Math")
    st.write(":arrow_right: [[Streamlit App] Explore chaotic behavior in initial value problems with the Lorenz Equations](%s)" % "https://walkerhughes.streamlit.app/Chaos_Theory_and_Lorenz_Equations")
    st.write(":arrow_right: [[GitHub] Estimating the Probability that Random Binary Matrices are Invertible with Monte Carlo Methods](%s)" % "https://github.com/walkerhughes/monte_carlo_matrix_invertability")
    st.write(":arrow_right: [[GitHub] Interior Point optimization methods and KKT conditions](%s)" % "https://github.com/walkerhughes/")

    st.write("#### Implementing Research Papers")
    st.write(":arrow_right: [[GitHub] U-Net Convolutional Neural Network for Biomedical Image Segmentation (Olaf Ronneberger, Philipp Fischer, and Thomas Brox, 2015)](%s)" % "https://github.com/walkerhughes/deep_learning/blob/main/cancer_detection.ipynb")


if __name__ == "__main__":
    run()
