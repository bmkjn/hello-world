# Hello World - Streamlit App

A simple interactive Streamlit application that demonstrates various features including data visualization, interactive elements, and integration with existing Python modules.

## Features

- **Multi-page Navigation**: Home, Circle Calculator, Data Visualization, and About pages
- **Interactive Elements**: Text inputs, sliders, buttons, and form controls
- **Data Visualization**: Charts and graphs using sample data
- **Module Integration**: Uses the existing `area_of_circle` function from `demo.py`
- **Responsive Design**: Wide layout with sidebar navigation

## Installation

### Option 1: Local Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Option 2: Docker Installation

1. Build the Docker image:
```bash
docker build -t demo-app .
```

2. Run the container:
```bash
docker run -p 8501:8501 demo-app
```

## Running the App

### Local Development
To run the Streamlit app locally, use the following command:

```bash
streamlit run app.py
```

### Docker
To run the app using Docker:

```bash
docker run -p 8501:8501 demo-app
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