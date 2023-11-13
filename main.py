import requests
from json.decoder import JSONDecodeError

url = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid' #저상버스위치조회
params ={'serviceKey' : '서비스 키', 'busRouteId' : '124000038', 'resultType': 'json'}

response = requests.get(url, params=params)

if response.status_code == 200:
   try:
        # JSON 형식의 응답을 파싱
        data = response.json()

        # 조회 결과 확인
        msg_body = data.get('ServiceResult', {}).get('msgBody', {})
        item_list = msg_body.get('itemList', [])

        if not item_list:
            print("데이터가 없습니다.")
        else:
            for item in item_list:
                bus_number = item.get('plainNo', '')
                bus_location = item.get('tmX', ''), item.get('tmY', '')

                print(f"버스 번호: {bus_number}, 위치: {bus_location}")
   
   except JSONDecodeError as e:
        print(f"JSON 디코딩 오류: {e}")
        print(response.text)  # 오류 발생 시 응답 텍스트 출력
else:
    print(f"API 요청 실패: {response.status_code}")
    print(response.text)  # 실패 시 응답 텍스트 출력