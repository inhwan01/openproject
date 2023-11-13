import requests

url = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid'
params ={'serviceKey' : 't서비스키', 'busRouteId' : '124000009'}

response = requests.get(url, params=params)
print(response.content)
