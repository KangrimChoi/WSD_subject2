# WSD_subject2: Flask 기반 REST API 서버

이 프로젝트는 Flask를 사용하여 사용자(User)와 상품(Product) 정보를 관리하는 기본적인 REST API 서버를 구현한 것입니다. 각 기능별로 Blueprint를 사용하여 코드를 모듈화했으며, 인메모리 데이터베이스를 통해 API의 동작을 시뮬레이션합니다.

## 📂 폴더 구조

프로젝트의 주요 폴더 구조는 다음과 같습니다.

```
WSD_subject2/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── product.py      # 상품 관련 API 라우트
│   │   └── users.py        # 사용자 관련 API 라우트
│   └── utils.py            # 응답 형식 등 유틸리티 함수
├── run.py                  # Flask 애플리케이션 실행 파일
├── requirments.txt         # 프로젝트의 의존성 라이브러리 목록
└── README.md               # 프로젝트 설명 파일
```

## ✨ 주요 기능

- **사용자 관리**: 사용자 정보 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) (CRUD)
- **상품 관리**: 상품 정보 생성(Create), 수정(Update), 삭제(Delete) (CRUD)
- **모듈화된 라우팅**: Flask Blueprint를 사용하여 기능별로 API 엔드포인트를 분리
- **표준화된 응답**: 모든 API 응답을 일관된 JSON 형식으로 제공

## 🚀 시작하기

### 1. 요구사항

- Python 3.x
- Flask

### 2. 설치

```bash
# Flask 설치
pip install Flask
```

### 3. 실행

프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 서버를 시작합니다.

```bash
python run.py
```

서버는 기본적으로 `http://127.0.0.1:5000`에서 실행됩니다.

## 📖 API 명세

API는 크게 `Users`와 `Products` 두 가지 리소스를 관리합니다.

### Users API

**Base URL**: `/users`

| Method | Endpoint | 설명 | Request Body 예시 |
| :--- | :--- | :--- | :--- |
| `POST` | `/` | 새로운 사용자를 생성합니다. | `{"id": "2", "name": "Jane Doe", "email": "jane@example.com"}` |
| `GET` | `/` | 모든 사용자 목록을 조회합니다. | N/A |
| `GET` | `/<user_id>` | 특정 ID의 사용자 정보를 조회합니다. | N/A |
| `PUT` | `/<user_id>` | 특정 ID의 사용자 정보를 수정합니다. | `{"id": "1", "name": "John Smith", "email": "john.smith@naver.com"}` |
| `DELETE` | `/<user_id>` | 특정 ID의 사용자 정보를 삭제합니다. | N/A |

### Products API

**Base URL**: `/products`

| Method | Endpoint | 설명 | Request Body 예시 |
| :--- | :--- | :--- | :--- |
| `POST` | `/` | 새로운 상품을 등록합니다. | `{"id": "2", "category": "Books", "registration_date": "2025-11-21", "name": "Product B", "price": "25.50"}` |
| `PUT` | `/<product_id>` | 특정 ID의 상품 정보를 수정합니다. | `{"id": "1", "category": "Electronics", "registration_date": "2025-11-20", "name": "Product A-1", "price": "9.99"}` |
| `DELETE` | `/<product_id>` | 특정 ID의 상품 정보를 삭제합니다. | N/A |

---

## 🔧 응답 형식 및 에러 코드

### 성공 응답 형식

모든 성공적인 응답은 다음과 같은 JSON 구조를 가집니다. `data` 필드에는 요청에 대한 결과 데이터가 포함됩니다.

```json
{
    "status": "success",
    "message": "User created",
    "data": {
        "1": {
            "id": "1",
            "name": "John Doe",
            "email": "john@naver.com"
        },
        "2": {
            "id": "2",
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
    }
}
```

### 실패 응답 형식

실패 응답은 `status` 필드에 `fail` 값을 가지며, `data`는 비어 있습니다.

```json
{
    "status": "fail",
    "message": "User not found",
    "data": {}
}
```

### HTTP 상태 코드

| Code | Status | 설명 |
| :--- | :--- | :--- |
| `200 OK` | Success | 요청이 성공적으로 처리되었습니다. (GET, PUT) |
| `201 Created` | Success | 리소스가 성공적으로 생성되었습니다. (POST) |
| `204 No Content` | Success | 요청은 성공했지만 반환할 콘텐츠가 없습니다. (DELETE) |
| `400 Bad Request` | Fail | 잘못된 요청입니다. (예: JSON 본문 필드 누락, 이미 존재하는 리소스 생성 시도) |
| `404 Not Found` | Fail | 요청한 리소스를 찾을 수 없습니다. (예: 존재하지 않는 사용자/상품 ID 조회) |

## 💡 추가 개선 제안

- **데이터 유효성 검사(Validation)**: `email` 형식 검사, `price`가 숫자인지 등 더 상세한 데이터 유효성 검사 로직을 추가할 수 있습니다.
- **데이터베이스 연동**: 현재는 인메모리 데이터 저장소를 사용하지만, SQLAlchemy와 같은 ORM을 사용하여 SQLite, PostgreSQL 등 실제 데이터베이스와 연동할 수 있습니다.
- **인증/인가**: JWT(JSON Web Token) 등을 도입하여 특정 API는 로그인한 사용자만 호출할 수 있도록 접근 제어 로직을 구현할 수 있습니다.
- **테스트 코드 작성**: `pytest`와 같은 도구를 사용하여 각 API의 동작을 검증하는 단위 테스트 및 통합 테스트 코드를 작성하여 안정성을 높일 수 있습니다.
