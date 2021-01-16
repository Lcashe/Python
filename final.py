import re, requests
from collections import Counter
from prettytable import PrettyTable

url_input = str(input("Enter url: "))

url_checked = re.findall(r'(http[s]?://)?\S+', url_input)[0] # берем первый элемент

response = requests.get(str(url_checked)) # запрос на введенную ссылку

result = re.findall( r"\"(?:http[s]?://)?([^:/\s\"]+)/?[^\"]*\"", response.text) # фильтрация ссылок

result.sort() # sorting by alphabet 

# link - https://stackoverflow.com/

pt = PrettyTable(field_names = ["word", "counter"])
pt.add_rows(list(Counter(result).most_common()))
print(pt)