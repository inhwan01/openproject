document.addEventListener('DOMContentLoaded', function () {
    // 백엔드 API 엔드포인트 주소
    const apiUrl = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid?serviceKey=OPS4fohR6WPWKsxqowtr+4b4tg053PyFaFhn3iIo0pyXfMA1Bsyx4x1j7P0TOmVbA67Y5V/UrGoQwyCO83K4LQ==&busRouteId=124000038&resultType=xml';

    // 버스 정보를 표시할 div 요소
    const busInfoDiv = document.getElementById('bus-info');

    // 백엔드에서 데이터를 받아오는 함수
    async function getBusInfo() {
        try {
            // 백엔드로 요청 보내기
            const response = await fetch(apiUrl);

            // 응답을 텍스트로 받아오기
            const responseText = await response.text();

            // XML 파싱
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(responseText, 'application/xml');

            // XML 구조를 기반으로 원하는 데이터 추출
            const msgBody = xmlDoc.querySelector('msgBody');
            if (msgBody !== null) {
                const itemNodes = msgBody.querySelectorAll('itemList');

                if (itemNodes.length > 0) {
                    itemNodes.forEach(item => {
                        const busNumber = item.querySelector('plainNo').textContent;
                        const tmX = item.querySelector('tmX').textContent;
                        const tmY = item.querySelector('tmY').textContent;
                        const busLocation = `X: ${tmX}, Y: ${tmY}`;

                        // 새로운 div 요소 생성
                        const busDiv = document.createElement('div');
                        busDiv.innerHTML = `<p>버스 번호: ${busNumber}</p><p>위치: ${busLocation}</p>`;

                        // busInfoDiv에 새로 생성한 div 추가
                        busInfoDiv.appendChild(busDiv);
                    });
                } else {
                    console.log("데이터가 없습니다.");
                }
            } else {
                console.log("응답 데이터의 구조가 예상과 다릅니다.");
            }
        } catch (error) {
            console.error('Error fetching bus information:', error);
        }
    }

    // 페이지 로딩 시 버스 정보 받아오기
    getBusInfo();
});
