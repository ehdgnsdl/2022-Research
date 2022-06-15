# Project - 자궁내막암(endometrium)

- 주제

자궁 내막암 위험이 낮은 여성의 수술 전 근점침입 및 등급 평가에 따른 최종 병리 예측

- Background

암수술을 받지 않고 호르몬 치료를 받기 위한 수술 전 데이터로 수술 후 결과에 해당하는 Group A, B, C, D가 동일해야함.

- Summary
    
    (1). Data Collection
    - 자궁내막암 환자 데이터 (252명. 자궁조직내막검사 + MRI)
    
    (2). Data Preprocessing
    - EDA (Grade, Stage의 분포도 및 변수와의 관계 확인)
    - Heatmap
    - Normalize (CA125, Tumor Size)
    - Grade에 대한 수치형, 범주형 countplot
    
    (3). Model & Algorithms
    - 평가 지표: F1 score의 macro average
    - XGBoost classifier (방식: Random Search)
    - XGBoost Hyperparameter tuning
    - Data Imbalance 문제 해결 위해 → Random Oversampling 및 Class weight(pos_weight) 사용
    
    (4). Report
    - Feature Importance 및 SHAP Importance 이용
       - 모델 예측에 영향을 주는 Feature Importance 확인.
    
    (5). Review
    - 우선 label data에서의 Stage Column은 Ia에 너무 편향되어 있는 문제가 존재.
       → Ib에 대한 데이터가 추가적으로 요구됨.
    - Stage 및 Grade를 Group 4개를 나누는 것보다 이 4개의 그룹을 1개로 묶는 것이 더 좋다고 생각함.
       → 수술 전 후 Stage 및 Grade의 일치도가 낮기 때문.
    : 문제와 목표를 재 설정 및 추가 데이터가 필요.
