from urllib.request import urlopen
import json 


url = 'https://data.cityofnewyork.us/resource/ic3t-wcy2.json?borough=BRONX&job_type=A1&job_status=P&house__=2952'
# api_secret = '2hypbqgitvabt0ux3cu4wtiawwbhsze67u2q914qz1xmci5gkj'
app_token = 'JRzXhDCoskeaC7oyCwEny9HRX'

usefulfile = urlopen(url)
data = json.load(usefulfile)





