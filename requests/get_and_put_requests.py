# import libraries 
import requests

"""
GET REQUESTS
"""

# set url
url = 'http://httpbin.org/get'
# set paarams to be added to query (get has no body, fetch and put do)
# params appear in the args section
params = {'name': 'Matthew'}


# make request and get response 
response = requests.get(url=url, params=params)
# response = response.json()

# response can be examined using methods eg
print(response.text) 
print(response.status_code)
print(response.url)
print(response.headers)

"""
PUT REQUESTS
"""

url = 'http://httpbin.org/put'
# set paarams to be added to query (get has no body, fetch and put do)
# appear in thr form section of the reponse
data = {'name': 'Matthew', 'job': 'Data Engineer', 'wife': 'Sarah'}

# make request and get response 
response = requests.put(url=url, data=data)
# response = response.json()

# response can be examined using methods eg
print(response.text) 
print(response.status_code)
print(response.url)
print(response.headers)