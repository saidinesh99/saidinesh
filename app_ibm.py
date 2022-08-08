from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
#model = pickle.load(open('churn.pkl','rb'))
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Z1Vo2KCboYL-ZJ8I7iBtUpCJhmYzqKQ1jiz19RLm6_Gz"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def admin():
    a= request.form["gender"]
    if (a == 'f'):
        a=0
    if (a == 'm'):
        a=1
    b= request.form["srcitizen"]
    if (b == 'n'):
        b=0
    if (b == 'y'):
        b=1
    c= request.form["partner"]
    if (c == 'n'):
        c=0
    if (c == 'y'):
        c=1
    d= request.form["dependents"]
    if (d == 'n'):
        d=0
    if (d == 'y'):
        d=1
    e= request.form["tenure"]
    f= request.form["phservices"]
    if (f == 'n'):
        f=0
    if (f == 'y'):
        f=1    
    g= request.form["multi"]
    if (g == 'n'):
        g=0
    if (g == 'nps'):
        g=1
    if (g == 'y'):
        g=2
    h= request.form["is"]
    if (h == 'dsl'):
        h=0
    if (h == 'fo'):
        h=1
    if (h == 'n'):
        h=2
    i= request.form["os"]
    if (i == 'n'):
        i=0
    if (i == 'nis'):
        i=1
    if (i == 'y'):
        i=2
    j= request.form["ob"]
    if (j == 'n'):
        j=0
    if (j == 'nis'):
        j=1
    if (j == 'y'):
        j=2
    k= request.form["dp"]
    if (k == 'n'):
        k=0
    if (k == 'nis'):
        k=1
    if (k == 'y'):
        k=2       
    l= request.form["ts"]
    if (l == 'n'):
        l=0
    if (l == 'nis'):
        l=1
    if (l == 'y'):
        l=2
    m= request.form["stv"]
    if (m == 'n'):
        m=0
    if (m == 'nis'):
        m=1
    if (m == 'y'):
        m=2        
    n= request.form["smv"]
    if (n == 'n'):
        n=0
    if (n == 'nis'):
        n=1
    if (n == 'y'):
        n=2 
    o= request.form["contract"]
    if (o == 'mtm'):
        o=0
    if (o == 'oyr'):
        o=1
    if (o == 'tyrs'):
        o=2
    p= request.form["pmt"]
    if (p == 'ec'):
        p=2
    if (p == 'mail'):
        p=3
    if (p == 'bt'):
        p=0 
    if (p == 'cc'):
        p=1    
    q= request.form["plb"]
    if (q == 'n'):
        q=0
    if (q == 'y'):
        q=1 
    r= request.form["mcharges"]
    s= request.form["tcharges"] 

    t=[[int(g),int(h),int(i),int(j),int(k),int(l),int(m),int(n),int(o),int(p),int(a),int(b),int(c),int(d),int(e),int(f),int(q),float(r),float(s)]]        
    #x = model.predict(t)
    payload_scoring = {"input_data": [{ "fields": ["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18"],
                            "values": t}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/83ab06ee-82f8-4529-b2ff-36a18ea73e81/predictions?version=2022-08-04', json=payload_scoring,
     headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    pred= response_scoring.json()
    x= pred['predictions'][0]['values'][0][0]
    print(x)
    if (x == 0):
        y ="No"
        return render_template("predno.html", z = y)

    if (x == 1):
        y ="Yes"
        return render_template("predyes.html", z = y)       

if __name__ == '__main__':
    app.run(debug = False)