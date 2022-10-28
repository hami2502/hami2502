import os
import requests
import json
from datetime import datetime, time, timedelta

print("hello world.")
print(os.environ["TEST"]=="TEST")

url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2022-10-14"

response=requests.get(url)

data = json.loads(r.content)
sunset = data['results']['sunset'] 
sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) 
print(sunset)
print(sunset_time)
