# Flask 라이브러리에서 필요한 기능들을 가져옵니다
from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import time

# Flask 애플리케이션을 만듭니다
app = Flask(__name__)

# CORS 설정 - 브라우저에서 우리 서버에 접근할 수 있도록 허용합니다
CORS(app)

# 화성 로버와 카메라 정보
ROVERS = ['Curiosity', 'Perseverance', 'Opportunity', 'Spirit']
CAMERAS = ['NAVCAM', 'MAST', 'CHEMCAM', 'MAHLI', 'FRONT_HAZCAM', 'REAR_HAZCAM']

# 사진 설명 템플릿
DESCRIPTIONS = [
    "화성 표면의 놀라운 암석 지형",
    "화성의 붉은 모래 언덕",
    "화성 크레이터 가장자리의 풍경",
    "화성의 신비로운 바위 구조물",
    "화성 탐사선의 바퀴 자국",
    "화성 표면의 독특한 광물 결정",
    "화성 하늘의 구름 형성",
    "화성의 고대 강바닥 흔적",
    "화성 폴라 캡의 얼음 구조",
    "화성 표면의 먼지 폭풍 흔적"
]

def generate_mock_photos(count=6):
    """
    테스트용 가짜 사진 데이터를 생성하는 함수
    실제 프로젝트에서는 NASA API를 사용할 예정입니다
    """
    photos = []
    for i in range(1, count + 1):
        photo = {
            "id": i,
            "img_src": f"https://picsum.photos/400/300?random={i}",
            "earth_date": f"2024-01-{15-i:02d}",  # 날짜를 역순으로 생성
            "rover_name": random.choice(ROVERS),
            "camera": random.choice(CAMERAS),
            "description": random.choice(DESCRIPTIONS)
        }
        photos.append(photo)
    return photos

@app.route('/')
def home():
    """
    홈페이지 - 서버 상태 확인용
    """
    return """
    <h1>🚀 화성 로버 사진 갤러리 백엔드</h1>
    <p>서버가 성공적으로 작동 중입니다!</p>
    <p><a href="/api/photos">API 테스트하기</a></p>
    """

@app.route('/api/photos')
def get_photos():
    """
    사진 데이터를 반환하는 API 엔드포인트
    """
    try:
        # 실제 API 호출을 시뮬레이션하기 위한 약간의 지연
        time.sleep(1)

        # 요청 파라미터 확인 (나중에 확장 가능)
        count = request.args.get('count', default=6, type=int)
        count = min(count, 20)  # 최대 20개로 제한

        # 테스트 데이터 생성
        photos = generate_mock_photos(count)

        # 성공 로그
        app.logger.info(f"사진 {len(photos)}개를 성공적으로 반환했습니다.")

        return jsonify(photos)

    except Exception as e:
        # 에러 로그
        app.logger.error(f"사진 데이터 생성 중 오류 발생: {str(e)}")
        return jsonify({"error": "사진 데이터를 가져오는 중 오류가 발생했습니다."}), 500

@app.route('/api/health')
def health_check():
    """
    서버 건강 상태 체크 엔드포인트
    """
    return jsonify({
        "status": "healthy",
        "message": "서버가 정상적으로 작동 중입니다",
        "timestamp": time.time()
    })

# 에러 핸들러
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "요청한 페이지를 찾을 수 없습니다."}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "서버 내부 오류가 발생했습니다."}), 500

# 서버를 실행하는 부분
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

# 실제 NASA API 사용 예시 (참고용)
import requests

# NASA API 키가 필요합니다 (api.nasa.gov에서 무료로 발급 가능)
NASA_API_KEY = "1q8EAMJZ0kF5geNjwAIaG9Db3goEyhs8nDlohgD9"  # 실제 사용시에는 본인의 API 키로 교체
NASA_API_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

@app.route('/api/real-photos')
def get_real_photos():
    """
    실제 NASA API에서 화성 로버 사진을 가져오는 함수
    """
    try:
        # NASA API 호출
        params = {
            'sol': 1000,  # 화성 일수
            'api_key': NASA_API_KEY,
            'page': 1
        }

        response = requests.get(NASA_API_URL, params=params)
        data = response.json()

        # 데이터 가공
        photos = []
        for photo in data['photos'][:6]:  # 첫 6개만 사용
            processed_photo = {
                'id': photo['id'],
                'img_src': photo['img_src'],
                'earth_date': photo['earth_date'],
                'rover_name': photo['rover']['name'],
                'camera': photo['camera']['full_name'],
                'description': f"{photo['rover']['name']} 로버가 촬영한 화성 사진"
            }
            photos.append(processed_photo)

        return jsonify(photos)

    except Exception as e:
        app.logger.error(f"NASA API 호출 오류: {str(e)}")
        return jsonify({"error": "NASA API 호출 중 오류가 발생했습니다."}), 500
