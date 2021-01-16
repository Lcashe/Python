import requests, re

response = requests.get("https://www.google.com/")

result = re.findall(r'/[A-Za-z\.]+/', response.text)
print(result)

def count_words(List):
    Dict = {}
    for word in List:
        if word in Dict:
            Dict[word] += 1
        else:
            Dict[word] = 1

    for word, counter in Dict.items():
        print(f"word {word} matches {counter}")

count_words(result) 