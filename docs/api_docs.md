# 트레이딩 봇 API 문서

## 기본 정보

- 기본 URL: `/api/v1`
- 모든 요청과 응답은 JSON 형식입니다.
- 인증이 필요한 엔드포인트의 경우, Authorization 헤더에 Bearer 토큰을 포함해야 합니다.

## 1. 데이터 수집 및 처리

### GET /data/market

최신 시장 데이터를 조회합니다.

**응답**

```json
{
  "timestamp": "2024-09-03T10:00:00Z",
  "data": {
    "symbol": "KR7175330007",
    "price": 150250,
    "volume": 1000000
  }
}
```

### POST /data/collect

특정 기간의 데이터 수집을 시작합니다.

**요청 본문**

```json
{
  "symbol": "KR7175330007",
  "start_date": "2024-09-01",
  "end_date": "2024-09-03"
}
```

**응답**

```json
{
  "success": true,
  "message": "데이터 수집이 시작되었습니다",
  "job_id": "collect_20240903_001"
}
```

### POST /data/process

수집된 데이터의 전처리를 시작합니다.

**요청 본문**

```json
{
  "data_source": "market_data_20240903",
  "features": ["price", "volume", "moving_average"]
}
```

**응답**

```json
{
  "success": true,
  "processed_records": 1000,
  "job_id": "process_20240903_001"
}
```

## 2. 모델 학습

### POST /model/train

모델 학습을 시작합니다.

**요청 본문**

```json
{
  "model_type": "LSTM",
  "hyperparameters": {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100
  },
  "data_source": "processed_data_20240903"
}
```

**응답**

```json
{
  "job_id": "train_20240903_001",
  "status": "started",
  "estimated_completion": "2024-09-03T12:00:00Z"
}
```

### GET /model/status/{job_id}

모델 학습 상태를 확인합니다.

**매개변수**

- `job_id`: 문자열 (경로 매개변수)

**응답**

```json
{
  "job_id": "train_20240903_001",
  "status": "in_progress",
  "progress": 60,
  "current_epoch": 60,
  "total_epochs": 100,
  "current_loss": 0.0015
}
```

## 3. 추론

### POST /inference/predict

현재 시장 데이터를 기반으로 트레이딩 결정을 얻습니다.

**요청 본문**

```json
{
  "market_data": {
    "symbol": "KR7175330007",
    "price": 150250,
    "volume": 1000000,
    "timestamp": "2024-09-03T10:05:00Z"
  }
}
```

**응답**

```json
{
  "timestamp": "2024-09-03T10:05:00Z",
  "action": "매수",
  "confidence": 0.85,
  "predicted_price": 152500
}
```

## 4. 트레이딩 실행

### POST /trade/execute

추론 결과 또는 수동 입력을 기반으로 거래를 실행합니다.

**요청 본문**

```json
{
  "action": "매수",
  "symbol": "KR7175330007",
  "quantity": 1,
  "price": 150250,
  "order_type": "시장가"
}
```

**응답**

```json
{
  "order_id": "ORD20240903001",
  "status": "executed",
  "execution_price": 150300,
  "timestamp": "2024-09-03T10:06:00Z"
}
```

### GET /trade/status/{order_id}

거래 주문 상태를 확인합니다.

**매개변수**

- `order_id`: 문자열 (경로 매개변수)

**응답**

```json
{
  "order_id": "ORD20240903001",
  "status": "체결됨",
  "symbol": "KR7175330007",
  "quantity": 1,
  "execution_price": 150300,
  "timestamp": "2024-09-03T10:06:00Z"
}
```

## 5. 대시보드

### GET /dashboard/performance

트레이딩 성과 지표를 조회합니다.

**쿼리 매개변수**

- `start_date`: 문자열 (YYYY-MM-DD)
- `end_date`: 문자열 (YYYY-MM-DD)

**응답**

