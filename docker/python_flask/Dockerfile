# 베이스 이미지로 Python 3.10 버전을 사용합니다.
FROM python:3.10-slim

# 컨테이너의 작업 디렉터리를 /app으로 설정합니다.
WORKDIR /app

# 로컬의 requirements.txt 파일을 컨테이너의 /app 디렉터리로 복사합니다.
COPY requirements.txt .

# 필요한 파이썬 패키지를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드를 컨테이너의 /app 디렉터리로 복사합니다.
COPY . .

# 컨테이너가 외부에서 5000번 포트를 사용함을 알립니다.
EXPOSE 5000

# 컨테이너가 시작될 때 실행할 명령어를 설정합니다.
CMD ["flask", "run", "--host=0.0.0.0"]