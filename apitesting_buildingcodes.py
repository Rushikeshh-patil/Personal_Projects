from urllib.request import urlopen
import json 
import requests
from urllib.parse import urlencode

def searchdob(borough, house_number):
    app_token = 'JRzXhDCoskeaC7oyCwEny9HRX'
    endpoint = f'https://data.cityofnewyork.us/resource/ic3t-wcy2.json?$$app_token={app_token}&'
    # api_secret = '2hypbqgitvabt0ux3cu4wtiawwbhsze67u2q914qz1xmci5gkj'
    data = urlencode({'borough':f'{borough}','house__':f'{house_number}'})
    url = endpoint + data
    print(url)
    r = requests.post(url)
    recieved = r.json()

    return recieved


print(searchdob('BROOKLYN',6711))


