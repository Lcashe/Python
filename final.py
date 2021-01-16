import re, requests
from collections import Counter

url_input = input("Enter url: ")

url_checked = re.findall(r'https?://\S+', url_input)[0] # берем первый элемент


if url_input != url_checked: # проверка валидности ссылки
    print("Entered url is invalid")
else:
    pass

response = requests.get(str(url_checked)) # запрос на введенную ссылку
result = re.findall(r'/[A-Za-z.]+/', response.text) # фильтрация ссылок

def count_words(List): # функция подсчета ссылок
    for word, counter in Counter(List).items():
        print(f"{word} matches {counter} times")

count_words(result)