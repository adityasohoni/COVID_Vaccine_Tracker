import requests
import time
import os
from datetime import date, datetime

#STEPS TO FOLLOW
# Go to this this url👇 in a browser to get your state_id
# https://cdn-api.co-vin.in/api/v2/admin/location/states
# Go to this this url👇 in a browser to get your district_id
# https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}

def alert(name):
    os.system('spd-say "The vaccine is available at {}"'.format(name))



district_id = '294'

# sending get request and saving the response as response object
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

while (1):
    time.sleep(3.4)
    date_var = date.today().strftime("%d-%m-%Y")
    # URL = "http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date_var

    r = requests.get(url=URL, headers=headers)
    # r = requests.get("https://google.com")

    print(r.status_code)
    # extracting data in json format
    data = r.json()

    flag = 0

    for center in data['centers']:
        for session in center['sessions']:
            if session['vaccine'] == 'COVAXIN' and session['available_capacity'] > 0:
                # if session['available_capacity'] > 0:
                if center['center_id'] != 634261:
                    alert(center['name'])
                    print(center['name'])
                    time.sleep(2.8)
                    print(session)
                    flag = 1
    if flag == 0:
        print("Not available at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
