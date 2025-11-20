from app.routes.users import user_bp
from flask import Flask

app = Flask(__name__)   

## 블루프린트(라우터) 등록
app.register_blueprint(user_bp)

PORT_NUM = 5000
if __name__ == '__main__':
    print(f"** Server is starting on port {{PORT_NUM}} **")
    app.run(debug=True, port=PORT_NUM)
    
    