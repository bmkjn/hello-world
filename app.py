import streamlit as st
import pandas as pd
import numpy as np
from demo import area_of_circle

# Set page config
st.set_page_config(
    page_title="Hello World - Streamlit App",
    page_icon="🌍",
    layout="wide"
)

# Main title
st.title("🌍 Hello World - Interactive Streamlit App")
st.markdown("---")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Home", "Circle Calculator", "Data Visualization", "About"]
)

if page == "Home":
    st.header("Welcome to our Streamlit App!")
    
    # Interactive greeting
    user_name = st.text_input("Enter your name:", "World")
    st.write(f"Hello, {user_name}! 👋")
    
    # Some interactive elements
    st.subheader("Interactive Elements")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider("How old are you?", 0, 100, 25)
        st.write(f"You are {age} years old!")
    
    with col2:
        favorite_color = st.selectbox(
            "What's your favorite color?",
            ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
        )
        st.write(f"Your favorite color is {favorite_color}!")
    
    with col3:
        if st.button("Click me!"):
            st.balloons()
            st.success("🎉 You clicked the button!")

elif page == "Circle Calculator":
    st.header("🔵 Circle Area Calculator")
    st.write("This uses the existing `area_of_circle` function from `demo.py`")
    
    # Input for radius
    radius = st.number_input(
        "Enter the radius of the circle:",
        min_value=0.0,
        max_value=1000.0,
        value=10.0,
        step=0.1
    )
    
    if st.button("Calculate Area"):
        area = area_of_circle(radius)
        st.success(f"Area of circle with radius {radius} is: {area:.2f} square units")
        
        # Create a simple visualization
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots(figsize=(6, 6))
        circle = plt.Circle((0, 0), radius, fill=False, color='blue', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-radius-1, radius+1)
        ax.set_ylim(-radius-1, radius+1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Circle with radius {radius}')
        
        st.pyplot(fig)

elif page == "Data Visualization":
    st.header("📊 Data Visualization")
    
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    st.subheader("Sample Data")
    st.dataframe(data.head())
    
    # Chart options
    chart_type = st.selectbox(
        "Choose chart type:",
        ["Scatter Plot", "Histogram", "Bar Chart"]
    )
    
    if chart_type == "Scatter Plot":
        st.scatter_chart(data, x='x', y='y', color='category')
    elif chart_type == "Histogram":
        st.bar_chart(data['x'].value_counts().head(10))
    elif chart_type == "Bar Chart":
        category_counts = data['category'].value_counts()
        st.bar_chart(category_counts)

elif page == "About":
    st.header("ℹ️ About This App")
    
    st.markdown("""
    This is a simple Streamlit application that demonstrates various features:
    
    - **Interactive Elements**: Text inputs, sliders, buttons
    - **Data Visualization**: Charts and graphs
    - **Integration**: Uses existing Python modules
    - **Navigation**: Multi-page layout with sidebar
    
    ### Features:
    - Home page with interactive greetings
    - Circle calculator using existing `demo.py` module
    - Data visualization with sample data
    - About page with information
    
    ### Technologies Used:
    - Streamlit
    - Pandas
    - NumPy
    - Matplotlib
    """)
    
    st.info("This app was built as a simple demonstration of Streamlit capabilities!")

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")
