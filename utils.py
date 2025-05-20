import pandas as pd
import numpy as np
from datetime import datetime

def prepare_input(json_input, previous_predictions=None):
    """Prepare input features for model prediction"""
    # Parse input
    order_date = pd.to_datetime(json_input["Order Date"])
    hist_sales = json_input["historical_data"]["Total_Sales"]
    hist_copiers = json_input["historical_data"]["Copiers_Sales"]
    hist_machines = json_input["historical_data"]["Machines_Sales"]
    
    # Calculate shares
    hist_copiers_share = [c/t if t > 0 else 0 for c,t in zip(hist_copiers, hist_sales)]
    hist_machines_share = [m/t if t > 0 else 0 for m,t in zip(hist_machines, hist_sales)]
    
    # Create features dictionary
    features = {
        'Day_of_Week': order_date.dayofweek,
        'Week_of_Year': order_date.isocalendar().week,
        'Month': order_date.month
    }
    
    # Add lag features for shares (using last 14 days), interleaved as in training
    for lag in range(1, 15):
        features[f'Copiers_Share_Lag_{lag}'] = (
            hist_copiers_share[-lag] 
            if lag <= len(hist_copiers_share) 
            else 0
        )
        features[f'Machines_Share_Lag_{lag}'] = (
            hist_machines_share[-lag] 
            if lag <= len(hist_machines_share) 
            else 0
        )
    
    # Add sales log features
    sales_log = np.log1p(hist_sales)
    for lag in range(1, 15):
        features[f'Sales_Lag_{lag}'] = (
            sales_log[-lag] 
            if lag <= len(sales_log) 
            else 0
        )
    
    # Add rolling means
    window_7 = sales_log[-7:] if len(sales_log) >= 7 else sales_log
    window_14 = sales_log[-14:] if len(sales_log) >= 14 else sales_log
    
    features['Sales_Rolling_Mean_7'] = np.mean(window_7) if len(window_7) > 0 else 0
    features['Sales_Rolling_Mean_14'] = np.mean(window_14) if len(window_14) > 0 else 0
    
    # If we have previous predictions, update the first lag with them
    if previous_predictions:
        features['Sales_Lag_1'] = np.log1p(previous_predictions['total_sales'])
        features['Copiers_Share_Lag_1'] = previous_predictions['copiers_share']
        features['Machines_Share_Lag_1'] = previous_predictions['machines_share']
    
    # Correct column order matching the trained model feature order (interleaving copiers and machines lags)
    columns = [
        'Day_of_Week', 'Week_of_Year', 'Month',
    ]
    # Interleave Copiers_Share_Lag_X and Machines_Share_Lag_X
    for lag in range(1, 15):
        columns.append(f'Copiers_Share_Lag_{lag}')
        columns.append(f'Machines_Share_Lag_{lag}')
    # Then all Sales_Lag features
    for lag in range(1, 15):
        columns.append(f'Sales_Lag_{lag}')
    # Then rolling means
    columns += ['Sales_Rolling_Mean_7', 'Sales_Rolling_Mean_14']
    
    return pd.DataFrame([features])[columns]
