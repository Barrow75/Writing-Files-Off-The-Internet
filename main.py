import requests


url = "http://norvig.com/ngrams/sowpods.txt"

response = requests.get(url)

with open("HangMan Words.txt", "w") as f:
    f.write(response.text)