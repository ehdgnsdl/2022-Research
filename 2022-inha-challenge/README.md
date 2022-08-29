## 주제
- 시공간 데이터 예측 (Spatio-Temporal Data Prediction)

## Background

- **시공간 데이터**는 교통, 물류, 에너지 등 다양한 산업분야에서 광범위하게 발생하게 있으며, **미래에 발생할 데이터를 미리 예측**하는 것은 **경제/산업적 측면에서의 활용가치**가 매우 높음
- 인하대학교 인공지능융합연구센터에서는 본 챌린지를 통해 **풍력 발전소**의 전기 에너지 발생량에 대한 데이터를 분석하여 **미래에 기대되는 에너지 발생량을 높은 정확도로 예측**하는 인공지능 모델 개발을 목표로 함
- 해당 모델은 에너지 분야 뿐만 아니라 **교통 및 물류 분야의 다양한 시공간 데이터에 적용**할 수 있을 것으로 기대됨

## Summary

(1). Data Description

- 134개 터빈의 2일 동안의 Patv(유효전력) 값을 예측

[데이터 설명](https://dacon.io/competitions/official/235926/talkboard/406431?page=1&dtype=recent)

**2022 인하인공지능 챌린지 예선**

[2022 인하 인공지능 챌린지](https://dacon.io/competitions/official/235926/overview/description)

**2022 인하인공지능 챌린지 본 대회**

[2022 인하 인공지능 챌린지](https://dacon.io/competitions/official/235952/overview/rules)

(2). Data Preprocessing

- 바로 Patv를 예측하는데 어려움 및 한계가 보여서 Regression model을 사용하기 위해서 풍속을 예측한 후에 Patv를 예측하기로 함.
- 풍속이 Patv와 상관 관계가 높았고, 이 전 Tmstamp과 연관성이 높아보였음.

  (2) - 1. 풍속 예측

- 데이터 전처리
    - 결측치 처리. interpolate 사용 (hour=0인 데이터로 모든 Day를 봤을 때, 풍속이 이어지게끔 처리)
    - Blocking Time Series Split 사용
- Model & Algorithms
    - LSTM
    - Autoformer
- 터빈 선택
    - 대표성을 띄는 풍속을 선정하여 Patv 예측
    - 지역성 및 중앙값, 평균 값, 분위수 값을 기준으로 선택

  (2) - 2. Patv 예측

- 데이터 전처리
    - 풍속 예측과 동일.
- Feature Engineering
    - 시간 변수 추가
    - 터빈별 공간적 상관관계
    - 터빈 별 풍속 통계량
    - Day별 풍속 통계량
- Model & Algorithms
    - LightGBM Regression (LGBM Regression)

(3). Report

- 평가 지표: RMSE + MAE의 평균
- 모델 예측에 영향을 주는 Feature importance 확인

(4). Review

- 처음엔 LSTM, GRU 등 model들로 바로 Patv 예측 시도.
    - But, 더 이상 모델 개선이 이루어지지 않는 어려움 및 한계를 느낌.
- Regression 모델을 사용하기로 생각.
    - Regression 모델을 사용하기 위해서 Patv와 상관 관계가 높은 풍속(Wspd)을 예측하기로함.
    - 확인한 결과, 풍속 예측 후 Regression 모델로 Patv를 예측했을 시, 성능이 더 좋은 것을 확인.
    - 이 후, 피쳐 엔지니어링 및 변수 추가를 통해서 성능 향상
    
