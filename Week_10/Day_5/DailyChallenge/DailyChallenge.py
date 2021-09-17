import requests  
from datetime import timedelta 

urls=["https://www.imdb.com","https://www.ynet.co.il", "https://www.google.com" ]
times=[]

for url in urls:
    request_time = requests.get(url).elapsed.total_seconds()
    print(request_time)
    times.append(request_time)
#store request_time in persistent data store
request_dict=dict(zip(urls,times))
print(request_dict)