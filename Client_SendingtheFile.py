'''
This is the Web-client/Front end application.
It sends the File to the Server/backendend to process it further.
The server has to be up and running before the client send the file. Once the Backend/server program recieves the file it process the data in the file,
and sends back the processed output to the client/frontend.
Both client and server has to run seperately.
'''
import json
import requests
with open('User_Data.js') as data_file:

    data = json.load(data_file)
    print(data)
#    payload = data[data_file]
    headers = {'content-type': 'application/json'}
print(data)

client = requests.post('http://127.0.0.1:5009/skill/health',json=data,headers=headers)
resp = client.json()
print("response is", resp)