# importing the requests library
import requests
import time
import os

# api-endpoint
pincode = '591313'
date = '09-05-2021'
URL = "http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + pincode + "&date=" + date


def alert(name):
    os.system('spd-say "The vaccine is available at {}"'.format(name))


# sending get request and saving the response as response object
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


while(1):
    time.sleep(3.5)
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
                alert(center['name'])
                print(center['name'])
                time.sleep(4)
                print(session)
                flag=1
    if flag == 0:
        print("Not available")

