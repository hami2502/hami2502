import os
import requests
import json
from datetime import datetime, time, timedelta
from todoist_api_python.api import TodoistAPI

def calc_last_sunday_of_march(year):
	return calc_last_sunday_of_month(year, 3, 31)

def calc_last_sunday_of_october(year):
	return calc_last_sunday_of_month(year, 10, 31)

def calc_last_sunday_of_month(year, month, day):
	last_day_of_month = datetime.datetime(year, month, day)
	weekday_last_day_of_month = last_day_of_month.weekday()

	if weekday_last_day_of_month==6:
		return last_day_of_month
	else:
		return datetime.datetime(year, month, day-1-weekday_last_day_of_month)

def add_quick_task(task_string):
    api = TodoistAPI(os.environ["TODOIST_API_KEY"])
    try:
        tasks = api.add_quick_task(task_string)
    except Exception as error:
        print(error)
 
#print("hello world.")
#print(os.environ["TEST"]=="TEST")
#date="2022-10-28"
#url="https://api.sunrise-sunset.org/json?lat=49.460983&lng=11.061859&date="+date

#response=requests.get(url)

#data = json.loads(response.content)
#sunset = data['results']['sunset'] 
#       sunset_time = time(int(sunset[11:13]), int(sunset[14:16])) 
#print(sunset)
#(sunset_time)

#date_string = date+" "+sunset
#print(date_string)
#format = '%Y-%m-%d %I:%M %p'
#my_date = datetime.strptime(date_string, format)
#print(my_date)

#result_1 = my_date + timedelta(hours=1)
#print(result_1)

#print(calc_last_sunday_of_october(2022))
add_quick_task("jeden Freitag gggg")