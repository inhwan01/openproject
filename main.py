from flask import Flask, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    # 백엔드 API 엔드포인트 주소
    api_url = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid'
    
    # API 호출 및 데이터 가져오기
    response = requests.get(api_url, params={
        'serviceKey': 'OPS4fohR6WPWKsxqowtr+4b4tg053PyFaFhn3iIo0pyXfMA1Bsyx4x1j7P0TOmVbA67Y5V/UrGoQwyCO83K4LQ==',
        'busRouteId': '124000038',
        'resultType': 'xml'
    })

    if response.status_code == 200:
        try:
            # XML 형식의 응답을 파싱
            root = ET.fromstring(response.text)
            
            # XML 구조를 기반으로 원하는 데이터 추출
            msg_body = root.find(".//msgBody")
            if msg_body is not None:
                item_list = msg_body.findall(".//itemList")

                if item_list:
                    bus_data = [
                        {'bus_number': item.findtext('plainNo', ''),
                         'bus_location': (item.findtext('tmX', ''), item.findtext('tmY', ''))}
                        for item in item_list
                    ]
                    return render_template('front.html', bus_data=bus_data)
                else:
                    return "데이터가 없습니다."
            else:
                return "응답 데이터의 구조가 예상과 다릅니다."
        except ET.ParseError as e:
            return f"XML 파싱 오류: {e}"
    else:
        return f"API 요청 실패: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
