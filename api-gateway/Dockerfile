# 베이스 이미지로 Python 3.9를 사용합니다
FROM python:3.9-slim

# 작업 디렉토리를 설정합니다
WORKDIR /app

# 환경 변수를 설정합니다
# PYTHONDONTWRITEBYTECODE: Python이 pyc 파일을 생성하지 않도록 합니다
# PYTHONUNBUFFERED: Python의 표준 출력을 버퍼링하지 않도록 합니다
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 시스템 의존성을 설치합니다
# gcc: 일부 Python 패키지를 컴파일하는 데 필요할 수 있습니다
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
# uvicorn을 사용하여 FastAPI 애플리케이션을 실행합니다
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]