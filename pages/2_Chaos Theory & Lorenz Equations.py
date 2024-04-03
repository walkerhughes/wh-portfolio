import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
import streamlit as st

st.set_page_config(page_title="Lorenz Equations", page_icon=":collision:")
st.markdown("#### Chaos Theory & Lorenz Equations")
st.sidebar.header("Chaos Theory & Lorenz Equations") 

st.write("A primary characteristic of chaotic systems is that small changes to the initial conditions \
         can result in large changes in the system's solution curves. Here I implement the Lorenz Equations \
         to look at this behavior, using **scipy.integrate.solve_ivp** to do so The Lorenz Equations are") 

st.latex("x_{t} = {\\sigma} (y - x)")
st.latex("y_{t} = {\\rho} x - y - xz_{t}")
st.latex("z_{t} = xy - {\\beta} z")

st.write("where where $x_t$ indicates the derivative of $x$ with respect to $t$, and $\\sigma$, ${\\rho}$, and $\\beta$ are constants. \
         For different values of $\\sigma$, $\\rho$, and $\\beta$, Lorenz found that the solutions to these equations did not gravitate \
         to a fixed point, nor did the system diverge to infinity either. He refered to this phenomena as \'chaotic behavior\', and \
         described how the system exhibited a \'strange attractor\' that the solutions converged to.")

st.write("I try two approaches to investigate the chaotic behavior Lorenz observed:") 
st.write("\t\t 1. Solve the system for different parameter values $\\sigma$, $\\rho$, and $\\beta$\n") 
st.write("\t\t 2. For the $\\sigma$, $\\rho$, and $\\beta$ values, solve the system for two additional initial conditions.")

st.write("**👈 Try some different $\\sigma$, $\\rho$, and $\\beta$ values to get started!**") 

st.code("""
            def lorenz(t, x, params):
                \"""
                Implements Lorenz equations:
                
                dx/dt = σ(y − x)
                dy/dt = ρx − y − xz
                dz/dt = xy − βz
                    
                Parameters:
                    x ((3,) ndarray): The state values (x,y,z)
                    params ((3,) tuple): The values (sigma, rho, beta)
                    t (float): The time value t
                Returns:
                    ((3,) ndarray): The derivative values
                x, y, z = x[0], x[1], x[2]  
                \"""
                sigma, rho, beta = params
                return np.array([sigma*(y-x), (rho*x)-y-(x*z), (x*y)-(beta*z)]))
            """, language="python") 
    
st.code("""
            # initial values 
            initial_vals = np.random.uniform(-15, 15, (3, ))  

            # solve the ivp 
            sol = solve_ivp(lorenz, (0, 40), y0 = initial_vals, t_eval = np.linspace(0, 40, 5000))     
            x, y, z = sol.y[0], sol.y[1], sol.y[2] 
    """, language="python")

def lorenz() -> None: 

    sigma = st.sidebar.slider("Sigma", 7, 13, 10)
    rho = st.sidebar.slider("Rho", 25, 33, 28)
    beta = st.sidebar.slider("Beta", 1.5, 4.0, 2.67)

    def lorenz(t, x):
        """
        Implements Lorenz equations:
        
        dx/dt = σ(y − x)
        dy/dt = ρx − y − xz
        dz/dt = xy − βz
            
        Parameters:
            x ((3,) ndarray): The state values (x,y,z)
            t (float): The time value t
        Returns:
            ((3,) ndarray): The derivative values
        """
        x, y, z = x[0], x[1], x[2]  
        return np.array([sigma * (y - x), (rho * x) - y - (x * z), (x * y) - (beta * z)])


    ################### one initial condition ###################

    # initial values 
    initial_vals = np.random.uniform(-15, 15, (3, ))  

    # solve the ODE 
    sol = solve_ivp(lorenz, (0, 40), y0 = initial_vals, t_eval = np.linspace(0, 40, 5000))     
    x, y, z = sol.y[0], sol.y[1], sol.y[2] 

    # init plot figure 
    fig = plt.figure(figsize = (7, 7))
    ax = fig.add_subplot(111, projection = '3d')

    ax.set_title(f"Lorenz Solutions for σ={sigma}, ρ={rho}, β={beta}") 
    ax.set_xlabel("x")
    ax.set_ylabel("y") 
    ax.set_zlabel("z")

    # plot solution 
    line3d, = plt.plot(x, y, z, lw = .55) 
    st.pyplot(fig)


    ################### three initial conditions ###################

    # init plot figure 
    fig = plt.figure(figsize = (7, 7)) 
    ax = fig.add_subplot(111, projection = '3d')

    # add titles and axes 
    ax.set_title(f"Lorenz Solutions for σ={sigma}, ρ={rho}, β={beta}") 
    ax.set_xlabel("x")
    ax.set_ylabel("y") 
    ax.set_zlabel("z")

    line3d, = plt.plot(x, y, z, lw = .55, label = "Initial Condition 1") 

    for i in range(2): 

        # randomllly initial values 
        initial_vals = np.random.uniform(-15, 15, (3, ))  

        # solve the ODE 
        sol = solve_ivp(lorenz, (0, 40), y0 = initial_vals, t_eval = np.linspace(0, 40, 5000))     
        x, y, z = sol.y[0], sol.y[1], sol.y[2]     
        
        # plot solution
        line3d, = plt.plot(x, y, z, lw = .55, label = "Initial Condition {}".format(i + 2))  

    # set limits 
    plt.legend() 
    st.pyplot(fig)

st.write("It's pretty clear that the solutions we get don't converge to a single point in space, instead, they really do just swirl \
         around these \'strange attractors\' like Lorenz observed. We can also see how different initial conditions passed into the \
         IVP solver produce fairly different solutions even for the same values of $\\sigma$, $\\rho$, and $\\beta$, demonstrating \
         the Lorenz Equations' chaotic nature.") 

lorenz() 


