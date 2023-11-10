import requests
import time

record_id = 1

while True:
    data = {'id': record_id, 'text': 'test'}
    response = requests.post(
        'http://main-receiver-1:8080/add_record', json=data)

    print(response.json())
    record_id += 1
    time.sleep(20)
