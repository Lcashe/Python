import re, requests, validators, sys
from collections import Counter
from prettytable import PrettyTable
from requests.exceptions import ConnectionError, HTTPError
import random

links = ["stackoverflow.com", "google.com", "cppstudio", "asjdak://adsajsda.com"]

choice = int(input("Enter your choice: 1 - Input, \n2 - random link from the list: \nstackoverflow.com, \ngoogle.com, \ncppstudio.com, \nasjdak://adsajsda.com\n\n"))

if choice == 1:
    url_input = str(input("Enter url: ")).strip()
elif choice == 2:
    url_input = random.choice(links)

if not url_input.startswith(("http://", "https://")):
    try:
        url = "https://" + url_input
    except:
        url = "http://"  + url_input

if url_input.startswith(("http://", "https://")):
    url = url_input

validators.url(url)
if not validators.url(url):
    print(f"You have chosen a link: {url}")
    print("Entered link is not correct...")
    sys.exit()

try:
    response = requests.get(url)
except ConnectionError as e:
    print("Ooooops, something went wrong: Connection Error!")
    print(e)
    sys.exit()
except HTTPError as e:
    print(e)
    sys.exit()

result = re.findall( r"\"(?:http[s]?://)([^:/\s\"]+)/?[^\"]*\"", response.text)

pt = PrettyTable(field_names=["word", "counter"])
pt.add_rows(list(Counter(result).most_common()))
print(pt)
