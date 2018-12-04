'''
This is the Web-Sever Application or Program.
It receives the File from the client/frontend and process it further.
The server has to be up and running before the client send the file. Once it recieves the file it process the data in the file,
and sends back the processed output to the client/frontend.
Both client and server has to run seperately.
'''
from collections import OrderedDict
from flask import Flask,render_template,jsonify,json,request
import pandas as pd

userskills = OrderedDict
userskills = {
    'id': [],
    'skill': []
}

app=Flask(__name__)
@app.route('/skill/health', methods=['POST'])
# This is how the api would look like
# /rest api - skill/health
#http://127.0.0.1:5009/skill/health is the address where the client shall send the request.



def get_userdata():
#    print('Before REST API')

    skill_data=[]

    if request.method == 'POST':
        try:
            # json file to be recieved
            try:
                content = request.json
            except:
                print("File not Found")
            #posted_data = json.load(content)
            print(content)
            skill_data = skill_evaluate(content)
            print('skill is:',skill_data[1])
            #Updating the dictionary
            userskills['id'].append(skill_data[0])
            userskills['skill'].append(skill_data[1])

            # Writing the Dictionary to csv
            if skill_data[0]=='99999':
                df = pd.DataFrame.from_dict(userskills, orient="columns")
                df.to_csv("health_skills.csv",index=False)
                print(userskills)


            return (json.dumps(skill_data[1]))

        except Exception as e:
            print("ERROR in Retrieving User Data -", e)



def skill_evaluate(user_data):
    dic = {}
    dic=user_data
    id=dic['customer']['id']
    postcode=dic['customer']['postcode']
    age=dic['customer']['age']
    gender=dic['customer']['gender']
    has_provider=dic['customer']['has_provider']
    has_children=dic['customer']['has_children']
    marital_status=dic['customer']['marital_status']
    cover_type=dic['customer']['cover_type']
    if int(has_provider)==0:
        return (id,'S001')
    if (int(postcode) >= 2000 and int(postcode) <= 4999):
        if(int(has_provider)==0 and cover_type=='combined'):
            return (id,'S002')
        if(marital_status=='married' and int(has_children)==1):
            return (id,'S001')
        else:
            return(id,'S004')
    if (gender=='female' and int(has_children)==1 and marital_status!='married'):
        return(id,'S003')
    else:
        return(id,'S004')


app.run(host='127.0.0.1', port=5009)