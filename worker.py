import time
import requests

while True:
    print('Incrementing the counter at https://stefanini-counter.herokuapp.com/')
    requests.post("https://stefanini-counter.herokuapp.com/api/counter")
    time.sleep(5)