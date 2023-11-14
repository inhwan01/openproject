import requests
import xml.etree.ElementTree as ET

url = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid'  # 저상버스위치조회
params = {
    'serviceKey': '서비스키',
    'busRouteId': '124000038',
    'resultType': 'xml'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        # XML 형식의 응답을 파싱
        root = ET.fromstring(response.text)

        # XML 구조를 기반으로 원하는 데이터 추출
        msg_body = root.find(".//msgBody")
        if msg_body is not None:
            item_list = msg_body.findall(".//itemList")

            if item_list:
                for item in item_list:
                    bus_number = item.findtext('plainNo', '')
                    bus_location = item.findtext('tmX', ''), item.findtext('tmY', '')

                    print(f"버스 번호: {bus_number}, 위치: {bus_location}")
            else:
                print("데이터가 없습니다.")
        else:
            print("응답 데이터의 구조가 예상과 다릅니다.")
    except ET.ParseError as e:
        print(f"XML 파싱 오류: {e}")
else:
    print(f"API 요청 실패: {response.status_code}")
    print(response.text)
