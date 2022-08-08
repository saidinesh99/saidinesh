import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Z1Vo2KCboYL-ZJ8I7iBtUpCJhmYzqKQ1jiz19RLm6_Gz"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{ "fields": ["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18"],
                        "values": [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/83ab06ee-82f8-4529-b2ff-36a18ea73e81/predictions?version=2022-08-04', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
pred= response_scoring.json()
x= pred['predictions'][0]['values'][0][0]
print(x)