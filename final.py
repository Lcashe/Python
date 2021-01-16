import requests
import re

response = requests.get("https://www.google.com/")
result = re.findall(r'^(https?:\/\/)?([\w-]{1,32}\.[\w-]{1,32})[^\s@]*$', response.text)
print(result)