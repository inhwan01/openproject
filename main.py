import requests

url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt'
params ={'serviceKey' : '서비스키', 'busRouteId' : '124000009', 'startOrd' : '1', 'endOrd' : '10' }

response = requests.get(url, params=params)
print(response.content)
