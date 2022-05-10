import folium
import requests
import json
import time
from datetime import datetime
pings = int(input('How many times should the API be called (every 2 seconds) : '))
api_key = '' #input your API key for Openweather here, you can find it on their website
x=[]
i=0
world_map = folium.Map(location=[0,0],zoom_start=2)

while i < pings: 
    time.sleep(2)
    response = requests.get("http://api.open-notify.org/iss-now.json")
    resp = response.json()
    print(response.status_code)   #simple checker returning 200 if request passed through
    print(response.json())        #sends back the API response is json format
    lat = resp['iss_position']['latitude']
    long = resp['iss_position']['longitude']
    t = datetime.now().time()
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}')
    w = weather.json()
    temp = w['main']['temp']-273
    city =  w['name']
    folium.CircleMarker([lat, long],popup=str(t)+' temperature: ' + str(temp) + ' ville: ' + str(city)).add_to(world_map)
    
    i+=1






world_map.save('modele.html')
