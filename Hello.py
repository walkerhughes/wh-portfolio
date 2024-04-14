import streamlit as st

def run():
    st.set_page_config(
        page_title="Walker Hughes Portfolio",
        page_icon="👋",
    )

    st.write("# Welcome!")

    st.markdown("""
        I'm Walker :wave: I'm a machine learning engineer, mathematician, and Brazilian Jiu-Jitsu enthusiast. \
        I'm currently a Master's Student in Data Science at the University of San Francisco, graduating in July 2025.
  
        **:point_left: Check out some interactive projects in the sidebar or scroll down for a full list :point_down:**
    """
    )

    st.code("""
        class about_me: 
            def __init__(self,):
                self.name = "walker hughes"
                self.education = {
                    "graduate": "ms in data science", 
                    "undergrad": [
                        "bs in computational math", 
                        "bs in economics", 
                        "minor in portuguese"
                    ]
                }
                self.skills = {
                    "python", 
                    "machine learning",
                    "statistics and econometrics",
                    "data structures & algorithms"
                }
                self.experience = {
                    "data solutions consultant": "addepar, mountain view", 
                    "data analyst": "cornerstone research, san francisco"
                }
                self.hobbies = {
                    "brazilian jiu-jitsu", 
                    "recreational probability"
                }
        """,
    language="python")

    st.write("#### Generative AI")
    st.write(":arrow_right: [Idiom.ai: Chatbot game to learn foreign language expressions and figures of speech](%s)" % "https://walkerhughes.streamlit.app/Idiom.ai:_Learn_Portuguese_Idioms_with_GPT_3.5")
    st.write(":arrow_right: [LangChain RAG App for YouTube video Q&A](%s)" % "https://github.com/walkerhughes/rag_langchain/blob/main/RAG_langchain_model.ipynb")
    st.write(":arrow_right: [Generating Original CryptoPunk-style NFTs with Kernel Density Estimators](%s)" % "https://walkerhughes.streamlit.app/Generating_New_CryptoPunks_with_Kernel_Density_Estimation")

    st.write("#### Machine Learning")
    st.write(":arrow_right: [Comparing different regression models' sensitivities to distributional drift post-training](%s)" % "https://walkerhughes.streamlit.app/Common_Model_Sensitivity_to_Distributional_Drift")
    st.write(":arrow_right: [A case for residualizing your regression data more often](%s)" % "https://walkerhughes.streamlit.app/")
    st.write(":arrow_right: [Hidden Markov Models: How to Perform Classification on Latent Variables](%s)" % "https://walkerhughes.streamlit.app/")

    st.write("#### Topics in Math")
    st.write(":arrow_right: [Explore chaotic behavior in initial value problems with the Lorenz Equations](%s)" % "https://walkerhughes.streamlit.app/Chaos_Theory_and_Lorenz_Equations")


if __name__ == "__main__":
    run()
