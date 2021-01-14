import re, requests, validators
from collections import Counter
from prettytable import PrettyTable

url_input = str(input("Enter url: ").strip())

if not url_input.startswith(("http://", "https://")):
    try:
        url = "https://" + url_input
    except:
        url = "http://"  + url_input

if url_input.startswith(("http://", "https://")):
    url = url_input

validators.url(url)
if not validators.url(url):
    print("Entered link is not correct...")
    quit()

response = requests.get(url)

result = re.findall( r"\"(?:http[s]?://)([^:/\s\"]+)/?[^\"]*\"", response.text)
result.sort()

pt = PrettyTable(field_names=["word", "counter"])
pt.add_rows(list(Counter(result).most_common()))
print(pt)