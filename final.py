import re, requests
from collections import Counter
from prettytable import PrettyTable

url_input = input("Enter url: ")

url_checked = re.findall(r'https?://\S+', url_input)[0] # берем первый элемент

if url_input != url_checked: # проверка валидности ссылки
    print("Entered url is invalid")
else:
    pass

response = requests.get(str(url_checked)) # запрос на введенную ссылку

result = re.findall( r"\"(?:http[s]?://)([^:/\s\"]+)/?[^\"]*\"", response.text) # фильтрация ссылок

result.sort() # sorting by alphabet 

# link - https://stackoverflow.com/

def count_words(List):
    for link, counter in Counter(List).most_common():
        print(f"{link} matches {counter} time(s)")

count_words(result)

counter_list = list(Counter(result).most_common())