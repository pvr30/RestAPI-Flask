# File For Testing The Api

import requests
BASE = 'http://127.0.0.1:5000/'

#response = requests.post(BASE + "helloworld").json()

# Arguments Get Request
#response = requests.get(BASE + 'helloworld/Vishal/20').json()

# response = requests.get(BASE + 'helloworld/harsh').json()


########## Project Start ########

#Create method 
"""
data = [{"name":"Rest Api", "likes":100, "views":100},
        {"name":"Django Tutorial", "likes":1000, "views":10000},
        {"name":"Flask Tutorial", "likes":100000, "views":10}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/'+str(i), data[i]).json()
    print(response)
"""

# Get Method
input() 
response = requests.get(BASE + 'video/2').json()
print(response)

# Update Method
input()
response = requests.patch(BASE + 'video/2', {"name":"Flask"}).json()
print(response)

# Delete Method
input()
response = requests.delete(BASE + 'video/2')
print(response)