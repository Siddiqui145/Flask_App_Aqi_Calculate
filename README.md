# AQI Calculator

A simple web-based **Air Quality Index (AQI)** calculator built using **Flask**. This tool calculates AQI based on **PM2.5** or **PM10** pollutant concentrations and provides the AQI category (Good, Satisfactory, Moderate, Poor, Very Poor, Severe).

## Features

- Choose between **PM2.5** or **PM10** pollutant types.
  
- Input pollutant concentration (µg/m³) and get the AQI value.
  
- AQI categories:
  - **0-50**: Good
  - **51-100**: Satisfactory
  - **101-200**: Moderate
  - **201-300**: Poor
  - **301-400**: Very Poor
  - **401-500**: Severe

## Demo

https://github.com/user-attachments/assets/ccc86c24-4216-4203-ba9e-fd167591dd96

## Technologies

- **Python** (v3.x)
- **Flask** (v2.x)
- **HTML/CSS** for frontend
- **Bootstrap** (optional for styling)

## Installation

Follow these steps to run the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/aqi-calculator.git](https://github.com/Siddiqui145/Flask_App_Aqi_Calculate
    cd Flask_App_Aqi_Calculate)
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```

    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required dependencies**:
    ```bash
    pip install Flask
    ```

5. **Run the Flask app**:
    ```bash
    flask run
    ```

6. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

- **Select Pollutant**: Choose either PM2.5 or PM10 from the dropdown menu.
- **Input Concentration**: Enter the concentration of the pollutant (µg/m³).
- **Calculate AQI**: Click the "Calculate AQI" button, and the AQI value with the corresponding category will be displayed.

### Example

For **PM2.5** concentration of **35.0 µg/m³**:
- **AQI**: 102
- **Category**: Moderate

## File Structure

/aqi-calculator
├── app.py                   # Main Flask application
├── templates
│   └── index.html            # Frontend HTML file
├── static
│   └── style.css             # Stylesheet for the website (optional)
└── README.md                 # Project documentation



## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.



