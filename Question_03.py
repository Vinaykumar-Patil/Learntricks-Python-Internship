'''Weather App: Develop a program that fetches weather data from an online API and 
displays it to the user based on their location or a user-provided location.'''

import requests

# Defining function for fetching the weather data
def fetch_weather_data(location):
    # Construct URL for fetching weather data from wttr.in
    url = f"https://wttr.in/{location}?format=%t+%C+%h"
    # Sending a GET request to fetch weather data
    response = requests.get(url)
    
    # Checking if the request was successful or not
    if response.status_code == 200:
        # Displaying weather information for the specified location
        print("Weather in", location + ":")
        print(response.text)
    else:
        # Displaying error message if weather data retrieval fails
        print("Error fetching weather data.")

if __name__ == "__main__":
    # Welcome message for the user
    print("Welcome to the Weather App!")
    print("Please enter the name of an Indian city to get its weather information.")
    
    # Creating Main loop for user interaction
    while True:
        # Prompt user to enter a city name or exit
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            # Exit the program if the user chooses to quit
            print("Thank you for using the Weather App. Goodbye!")
            break
        # Fetching weather data for the specified city
        fetch_weather_data(city)
