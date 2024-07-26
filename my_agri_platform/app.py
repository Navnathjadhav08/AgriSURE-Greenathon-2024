from flask import Flask, render_template, request
import os
from utils.data_fetch import get_market_price
from utils.plotting import plot_income, plot_impact
from utils.predictions import calculate_income, predict_impact

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        data = {
            'crop_name': request.form['crop_name'],
            'crop_variety': request.form['crop_variety'],
            'plantation_date': request.form['plantation_date'],
            'soil_type': request.form['soil_type'],
            'water_resources': request.form['water_resources'],
            'irrigation_system': request.form['irrigation_system'],
            'land_area': float(request.form['land_area']),
            'location': request.form['location'],
            'avg_yield': float(request.form['avg_yield'])  # New field for average yield
        }
        
        # Fetch market price and weather forecast
        market_price = get_market_price(data['crop_name'], data['crop_variety'])
        
        # Calculate income and impact predictions
        min_price = market_price['min_price']
        max_price = market_price['max_price']
        avg_price = market_price['avg_price']
        
        # Dummy impact predictions data for demonstration
        impact_predictions = predict_impact(data, None)  # Replace None with actual weather forecast
        
        # Generate plots
        income_plot_url = plot_income(
            min_price, max_price, avg_price,
            data['avg_yield'], data['land_area']
        )
        
        impact_plot_url = plot_impact(
            impact_predictions['dates'], impact_predictions['values']
        )

        return render_template('result.html', data=data, market_price=market_price, income=calculate_income(data, market_price), income_plot_url=income_plot_url, impact_plot_url=impact_plot_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
