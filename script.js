document.addEventListener('DOMContentLoaded', function () {
    // 페이지 로딩이 완료되면 실행됨

    // 백엔드 API 엔드포인트 주소
    const apiUrl = 'http://ws.bus.go.kr/api/rest/buspos/getLowBusPosByRtid';

    // 버스 정보를 표시할 div 요소
    const busInfoDiv = document.getElementById('bus-info');

    // 백엔드에서 데이터를 받아오는 함수
    async function getBusInfo() {
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();

            // 받아온 데이터를 HTML에 삽입
            data.forEach(bus => {
                const busNumber = bus.plainNo;
                const busLocation = `X: ${bus.tmX}, Y: ${bus.tmY}`;

                // 새로운 div 요소 생성
                const busDiv = document.createElement('div');
                busDiv.innerHTML = `<p>버스 번호: ${busNumber}</p><p>위치: ${busLocation}</p>`;

                // busInfoDiv에 새로 생성한 div 추가
                busInfoDiv.appendChild(busDiv);
            });
        } catch (error) {
            console.error('Error fetching bus information:', error);
        }
    }

    // 페이지 로딩 시 버스 정보 받아오기
    getBusInfo();
});
