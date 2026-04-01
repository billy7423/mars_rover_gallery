// 페이지가 완전히 로드된 후 실행됩니다
document.addEventListener('DOMContentLoaded', function() {
    // 버튼 요소를 찾아서 변수에 저장합니다
    const fetchButton = document.getElementById('fetch-photos-btn');

    // 버튼을 클릭했을 때 실행될 함수를 정의합니다
    fetchButton.addEventListener('click', function() {
        console.log('사진 데이터를 가져오는 중...');

        // 백엔드 서버에서 사진 데이터를 가져옵니다
        // fetch()는 서버와 통신하는 JavaScript 함수입니다
        fetch('http://localhost:5000/api/photos')
            .then(response => {
                // 서버 응답을 JSON 형태로 변환합니다
                return response.json();
            })
            .then(photos => {
                // 가져온 데이터를 콘솔에 출력해봅시다
                console.log('받은 사진 데이터:', photos);

                // 사용자에게 성공 메시지를 보여줍니다
                alert(`${photos.length}개의 화성 로버 사진을 가져왔습니다!`);
            })
            .catch(error => {
                // 에러가 발생했을 때 처리합니다
                console.error('에러 발생:', error);
                alert('사진을 가져오는 중 오류가 발생했습니다.');
            });
    });
});
