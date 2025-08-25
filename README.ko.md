# Django 테스트 프로젝트

이것은 기본적인 Django 기능들을 보여주기 위해 만들어진 간단한 Django 프로젝트입니다.

## 기능

*   **게시글 관리:** 게시글 생성, 읽기, 수정, 삭제 기능
*   **메모 관리:** 메모 생성 및 읽기 기능
*   **기본 산술 연산:** 덧셈과 곱셈을 위한 간단한 API 엔드포인트

## 시작하기

이 설명은 개발 및 테스트 목적으로 로컬 컴퓨터에서 프로젝트를 복사하고 실행하는 방법을 안내합니다.

### 사전 요구 사항

*   Python 3.x
*   Django 4.x

### 설치

1.  레포지토리 복제
    ```sh
    git clone https://github.com/your_username/django_test.git
    ```
2.  의존성 설치 (pip가 설치되어 있다고 가정)
    ```sh
    pip install Django
    ```
3.  마이그레이션 적용
    ```sh
    python manage.py migrate
    ```
4.  개발 서버 실행
    ```sh
    python manage.py runserver
    ```

## 사용법

애플리케이션은 `http://127.0.0.1:8000/`에서 사용할 수 있습니다.

## 프로젝트 구조

```
.
├── config/             # Django 프로젝트 설정
├── polls/              # Django 앱
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py           # Django의 커맨드 라인 유틸리티
└── README.md
```

## API 엔드포인트

*   `/`: 게시글 목록을 표시합니다.
*   `/hello/`: "Hello, world!" 메시지를 반환합니다.
*   `/lion/<str:name>/`: 제공된 이름으로 사용자에게 인사합니다.
*   `/good/`: "Good!" 메시지를 반환합니다.
*   `/moon/`: "Moon!" 메시지를 반환합니다.
*   `/add/<int:num1>/<int:num2>/`: 두 숫자의 합을 반환합니다.
*   `/multiply/<int:num1>/<int:num2>/`: 두 숫자의 곱을 반환합니다.
*   `/memo/`: 메모 목록을 표시합니다.
*   `/memo/<int:memo_id>`: 단일 메모를 표시합니다.
