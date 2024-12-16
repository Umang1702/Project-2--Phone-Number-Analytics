import requests

def lookup_phone_number(phone_number, api_key, country_code='IN'):
    # Format phone number with country code if not already included
    if not phone_number.startswith('+'):
        phone_number = f'+{country_code}{phone_number}'
    
    # URL for the NumVerify API with the API key
    url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code={country_code}&format=1'

    # Send request to NumVerify API
    response = requests.get(url)

    # Parse the response
    data = response.json()

    # Debugging: print the entire API response to inspect it
    print("API Response:", data)

    # Check if the response contains the 'valid' key
    if 'valid' in data:
        if data['valid']:
            print(f"Phone Number: {phone_number}")
            print(f"Country: {data['country_name']}")
            print(f"Location: {data['location']}")
            print(f"Carrier: {data['carrier']}")
            print(f"Line Type: {data['line_type']}")
        else:
            print(f"Invalid phone number: {phone_number}")
    else:
        print("Error in API response. Check if the API key is correct or the response format.")
        # You can also print the error message if it's available
        if 'error' in data:
            print("Error Message:", data['error']['info'])

# Example Usage:
# Replace 'YOUR_API_KEY' with the actual API key you got after signing up
api_key = 'Your_Api_Key'
phone_number = input("Enter your number:")  # Replace with the phone number you want to lookup
country_code = 'IN'  # Country code for India

# Call the function to lookup phone number
lookup_phone_number(phone_number, api_key, country_code)
