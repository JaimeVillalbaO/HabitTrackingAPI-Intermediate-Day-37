import requests
from datetime import datetime
import os

'''https://pixe.la/v1/users/jaimevi/graphs/graph1.html'''

username = 'jaimevi'
token = os.environ.get('TOKEN_PIXEL')

# create a username
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : token,
    'username' : username,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# create a Graph
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_params = {
    'id' : 'graph1',
    'name' : 'Reading Graph', 
    'unit' : 'pages' , 
    'type' : 'int',
    'color' : 'sora'
}

headers = {
    'X-USER-TOKEN' : token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# edit a graph

edit_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'
# response_1 = requests.put(url=edit_endpoint, json={'timezone':'EST'}, headers=headers)
# print(response_1.text)


# post a pixel

postpixel_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'

today = (datetime.now()).strftime('%Y%m%d')
# print(today)

pixel_params = {
    'date': today,
    'quantity' : input('How many pages did you read today?  '),
}

response_2 = requests.post(url=postpixel_endpoint, json=pixel_params, headers=headers)
print(response_2.text)


# edit pixel 
editpixel_endpoint = f'{postpixel_endpoint}/{today}'
# response_3 = requests.put(url= editpixel_endpoint, json={'quantity': '15'}, headers=headers)
# print(response_3.text)


# dalate  a pixel
delatepixel_endpoint = f'{postpixel_endpoint}/{today}'
# response = requests.delete(url=delatepixel_endpoint, headers=headers)
# print(response.text)