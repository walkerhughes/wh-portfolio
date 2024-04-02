# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import pandas as pd
import pydeck as pdk

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Lorenz Equations", page_icon=":collision:")
st.markdown("#### Chaos Theory & Lorenz Equations")
st.sidebar.header("Chaos Theory & Lorenz Equations") 

"""
in the side bar I want to be able to toggle rho, beta and sigma 
"""

st.code("""
        def lorenz(t, x):
            \"""
            Implements Lorenz equations:
            
            dx/dt = σ(y − x)
            dy/dt = ρx − y − xz
            dz/dt = xy − βz
                
            Parameters:
                x ((3,) ndarray): The state values (x,y,z)
                t (float): The time value t
            Returns:
                ((3,) ndarray): The derivative values
            x, y, z = x[0], x[1], x[2]  
            \"""
            sigma, rho, beta = 10, 28, 8/3 
            return np.array([sigma * (y - x), (rho * x) - y - (x * z), (x * y) - (beta * z)]))
        """, language="python") 
