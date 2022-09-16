import requests
#print(requests.__version__)

print(requests.get("http://www.google.com/"))

raw_url = "https://raw.githubusercontent.com/Baidadan67/404Lab1/main/request.py"

res = requests.get(raw_url)
print(res.text)