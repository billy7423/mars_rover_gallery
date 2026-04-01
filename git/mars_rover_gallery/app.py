# Flask 라이브러리에서 필요한 기능들을 가져옵니다
from flask import Flask, jsonify
from flask_cors import CORS

# Flask 애플리케이션을 만듭니다
app = Flask(__name__)

# CORS 설정 - 브라우저에서 우리 서버에 접근할 수 있도록 허용합니다
CORS(app)

# 홈페이지 라우트 - 서버가 잘 작동하는지 확인용
@app.route('/')
def home():
    """
    웹브라우저에서 http://localhost:5000 으로 접속했을 때 실행되는 함수
    """
    return "화성 로버 사진 갤러리 백엔드가 작동 중입니다! 🚀"

# API 엔드포인트 - 사진 데이터를 제공합니다
@app.route('/api/photos')
def get_photos():
    """
    프론트엔드에서 사진 데이터를 요청했을 때 실행되는 함수
    지금은 테스트용 가짜 데이터를 반환합니다
    """
    # 화성 로버 사진들을 모방한 테스트 데이터
    # 실제로는 NASA API에서 가져올 예정이지만, 지금은 연습용 이미지를 사용합니다
    mock_photos = [
        {
            "id": 1,
            "img_src": "https://picsum.photos/400/300?random=1",
            "earth_date": "2024-01-15",
            "rover_name": "Perseverance",
            "camera": "NAVCAM",
            "description": "화성 표면의 놀라운 암석 지형"
        },
        {
            "id": 2,
            "img_src": "https://picsum.photos/400/300?random=2",
            "earth_date": "2024-01-14",
            "rover_name": "Curiosity",
            "camera": "MAST",
            "description": "화성의 붉은 모래 언덕"
        },
        {
            "id": 3,
            "img_src": "https://picsum.photos/400/300?random=3",
            "earth_date": "2024-01-13",
            "rover_name": "Perseverance",
            "camera": "FRONT_HAZCAM",
            "description": "화성 크레이터 가장자리의 풍경"
        },
        {
            "id": 4,
            "img_src": "https://picsum.photos/400/300?random=4",
            "earth_date": "2024-01-12",
            "rover_name": "Curiosity",
            "camera": "CHEMCAM",
            "description": "화성의 신비로운 바위 구조물"
        },
        {
            "id": 5,
            "img_src": "https://picsum.photos/400/300?random=5",
            "earth_date": "2024-01-11",
            "rover_name": "Perseverance",
            "camera": "REAR_HAZCAM",
            "description": "화성 탐사선의 바퀴 자국"
        },
        {
            "id": 6,
            "img_src": "https://picsum.photos/400/300?random=6",
            "earth_date": "2024-01-10",
            "rover_name": "Curiosity",
            "camera": "MAHLI",
            "description": "화성 표면의 독특한 광물 결정"
        }
    ]

    # Python 딕셔너리 리스트를 JSON 형태로 변환해서 반환합니다
    # JSON은 웹에서 데이터를 주고받을 때 사용하는 표준 형식입니다
    return jsonify(mock_photos)

# 서버를 실행하는 부분
if __name__ == '__main__':
    # debug=True 설정으로 코드 변경시 자동으로 서버가 재시작됩니다
    app.run(debug=True, port=5000)
