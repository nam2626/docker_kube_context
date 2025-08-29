from flask import Flask, render_template

# Flask 애플리케이션 인스턴스를 생성합니다.
app = Flask(__name__)

# 루트 URL("/")에 대한 라우팅을 설정합니다.
# 사용자가 이 URL로 접속하면 home() 함수가 실행됩니다.
@app.route('/')
def home():
    # 'index.html' 템플릿 파일을 렌더링하여 반환합니다.
    # 템플릿 파일은 'templates' 폴더에 있어야 합니다.
    return render_template('index.html')

# '/about' URL에 대한 라우팅을 설정합니다.
@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'

if __name__ == '__main__':
    # 애플리케이션을 실행합니다.
    # debug=True는 개발 모드로, 코드를 수정하면 서버가 자동으로 재시작됩니다.
    app.run(debug=True, host='0.0.0.0')