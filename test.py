import requests
print(requests.get('https://httpbin.org/ip').text)