```json
{
"total_profit": 10000000,
  "win_rate": 0.65,
  "total_trades": 100,
  "best_performing_symbol": "KR7175330007",
  "worst_performing_symbol": "KR7005930003",
  "daily_returns": [
    {
      "date": "2024-09-01",
      "return": 500250
    },
    {
      "date": "2024-09-02",
      "return": -200500
    },
    {
      "date": "2024-09-03",
      "return": 700750
    }
  ]
}
```

### GET /dashboard/settings

현재 시스템 설정을 조회합니다.

**응답**

```json
{
  "risk_level": "중간",
  "max_trade_size": 10000000,
  "allowed_symbols": ["KR7175330007", "KR7005930003", "KR7035720002"],
  "trading_hours": {
    "start": "09:00",
    "end": "15:30"
  },
  "model_update_frequency": "매일"
}
```

### PUT /dashboard/settings

시스템 설정을 업데이트합니다.

**요청 본문**

```json
{
  "risk_level": "높음",
  "max_trade_size": 15000000,
  "allowed_symbols": ["KR7175330007", "KR7005930003", "KR7035720002", "KR7051910008"],
  "trading_hours": {
    "start": "09:00",
    "end": "15:30"
  },
  "model_update_frequency": "주간"
}
```

**응답**

```json
{
  "success": true,
  "message": "설정이 성공적으로 업데이트되었습니다"
}
```

### GET /dashboard/logs

시스템 로그를 조회합니다.

**쿼리 매개변수**

- `start_date`: 문자열 (YYYY-MM-DD)
- `end_date`: 문자열 (YYYY-MM-DD)
- `log_level`: 문자열 (INFO, WARNING, ERROR)

**응답**

```json
{
  "logs": [
    {
      "timestamp": "2024-09-03T10:00:00Z",
      "level": "INFO",
      "message": "데이터 수집이 성공적으로 완료되었습니다"
    },
    {
      "timestamp": "2024-09-03T10:05:00Z",
      "level": "WARNING",
      "message": "KR7175330007 종목에 대해 높은 변동성이 감지되었습니다"
    },
    {
      "timestamp": "2024-09-03T10:10:00Z",
      "level": "ERROR",
      "message": "거래 실행 실패: 잔액 부족"
    }
  ]
}
```

## 6. 하이퍼파라미터 튜닝

### POST /hyperparameter/tune

하이퍼파라미터 튜닝 작업을 시작합니다.

**요청 본문**

```json
{
  "model_type": "LSTM",
  "parameter_space": {
    "learning_rate": [0.001, 0.01, 0.1],
    "batch_size": [32, 64, 128],
    "num_layers": [1, 2, 3]
  },
  "optimization_metric": "sharpe_ratio",
  "num_trials": 50
}
```

**응답**

```json
{
  "job_id": "tune_20240903_001",
  "status": "started",
  "estimated_completion": "2024-09-04T12:00:00Z"
}
```

### GET /hyperparameter/status/{job_id}

하이퍼파라미터 튜닝 작업의 상태를 확인합니다.

**매개변수**

- `job_id`: 문자열 (경로 매개변수)

**응답**

```json
{
  "job_id": "tune_20240903_001",
  "status": "in_progress",
  "progress": 60,
  "current_trial": 30,
  "total_trials": 50,
  "best_params": {
    "learning_rate": 0.01,
    "batch_size": 64,
    "num_layers": 2
  },
  "best_metric": 1.5
}
```

## 에러 응답

API 요청이 실패할 경우, 다음과 같은 형식의 에러 응답을 반환합니다:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "에러에 대한 상세 설명"
  }
}
```

주요 에러 코드:

- `INVALID_INPUT`: 잘못된 입력 데이터
- `UNAUTHORIZED`: 인증 실패
- `RESOURCE_NOT_FOUND`: 요청한 리소스를 찾을 수 없음
- `INTERNAL_SERVER_ERROR`: 서버 내부 오류

## 변경 이력

- 2024-09-03: 초기 API 문서 작성