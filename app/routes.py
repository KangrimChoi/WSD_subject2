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

#POST1 사용자 생성
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


#GET1 사용자 목록 조회
@user_bp.route('/', methods=['GET'])
def get_users():
    if not user_db:
        return build_response(status="fail", code=404, message="No users found")
    return build_response(status="success", code=200, message="Users retrived", data=list(user_db.values()))

#GET2 특정 사용자 조회
@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in user_db:
        return build_response(status="fail", code=404, message="User not found")
    return build_response(status="success", code=200, message="User retrived", data=user_db[user_id])




#DELETE
