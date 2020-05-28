import requests

def get_time():
    req = 'http://worldclockapi.com/api/json/utc/now'
    value = requests.get(url= req)
    data = value.json()
    #print(data)
    date_time = data['currentDateTime']
    day = data['dayOfTheWeek']
    timezone = data['timeZoneName']
    print(f'Today is {day}')
    print(f'Timezone displayed: {timezone}')
    print(f'Current Date Time is {date_time}')
    return data



if __name__ == "__main__":
    val = get_time()
    #print(val)