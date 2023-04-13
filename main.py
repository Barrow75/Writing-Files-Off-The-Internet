import requests


url = "Enter the url of the website you would like to get content from"

response = requests.get(url)

with open("name of file that you want the content to be written in.txt", "w") as f:
    f.write(response.text)
