# 서울 데이터 업로더 README

## 개요

이 저장소에는 서울시 데이터를 Elasticsearch 인덱스에 업로드하기 위한 Python 스크립트가 포함되어 있습니다. 두 가지 주요 기능이 구현되어 있습니다.

1. **버스 탑승객 데이터 업로드:** 서울시 API에서 버스 탑승객 데이터를 가져와 처리한 후 Elasticsearch 인덱스에 업로드합니다.
2. **인구 데이터 업로드:** 서울시 API에서 인구 데이터를 가져와 처리한 후 다른 Elasticsearch 인덱스에 업로드합니다.

## 요구 사항

- Python 3.x
- Elasticsearch
- 필수 Python 패키지 (`elasticsearch`, `requests`, `datetime`, `dateutil.relativedelta`)

## 설정

1. 필요한 Python 패키지를 설치하세요.

    ```bash
    pip install elasticsearch requests
    ```

2. 실행 중인 Elasticsearch 인스턴스가 있으며 필요한 자격 증명이 설정되어 있는지 확인하세요.

3. 두 스크립트에서 `CLOUD_ID` 및 `ELASTIC_PASSWORD` 변수를 Elasticsearch 클라우드 ID 및 비밀번호로 조정하세요.

## 버스 탑승객 데이터 업로드

### 스크립트 실행

1. `bus_passenger_upload.py` 스크립트를 실행하세요.

    ```bash
    python bus_passenger_upload.py
    ```

2. 스크립트는 서울시 API에서 버스 탑승객 데이터를 가져와 "buspassenger"라는 Elasticsearch 인덱스에 업로드합니다.

## 인구 데이터 업로드

### 스크립트 실행

1. `population_data_upload.py` 스크립트를 실행하세요.

    ```bash
    python population_data_upload.py
    ```

2. 스크립트는 서울시 API에서 인구 데이터를 가져와 "seoullifepopluation1"이라는 Elasticsearch 인덱스에 업로드합니다.

## 데이터 재색인

초기 인덱스에 데이터를 업로드한 후 추가 인덱스를 만들기 위해 재색인 작업이 수행됩니다.

### 재색인 실행

1. `reindex_data.py` 스크립트를 실행하세요.

    ```bash
    python reindex_data.py
    ```

2. 스크립트는 Elasticsearch 인덱스에 재색인 작업을 수행합니다.

## 추가 정보

- 두 스크립트 모두 데이터를 매 시간마다 업데이트하도록 설계되었습니다.
- API 및 데이터 소스가 사용 가능하고 올바르게 구성되어 있는지 확인하세요.
