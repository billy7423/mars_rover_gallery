// 페이지가 완전히 로드된 후 실행됩니다
document.addEventListener('DOMContentLoaded', function() {
    // 필요한 HTML 요소들을 찾아서 변수에 저장합니다
    const fetchButton = document.getElementById('fetch-photos-btn');
    const photoGallery = document.getElementById('photo-gallery');

    // 로딩 상태를 표시하는 함수
    function showLoading() {
        photoGallery.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #666;">
                <div style="font-size: 2em; margin-bottom: 10px;">🚀</div>
                <div>화성에서 사진을 전송받는 중...</div>
                <div style="margin-top: 10px; font-size: 0.9em;">잠시만 기다려주세요!</div>
            </div>
        `;
    }

    // 개별 사진 카드를 만드는 함수
    function createPhotoCard(photo) {
        // 새로운 div 요소를 만듭니다
        const photoCard = document.createElement('div');
        photoCard.className = 'photo-item';

        // 사진 카드의 HTML 내용을 설정합니다
        photoCard.innerHTML = `
            <img src="${photo.img_src}" alt="${photo.description}" loading="lazy">
            <div style="padding: 15px;">
                <h3 style="margin: 0 0 10px 0; color: #333; font-size: 1.1em;">
                    ${photo.rover_name} 로버
                </h3>
                <p style="margin: 0 0 10px 0; color: #666; font-size: 0.9em;">
                    📅 ${photo.earth_date}
                </p>
                <p style="margin: 0 0 10px 0; color: #666; font-size: 0.9em;">
                    📷 ${photo.camera} 카메라
                </p>
                <p style="margin: 0; color: #777; font-size: 0.95em; line-height: 1.4;">
                    ${photo.description}
                </p>
            </div>
        `;

        return photoCard;
    }

    // 사진들을 화면에 표시하는 함수
    function displayPhotos(photos) {
        // 갤러리 영역을 비웁니다
        photoGallery.innerHTML = '';

        // 각 사진에 대해 카드를 만들어서 갤러리에 추가합니다
        photos.forEach(photo => {
            const photoCard = createPhotoCard(photo);
            photoGallery.appendChild(photoCard);
        });

        // 성공 메시지를 콘솔에 출력합니다
        console.log(`총 ${photos.length}개의 사진이 성공적으로 표시되었습니다!`);
    }

    // 에러 상태를 표시하는 함수
    function showError(error) {
        photoGallery.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #e74c3c;">
                <div style="font-size: 2em; margin-bottom: 10px;">❌</div>
                <div style="font-size: 1.2em; margin-bottom: 10px;">
                    사진을 가져오는 중 오류가 발생했습니다
                </div>
                <div style="font-size: 0.9em; color: #666;">
                    서버가 실행 중인지 확인해주세요 (python app.py)
                </div>
            </div>
        `;
        console.error('에러 상세:', error);
    }

    // 비동기 함수로 사진 데이터를 가져오는 함수
    async function fetchPhotos() {
        try {
            // 로딩 화면을 보여줍니다
            showLoading();

            // 서버에서 사진 데이터를 가져옵니다
            console.log('서버에 사진 데이터 요청 중...');
            const response = await fetch('http://localhost:5000/api/photos');

            // 응답이 성공적인지 확인합니다
            if (!response.ok) {
                throw new Error(`서버 오류: ${response.status}`);
            }

            // JSON 데이터로 변환합니다
            const photos = await response.json();
            console.log('받은 사진 데이터:', photos);

            // 사진들을 화면에 표시합니다
            displayPhotos(photos);

        } catch (error) {
            // 에러가 발생했을 때 처리합니다
            showError(error);
        }
    }

    // 버튼 클릭 이벤트 리스너를 추가합니다
    fetchButton.addEventListener('click', fetchPhotos);

    // 페이지 로드 시 자동으로 사진을 가져오도록 설정 (선택사항)
    // fetchPhotos();
});
