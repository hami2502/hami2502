import os
import requests
import json
from datetime import datetime, time, timedelta

print("hello world.")
print(os.environ["TEST"]=="TEST")

url="https://api.sunrise-sunset.org/json?lat=49.460983&lng=11.061859&date=2022-10-28"

response=requests.get(url)

data = json.loads(response.content)
sunset = data['results']['sunset'] 
#       sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) 
print(sunset)
#(sunset_time)
