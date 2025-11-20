from flask import Blueprint, request
from app.utils import build_response

# 블루 프린트 정의
user_bp = Blueprint('user', __name__, url_prefix='/users')

#간단한 API 구현을 위한 인메모리 데이터 저장소 (DB 대용)
user_db = {
    "1": {
        "id": "1",
        "name": "John Doe",
        "email": "john@naver.com"
    }
}

#POST 사용자 생성
@user_bp.route('/', methods=['POST'])
def create_user():
    body = request.get_json()
    if not body or 'id' not in body or 'name' not in body:
        return build_response(status="fail", code=400, message="Invalid request body")
    
    user_id = body['id']
    if user_id in user_db:
        return build_response(status="fail", code=400, message="User already exists")
    
    user_db[user_id] = body
    return build_response(status="success", code=201, message="User created", data=user_db)


#GET

#PUT

#DELETE
