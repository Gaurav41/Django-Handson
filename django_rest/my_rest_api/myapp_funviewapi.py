import requests
import json


# URL="http://127.0.0.1:8000/api/funviewapi/" 
URL="http://127.0.0.1:8000/api/rest_api/" 



def get_data(id=None):
    data ={}
    if id is not None:
        data = {"id":id}
    headers = { 'content-type':'application/json'}
    r = requests.get(url = URL,headers=headers,data=json.dumps(data))
    data = r.json()
    print(data)


# get_data()

def post_data():
    data={
        'name':'shubham',
        'roll': 110,  
        # 'roll':-1,      ## {'roll': ['Invalid roll number']}
        'city':"Pune"
    }
    headers = { 'content-type':'application/json'}
    json_data = json.dumps(data)
    response = requests.post(url=URL,headers=headers,data=json_data)
    data = response.json()
    print(data)

# post_data()

def update_data():
    data={
        'id':9,
        'name':'Amit',
        'roll': 51,  
        'city':'Pune'
    }

    json_data = json.dumps(data)
    headers = { 'content-type':'application/json'}
    response = requests.put(url=URL,headers=headers,data=json_data)
    data = response.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':10,
    }
    json_data = json.dumps(data)
    headers = { 'content-type':'application/json'}
    response = requests.delete(url=URL,headers=headers,data=json_data)
    data = response.json()
    print(data)

# delete_data()

# get_data(1)
# post_data()
# update_data()
delete_data()
