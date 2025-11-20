from flask import jsonify

def build_response(data=None, message="", status="success", code=200):
    """응답 포맷 표준화"""
    
    reponse_body={
        "status": status,
        "message": message,
        "data": data if data is not None else {}
    }
    
    return jsonify(reponse_body), code
