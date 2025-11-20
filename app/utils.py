from flask import jsonify

def build_response(data=None, message="", status="success", code=200):
    """응답 포맷 표준화"""
    
    reponse_body={
        "status": status,
        "message": message,
        "data": data if data is not None else {}
    }
    
    return jsonify(reponse_body), code

## 자주 사용되는 메시지
#404
def user_not_found_response():
    """user 정보 탐색 불가한 경우"""
    return build_response(status="fail", code=404, message="User not found")
