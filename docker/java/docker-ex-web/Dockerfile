# 스테이지 1: 애플리케이션 빌드
# Gradle이 미리 설치된 이미지를 사용해 빌드 환경 구축
FROM gradle:8.5-jdk21 AS builder

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# Gradle Wrapper 및 소스 코드 복사
COPY . .

# Gradle을 사용하여 애플리케이션 빌드
RUN gradle clean build -x test

# 스테이지 2: 최종 이미지 생성
# 가볍고 JDK 21이 설치된 이미지를 사용
FROM openjdk:21-jdk-slim

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 빌더 스테이지에서 빌드된 JAR 파일을 최종 이미지로 복사
COPY --from=builder /app/build/libs/*.jar app.jar

# 컨테이너가 외부에서 8080번 포트를 사용함을 알립니다.
EXPOSE 8080

# 컨테이너 시작 시 JAR 파일 실행
ENTRYPOINT ["java", "-jar", "app.jar"]
