import json
import requests

url = 'http://45.82.72.48:8080/loan-api/v1'
#url = 'http://0.0.0.0:8080/loan-api/v1'

headers ={
 'Content-Type':'application/json'
}

def create_loan():
    print('CREATING LOANS from create-loan.json file ')
    f=open('create-loan.json')
    data = json.load(f)

    create_loan_url = url+'/loan'

    for d in data:
        try:
            resp = requests.post(create_loan_url,json.dumps(d),headers=headers,verify=False);
            print("loan created \n")
            print(resp.text)
        except requests.exceptions.ConnectionError:
            pass
create_loan()



def get_loan_by_ids():
    f = open('get-loan.json')
    data = json.load(f)
    print("GETTING LOAN FOR IDs: \n")
    print(' '.join(map(str, data))) 
    get_loan_url = url +"/loans/"

    for d in data:
        try:
            resp = requests.get(get_loan_url+str(d),headers=headers,verify=False)
            print(resp.text)
        except requests.exceptions.ConnectionError:
            pass
get_loan_by_ids()


def update_loan():
    f = open('update-loan.json')
    data = json.load(f)
    print("UPDATING LOANS from update-loan.json\n")
    print(' '.join(map(str, data)))

    update_loan_url = url+"/loans/"

    print("Loans after update \n")
    for d in data:
        try:
            resp = requests.put(update_loan_url+str(d['id']),json.dumps(d),headers=headers,verify=False)
            print(resp.text)
        except requests.exceptions.ConnectionError:
            pass
update_loan()
