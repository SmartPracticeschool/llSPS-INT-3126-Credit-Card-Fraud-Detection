import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'time':0, 'v1':-1.359807, 'v7':0.239599,'v13':-0.991390,'v27':0.133558, 'Amount':149.62})

print(r.json())
