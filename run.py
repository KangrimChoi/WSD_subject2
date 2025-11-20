from app.__init__ import create_app

PORT_NUM = 5000
app = create_app()

if __name__ == '__main__':
    print(f"** Server is starting on port {{PORT_NUM}} **")
    app.run(debug=True, port=PORT_NUM)
    
    