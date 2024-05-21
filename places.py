from flask import Flask, jsonify, request
import requests
# from bs4 import BeautifulSoup
app = Flask(__name__)

# Your Geoapify API key
API_KEY = '34583d847bb34e128d658a90b0119a7d'

"""
GET API

req param:: place: str

response:: objects of near by toorist attraction in place
"""
@app.route('/location', methods=['GET'])
def get_location():

    place = request.args.get('text')
    print(place)
    country_code_filter = request.args.get('filter')
    country_code_filter=country_code_filter.split(':')[1]
    print(country_code_filter)
    # Construct the URL for the Geoapify API request
    url = f'https://api.geoapify.com/v1/geocode/search?text={place}&filter=countrycode:{country_code_filter}&apiKey={API_KEY}'

    # Make the request to the Geoapify API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response from the API
        response1=response.json()
        # print(response1)
        coordinates = response1['features'][0]['geometry']['coordinates']
        lon,lat=coordinates
        print(lon)
        categories = 'tourism.attraction'
        # lat = request.args.get('lat')
        # lon = request.args.get('lon')
        radius = 5000
        limit = 20

    # Construct the URL for the Geoapify API request
        url = f'https://api.geoapify.com/v2/places?categories={categories}&filter=circle:{lon},{lat},{radius}&bias=proximity:{lon},{lat}&limit={limit}&apiKey={API_KEY}'

    # Make the request to the Geoapify API
        response = requests.get(url)

    # Check if the request was successful
        if response.status_code == 200:
        # Return the JSON response from the API
            return jsonify(response.json())
        else:
        # Return an error message if the request failed
            return jsonify({'error': 'Failed to fetch places'}), response.status_code

    else:
        # Return an error message if the request failed
        return jsonify({'error': 'Failed to fetch places'}), response.status_code
    

'''
GET API

request param:: lat,lon : str

response param:: objects of near by toorist attraction in place

'''
@app.route('/places', methods=['GET'])
def get_places():
    # Define the parameters for the API request
    categories = 'tourism.attraction'
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = 5000
    limit = 20

    # Construct the URL for the Geoapify API request
    url = f'https://api.geoapify.com/v2/places?categories={categories}&filter=circle:{lon},{lat},{radius}&bias=proximity:{lon},{lat}&limit={limit}&apiKey={API_KEY}'

    # Make the request to the Geoapify API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response from the API
        return jsonify(response.json())
    else:
        # Return an error message if the request failed
        return jsonify({'error': 'Failed to fetch places'}), response.status_code
    
'''

GET API

request params:: lat,lon: str

response :: objects of weather condition in a place
'''
@app.route('/weather', methods=['GET'])
def get_weather():
    WEATHER_API_KEY="9c3aac1db2cb34834f49d6eece299f6f"
    # Get latitude and longitude from query parameters
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({'error': 'Please provide latitude and longitude'}), 400

    # Construct the URL for the OpenWeatherMap API request
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}'

    try:
        # Make the request to the OpenWeatherMap API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response from the API
            return jsonify(response.json())
        else:
            # Log the error response from the API
            app.logger.error('Failed to fetch weather data: %s', response.text)
            # Return an error message if the request failed
            return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

    except Exception as e:
        # Log the exception
        app.logger.exception('An error occurred while fetching weather data')
        # Return an internal server error message
        return jsonify({'error': 'Internal Server Error'}), 500
    
@app.route('/location1', methods=['GET'])
def get_locations():

    place = request.args.get('text')
    print(place)
    country_code_filter = request.args.get('filter')
    country_code_filter="in"
    print(country_code_filter)
    # Construct the URL for the Geoapify API request
    url = f'https://api.geoapify.com/v1/geocode/search?text={place}&filter=countrycode:{country_code_filter}&apiKey={API_KEY}'

    # Make the request to the Geoapify API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response from the API
        return jsonify(response.json())
    else:
        # Return an error message if the request failed
        return jsonify({'error': 'Failed to fetch places'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True,port=5090)




