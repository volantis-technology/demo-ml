import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepal_length':1, 'sepal_width':1, 'petal_length':1, 'petal_width':1})

print(r.json())
