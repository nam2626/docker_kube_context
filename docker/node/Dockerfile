# 베이스 이미지 node.js 22버전 지정
FROM node:22

# 컨테이너 작업 디렉토리 설정
WORKDIR /app

# 로컬의 package.json과 package-lock.json 파일을 컨테이너의 /app 디렉터리로 복사합니다.
# 이 두 파일만 먼저 복사하여 종속성 설치 레이어를 캐싱합니다.
COPY package*.json ./

# 패키지 설치
RUN npm install

# 애플리케이션 소스 코드를 컨테이너의 /app 디렉터리로 복사합니다.
# RUN 명령어 이후에 COPY를 배치하여 빌드 효율을 높입니다.
COPY . .

# 컨테이너가 외부에서 3000번 포트를 사용함을 알립니다.
EXPOSE 3000

# 컨테이너가 시작될 때 실행할 명령어를 설정합니다.
CMD ["node", "app.js"]