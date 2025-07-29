# Hello World - Streamlit App

A simple interactive Streamlit application that demonstrates various features including data visualization, interactive elements, and integration with existing Python modules.

## Features

- **Multi-page Navigation**: Home, Circle Calculator, Data Visualization, and About pages
- **Interactive Elements**: Text inputs, sliders, buttons, and form controls
- **Data Visualization**: Charts and graphs using sample data
- **Module Integration**: Uses the existing `area_of_circle` function from `demo.py`
- **Responsive Design**: Wide layout with sidebar navigation

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Pages

### Home
- Interactive greeting with name input
- Age slider and color selection
- Fun button with balloons animation

### Circle Calculator
- Uses the existing `area_of_circle` function from `demo.py`
- Interactive radius input with validation
- Visual representation of the circle using matplotlib
- Real-time area calculation

### Data Visualization
- Sample data generation using NumPy
- Multiple chart types: Scatter Plot, Histogram, Bar Chart
- Interactive chart selection

### About
- Information about the app features
- Technologies used
- Project description

## Project Structure

```
hello-world/
├── app.py              # Main Streamlit application
├── demo.py             # Circle area calculation module
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Streamlit**: Web app framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization

## Development

To modify the app:
1. Edit `app.py` to add new features
2. Update `requirements.txt` if adding new dependencies
3. Run `streamlit run app.py` to see changes

Enjoy exploring the app! 🚀