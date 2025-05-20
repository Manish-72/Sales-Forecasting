import requests

url = 'http://127.0.0.1:5000/predict'  # Local Flask server endpoint

# Features in the exact order expected by your model (as per your list)
data = {
    "features": [
        0.15,     # Copiers_Share
        0.25,     # Machines_Share
        1200.50,  # Sales_Lag_1
        1150.75,  # Sales_Lag_2
        1100.30,  # Sales_Lag_3
        1050.20,  # Sales_Lag_4
        1000.10,  # Sales_Lag_5
        950.45,   # Sales_Lag_6
        900.60,   # Sales_Lag_7
        850.25,   # Sales_Lag_8
        800.40,   # Sales_Lag_9
        750.55,   # Sales_Lag_10
        700.70,   # Sales_Lag_11
        650.85,   # Sales_Lag_12
        600.90,   # Sales_Lag_13
        550.95,   # Sales_Lag_14
        980.35,   # Sales_Rolling_Mean_7
        850.50    # Sales_Rolling_Mean_14
    ]
}

response = requests.post(url, json=data)
print(response.json())