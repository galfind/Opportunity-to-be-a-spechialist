import requests
url = 'https://citaty.info/random/data'
resp = requests.get(url)
resp
print(resp.text)
