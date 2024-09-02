# 베이스 이미지로 Python 3.9를 사용합니다
FROM python:3.9-slim

# 작업 디렉토리를 설정합니다
WORKDIR /app

# 환경 변수를 설정합니다
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 시스템 의존성을 설치합니다
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 프로젝트 의존성을 설치합니다
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 프로젝트 파일들을 복사합니다
COPY . .

# 애플리케이션을 실행합니다
CMD ["python", "main.py"]