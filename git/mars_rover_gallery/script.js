// 페이지가 완전히 로드된 후 실행됩니다
document.addEventListener('DOMContentLoaded', function() {
    // 버튼 요소를 찾아서 변수에 저장합니다
    const fetchButton = document.getElementById('fetch-photos-btn');

    // 버튼을 클릭했을 때 실행될 함수를 정의합니다
    fetchButton.addEventListener('click', function() {
        // 브라우저의 개발자 도구 콘솔에 메시지를 출력합니다
        // F12를 눌러서 개발자 도구를 열고 Console 탭을 확인해보세요!
        console.log('버튼이 클릭되었습니다! 🚀');

        // 사용자에게 알림을 보여줍니다
        alert('곧 화성 로버 사진들을 가져올 예정입니다!');
    });
});
