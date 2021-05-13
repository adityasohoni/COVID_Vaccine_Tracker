import requests
import time
import os
from datetime import date
from datetime import datetime
district_id = '363'


def alert(name):
    os.system('spd-say "The vaccine is available at {}"'.format(name))


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


while(1):
    time.sleep(3.4)
    date_var = date.today().strftime("%d-%m-%Y")
    # date_var = '11-05-2021'
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date_var

    try:
        r = requests.get(url=URL, headers=headers)
    except requests.ConnectionError:
        print("No Network at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        continue

    print(r.status_code)
    data = r.json()

    flag = 0

    for center in data['centers']:
        if center['center_id'] != 629727 and center['center_id'] != 629727:
            for session in center['sessions']:
                if session['available_capacity'] > 0 and session['min_age_limit']<45:
                    alert(center['name'])
                    print(center['name'])
                    print(center['address'])
                    time.sleep(2.8)
                    print(session)
                    flag=1
    if flag == 0:
        print("Not available at " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

