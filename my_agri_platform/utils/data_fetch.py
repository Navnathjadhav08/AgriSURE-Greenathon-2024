import pandas as pd

df = pd.read_csv('marketprice.csv')

def get_market_price(crop_name, crop_variety=None):
    # Filter data for the given crop name and optionally crop variety
    if crop_variety:
        crop_data = df[(df['Commodity'].str.contains(crop_name, case=False, na=False)) & 
                       (df['Variety'].str.contains(crop_variety, case=False, na=False))]
    else:
        crop_data = df[df['Commodity'].str.contains(crop_name, case=False, na=False)]
    
    if crop_data.empty:
        return {'min_price': 0, 'max_price': 0, 'avg_price': 0}

    min_price = crop_data['Min_Price'].mean()
    max_price = crop_data['Max_Price'].mean()
    avg_price = crop_data['Avg_Price'].mean()

    return {'min_price': min_price/100, 'max_price': max_price/100, 'avg_price': avg_price/100}
