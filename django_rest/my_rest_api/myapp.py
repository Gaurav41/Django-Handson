import requests
import json

# URL="http://127.0.0.1:8000/api/studentapi/"
URL="http://127.0.0.1:8000/api/studentapi_cls/" ## class based



def get_data(id=None):
    data ={}
    if id is not None:
        data = {"id":id}

    r = requests.get(url = URL,data=json.dumps(data))
    data = r.json()
    print(data)

# get_data()

def post_data():
    data={
        'name':'Amit',
        'roll': 50,  
        # 'roll':-1,      ## {'roll': ['Invalid roll number']}
        'city':"Pune"
    }

    json_data = json.dumps(data)
    response = requests.post(url=URL,data=json_data)
    data = response.json()
    print(data)

# post_data()

def update_data():
    data={
        'id':1,
        'name':'Gaurav',
        'roll': 7,  
        'city':'Pune'
    }

    json_data = json.dumps(data)
    response = requests.put(url=URL,data=json_data)
    data = response.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':7,
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL,data=json_data)
    data = response.json()
    print(data)

# delete_data()

get_data()
# post_data()
# update_data()
# delete_data()
