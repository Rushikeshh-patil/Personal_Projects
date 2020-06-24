from urllib.request import urlopen
import json 
import requests
from urllib.parse import urlencode


def searchdobpermit(borough, house_number, street_name):
    app_token = 'JRzXhDCoskeaC7oyCwEny9HRX'
    endpoint = f'https://data.cityofnewyork.us/resource/ic3t-wcy2.json?$$app_token={app_token}&'
    # api_secret = '2hypbqgitvabt0ux3cu4wtiawwbhsze67u2q914qz1xmci5gkj'
    data = urlencode({'borough':f'{borough}','house__':f'{house_number}','street_name':f'{street_name}'})
    url = endpoint + data
    print(url)
    r = requests.get(url)
    recieved = r.json()
    return recieved

if __name__ == "__main__":
    borough = input('Please Provide Borough :')
    house_number = input ('Please Provide house number :')
    street_name = input('Please Provide Street Name :')
    data = searchdobpermit(borough,house_number,street_name)
    dictionary = data[0]
    print(f"\nFor {street_name} Job\n")
    for x in dictionary:
        print(f'{x} = {dictionary[x]}' )
        








