import requests as req
url = input("Please Enter hostname (eg.http://www.example.com) : ")
resp = req.head(url)
print(resp.headers)


# response = req.get(url)
# 
# print(response.status_code)
# print(response.text)
