import requests

url = 'http://13.215.51.79/img'

files = {'file': open('1.jpg', 'rb').read()}

response = requests.post(url, files=files)

print(response.json())