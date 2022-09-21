import requests
import threading
import time

text = input("give text: ")
url = "https://ngl.link/[PUT USERNAME]"

param = {
    'question': text
    }

while True:
    requests.post(url, data=param)
    text = input("give text: ")
    time.sleep(0.6)


