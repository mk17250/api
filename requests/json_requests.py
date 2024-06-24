import requests

# get json data
url = 'https://api.github.com/events'

response = requests.get(url=url)
events = response.json()

# response can be examined using methods eg
print(events[0])

# # post json data 
url1 = 'http://httpbin.org/post'

data = {'name': 'Matthew King'}

response1 = requests.post(url=url1, json=data)
print(response1.text)