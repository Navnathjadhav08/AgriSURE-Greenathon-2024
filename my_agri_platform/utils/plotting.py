import matplotlib.pyplot as plt
import io
import base64

def calculate_total_income(price, yield_per_acre, land_area):
    return price * yield_per_acre * land_area

def plot_income(min_price, max_price, avg_price, yield_per_acre, land_area):
    min_income = calculate_total_income(min_price, yield_per_acre, land_area)
    max_income = calculate_total_income(max_price, yield_per_acre, land_area)
    avg_income = calculate_total_income(avg_price, yield_per_acre, land_area)
    
    price_types = ['Min Price', 'Max Price', 'Avg Price']
    total_incomes = [min_income, max_income, avg_income]

    fig, ax = plt.subplots()
    ax.bar(price_types, total_incomes, color=['red', 'green', 'blue'])
    ax.set_xlabel('Price Type')
    ax.set_ylabel('Total Income (in currency units)')
    ax.set_title('Total Income Based on Price Types')
    ax.grid(True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('ascii')
    
    return plot_url

def plot_impact(dates, values):
    fig, ax = plt.subplots()
    ax.plot(dates, values, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Date')
    ax.set_ylabel('Impact Value')
    ax.set_title('Predicted Impact on Crop')
    ax.grid(True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('ascii')
    
    return plot_url
