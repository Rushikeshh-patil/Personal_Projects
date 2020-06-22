import json
import base64
import requests
from urllib.parse import urlencode
api_key = 'a59cf2d2b5a84ba6b397cb11f29e30d1'
client_secret = '0d720cd6ab6142b797ebfd9feecc7d07'


def get_token(api_key,client_secret):

    client_cred = f'{api_key}:{client_secret}'
    client_cred_base64 = base64.b64encode(client_cred.encode())
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {'grant_type':'client_credentials'}
    token_headers = {'Authorization' : f'Basic {client_cred_base64.decode()}'}
    r = requests.post(token_url, data = token_data, headers = token_headers)
    token_response_data = r.json()
    access_token = token_response_data['access_token']

    return access_token

def searchonspotify(keyword):

    access_token = get_token(api_key,client_secret)
    keyword = str(keyword)
    endpoint_base = f'https://api.spotify.com/v1/search'
    data = urlencode({'q':keyword, 'type':'track'})
    endpoint = f'{endpoint_base}?{data}'

    api_headers = {'Authorization':f'Bearer {access_token}'}
    r = requests.get(endpoint,headers=api_headers)
    data_back = r.json()

    return data_back

if __name__ == "__main__":
    keyword = input('Please provide a keyword search: ')
    print(searchonspotify(keyword))