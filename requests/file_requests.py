import requests

# set url
url = 'http://httpbin.org/post'
# set paarams to be added to query (get has no body, fetch and put do)

files = {'file': open('car_brands.csv', 'rb')}

# make request and get response 
response = requests.post(url=url, files=files)
# response = response.json()

# response can be examined using methods eg
print(response.status_code)
print(response.text) 


# many files demo 

files = [
    ('file1', ('car_brands.csv', open('car_brands.csv', 'rb'), 'csv')),
    ('file2', ('car_brands.csv', open('car_brands.csv', 'rb'), 'csv')),
]

# make request and get response 
response = requests.post(url=url, files=files)
# response = response.json()

# response can be examined using methods eg
print(response.status_code)
print(response.text) 