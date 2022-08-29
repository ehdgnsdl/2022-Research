# 2022-AI-Term-project
 2022-AI-Term-project

## Subject
* SuperResolution을 적용한 자동차 번호판 추정 향상

## Overview
* Object detection에서 SuperResolution의 필요성 <br>
* 자동차의 번호판은 차량을 식별할 수 있는 중요 정보를 담고 있다. 블랙박스 카메라의 화질
이나 기상 상황, 도로 상황 등에 따라서 Object detection이 안되거나 잘못된 위치를 찾는 일이
발생한다. Super Resolution을 통해서 Pre-processing 이후, Object Detection을 진행 시 더 높은
인식률과 정확도를 기대해볼 수 있다. <br>

## Try
- Blur처리된 이미지와 기본 이미지, SuperResolution을 적용한 이미지 각각에 자동차 번호판을 Object Detection 했을 때의 Loss 값과 Accuracy 값을 비교.<br>
- 또한, 하이퍼파라미터 수정 및 가중치 초기화, Dropout 같은 여러가지 기법을 사용하여 성능 비교. <br>

## Experiments and results
#### Base Code 
- 데이터: Kaggle ‘Car License Plate Detection’
- VGG16을 이용한 자동차 번호판 Detection

#### Model
- VGG16 Model

#### Summary
- Blur처리된 이미지, 기본 이미지, SuperResolution(BSRGAN)을 적용한 이미지 순서대로 성능이 점차 좋아지는 것을 확인.
- 가중치 초기화 및 Batch Size, Epoch, EarlyStopping 등의 기법과 하이퍼파라미터을 수정했을 때 성능 향상을 확인.

#### A case of trying but bad results
1. Optimizer 수정 (RMSProp, RAdam, NAdam, SGD 등)
2. Loss Function 수정
3. Dropout, Batch Normalized 기법 적용
4. 모델 수정 (Layer 층 추가, activation function 수정 등)

