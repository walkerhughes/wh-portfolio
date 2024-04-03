import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Walker Hughes Portfolio",
        page_icon="👋",
    )

    st.write("# Welcome!")

    # st.sidebar.success("Select a demo above.")

    st.markdown("""
        I'm Walker :wave: I'm a machine learning engineer, mathematician, and Brazilian Jiu-Jitsu enthusiast. \
        I'm currently a Master's Student in Data Science at the University of San Francisco, graduating in July 2025.
  
        **:point_left: Check out some recent projects of mine in the sidebar or scroll down for a full list :point_down:**
    """
    )

    st.code("""
        class about_me: 
            def __init__(self,):
                self.name = "walker hughes"
                self.education = {
                    "graduate": "ms in data science", 
                    "undergrad": ["bs in computational math", 
                                  "bs in economics"]
                }
                self.skills = {
                    "python",
                    "machine learning", 
                    "statistics and causality",
                    "brazilian portuguese"
                }
                self.hobbies = {
                    "brazilian jiu-jitsu", 
                    "recreational probability"
                }
                self.experience = {
                    "data solutions consultant": "addepar, mountain view", 
                    "data analyst": "cornerstone research, san francisco"
                }
        """,
    language="python")


if __name__ == "__main__":
    run()
