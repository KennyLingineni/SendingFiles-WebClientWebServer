"""
This is the Web-client/Front end application for sending 1000000 http request-
It reads a file,converts each row data into request and sends a HTTP request and gets the response back from the web server,
before it send the next request in a loop.

"""
import json
import requests
import pandas as pd
import time

data = pd.read_csv('health_customers.csv')
print(data.head())
print(data.shape)
dict_json = {}
dict_json['customer'] = {
    'id': '',
    'postcode': '',
    'age': '',
    'gender': '',
    'has_provider': '',
    'has_children': '',
    'marital_status': '',
    'cover_type': ''

}

for i in range(data.shape[0]):
    dict_json['customer']['id'] = str(data['id'][i])
    dict_json['customer']['postcode'] = str(data['postcode'][i])
    dict_json['customer']['age'] = str(data['age'][i])
    dict_json['customer']['gender'] = str(data['gender'][i])
    dict_json['customer']['has_provider'] = str(data['has_provider'][i])
    dict_json['customer']['has_children'] = str(data['has_children'][i])
    dict_json['customer']['marital_status'] = str(data['marital_status'][i])
    dict_json['customer']['cover_type'] = str(data['cover_type'][i])
    #    print(dict_json)
    with open("myjson.json", "w") as json_file:
        json.dump(dict_json, json_file)
    with open("myjson.json") as json_file:
        datas = json.load(open('myjson.json'))
        print(datas)
        headers = {'content-type': 'application/json'}
        client = requests.post('http://127.0.0.1:5009/skill/health', json=datas, headers=headers)
        # Waiting for the client response
        #        time.sleep(1)

        resp = client.json()
        print("response is", resp)

