import os
import requests
import json
from datetime import datetime, time, timedelta

print("hello world.")
print(os.environ["TEST"]=="TEST")
date="2022-10-28"
url="https://api.sunrise-sunset.org/json?lat=49.460983&lng=11.061859&date="+date

response=requests.get(url)

data = json.loads(response.content)
sunset = data['results']['sunset'] 
#       sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) 
print(sunset)
#(sunset_time)

date_string = date+" "+sunset
print(date_string)
format = '%Y-%m-%d %I:%M %p'
my_date = datetime.strptime(date_string, format)
print(my_date)

result_1 = my_date + timedelta(hours=1)
print(result_1)