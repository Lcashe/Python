import re
import requests
from collections import Counter
from prettytable import PrettyTable

url_input = input("Enter url: ").strip()
if not url_input.startswith(('http://', 'https://')):
    url_input = 'https://' + url_input

response = requests.get(url_input)

result = re.findall( r"\"(?:http[s]?://)([^:/\s\"]+)/?[^\"]*\"", response.text)

def count_words(List):
    for word, counter in Counter(List).most_common():
        print(f"{word} matches {counter} times")

count_words(result)

pt = PrettyTable()
pt.add_rows(list(Counter(result).most_common()))
print(pt)