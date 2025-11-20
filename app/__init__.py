from flask import Flask, request, jsonify
from app.utils import build_response
from app.routes import user_bp
import logging

def create_app():
    """
    앱 인스턴스를 생성하고 설정을 초기화 하는 함수
    """
    app = Flask(__name__)   
    
    ## 블루프린트(라우터) 등록
    app.register_blueprint(user_bp)
    return app
