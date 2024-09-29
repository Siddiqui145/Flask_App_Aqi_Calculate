from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_aqi(concentration, pollutant):
    if pollutant == 'PM2.5':
        c_low = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
        c_high = [12, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4, 999.9]
        aqi_low = [0, 51, 101, 151, 201, 301, 401, 501]
        aqi_high = [50, 100, 150, 200, 300, 400, 500, 999]
    elif pollutant == 'PM10':
        c_low = [0, 55, 155, 255, 355, 425, 505, 605]
        c_high = [54, 154, 254, 354, 424, 504, 604, 999]
        aqi_low = [0, 51, 101, 151, 201, 301, 401, 501]
        aqi_high = [50, 100, 150, 200, 300, 400, 500, 999]
    else:
        return None, None

    i_low = 0
    while concentration > c_high[i_low]:
        i_low += 1
    i_high = i_low
    aqi = round(((aqi_high[i_high] - aqi_low[i_low]) / (c_high[i_high] - c_low[i_low])) * (concentration - c_low[i_low]) + aqi_low[i_low])

    if aqi <= 50:
        category = "Good"
    elif aqi <= 100:
        category = "Satisfactory"
    elif aqi <= 200:
        category = "Moderate"
    elif aqi <= 300:
        category = "Poor"
    elif aqi <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    return aqi, category


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    pollutant = request.form['pollutant']
    concentration = float(request.form['concentration'])

    aqi, category = calculate_aqi(concentration, pollutant)

    return render_template('index.html', aqi=aqi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
