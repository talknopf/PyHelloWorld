import requests
import json
import os
import urllib.parse

def main(api_key,city_name='Tel Aviv'):
	# base_url variable to store url 
	base_url = "http://api.openweathermap.org/data/2.5/weather?"

	complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
	response = requests.get(complete_url) 

	x = response.json() 
	# Now x contains list of nested dictionaries 
	# Check the value of "cod" key is equal to 
	# "404", means city is found otherwise, 
	# city is not found 
	if x["cod"] != "404": 
	  
	    # store the value of "main" 
	    # key in variable y 
	    y = x["main"] 
	  
	    # store the value corresponding 
	    # to the "temp" key of y 
	    current_temperature = y["temp"] 
	  
	    # store the value corresponding 
	    # to the "pressure" key of y 
	    current_pressure = y["pressure"] 
	  
	    # store the value corresponding 
	    # to the "humidity" key of y 
	    current_humidiy = y["humidity"] 
	  
	    # store the value of "weather" 
	    # key in variable z 
	    z = x["weather"] 
	  
	    # store the value corresponding  
	    # to the "description" key at  
	    # the 0th index of z 
	    weather_description = z[0]["description"] 
	  
	    # print following values 
	    print(" Temperature: " +
	                    str(current_temperature) + " C" + 
	          "\n Atmospheric pressure (in hPa unit) = " +
	                    str(current_pressure) +
	          "\n Humidity (in percentage) = " +
	                    str(current_humidiy) +
	          "\n Description = " +
	                    str(weather_description)) 
	else: 
	    print("City Not Found")

if __name__ == "__main__":
    # execute only if run as a script
    # checking if API_KEY is in env var
    #if this module is imported no need to check and the function can be invoked with it

    api_key = os.getenv('API_KEY')
    if api_key is not None:
    	main(api_key)
    else:
    	print("Missing api key in env variables")