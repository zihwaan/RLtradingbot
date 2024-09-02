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