import json

import requests
from pprint import pprint

url = "http://qa.tab.kitecash.in/simulator/fis/transaction/authorization"
file = open("C:\\Users\\Bestpeers\\Desktop\\PRE_AUTH.txt", 'r')
json_input = file.read()
request_json = json.loads(json_input)
response = requests.post(url, request_json)

# print("Response Request :")
# pprint(response.request)
print("Response Content :")
pprint(response.content)
# print("Response Cookies :")
# pprint(response.cookies)
print("Response Status Code :")
pprint(response.status_code)
# print("Response Headers :")
# pprint(response.headers)
# print("Response Encoding :")
# pprint(response.encoding)
# print("Response JSon :")
# pprint(response.json())
# print("Response Url :")
# pprint(response.url)
# print("Response Reason :")
# pprint(response.reason)
# print("Response History :")
# pprint(response.history)
# print("Response Elapsed :")
# pprint(response.elapsed)
# print("Response raise for status :")
# pprint(response.raise_for_status())
# print("Response isRedirect :")
# pprint(response.is_redirect)
# print("Response isPermanent Redirect :")
# pprint(response.is_permanent_redirect)
# print("Response OK :")
# pprint(response.ok)
# print("Response Links :")
# pprint(response.links)
# print("Response iterContent :")
# pprint(response.iter_content())
# data = response.json()
# username = data['username']
# password = data['password']
# token = data['auth_token']
# print("Response Data Extraction :")
# print("userName:%s\nPassword:%s\nAuthorization Token:%s"
#       % (username, password, token))
