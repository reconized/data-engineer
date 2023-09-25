url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=***Your Free API Key***"  #Make sure to change ******* to your API key.
import requests

# Replace 'YOUR_API_KEY' with your actual API key from ExchangeRate-API.
api_key = 'YOUR_API_KEY'

# Define the base currency and target currency for conversion.
base_currency = 'USD'
target_currency = 'EUR'

# Define the API endpoint URL with your API key and currency pair.
url = f'https://v6.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&apikey={api_key}'

try:
    # Send an HTTP GET request to the ExchangeRate-API.
    response = requests.get(url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the JSON response to extract exchange rate data.
        exchange_rate_data = response.json()

        # Extract the exchange rate.
        exchange_rate = exchange_rate_data['rates'][target_currency]

        # Print the exchange rate.
        print(f"Exchange rate from {base_currency} to {target_currency}: {exchange_rate}")

    else:
        # Print an error message if the request was not successful.
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle any exceptions that may occur during the request.
    print(f"An error occurred: {e}")
import pandas as pd
import json

def extract_data_from_json(json_file_path):
    # Initialize an empty list to store the extracted data
    data = []
    
    try:
        # Open and load the JSON file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
            
        # Assuming the JSON structure contains a list of objects with 'Name' and 'Market Cap' keys
        for entry in json_data:
            name = entry.get('Name', None)
            market_cap = entry.get('Market Cap', None)
            
            if name is not None and market_cap is not None:
                data.append([name, market_cap])
    
    except Exception as e:
        print(f"Error loading data from JSON file: {str(e)}")
    
    return data

# Define the JSON file path
json_file_path = 'bank_market_cap_1.json'

# Call the extract_data_from_json function to extract the data
extracted_data = extract_data_from_json(json_file_path)

# Create a Pandas DataFrame using the extracted data and specified columns
columns = ['Name', 'Market Cap (US$ Billion)']
df = pd.DataFrame(extracted_data, columns=columns)

# Display the DataFrame
print(df)

    
    
    # Write your code here
import pandas as pd

# Load the CSV file as a DataFrame with index_col set to 0
df = pd.read_csv('exchange_rates.csv', index_col=0)

# Find the exchange rate for British pounds with the symbol GBP
exchange_rate = df.loc['GBP', 'Exchange Rate']

# Print the exchange rate
print("Exchange Rate for GBP:", exchange_rate)
