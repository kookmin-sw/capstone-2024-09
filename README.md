분류형 ai는 챗봇과 이용자(학생)간의 대화 내용을 받아 그 대화 내용을 토대로 이용자에게 적합한 직업을 직업 번호(0~42)로 반환하는 역할을 한다. 

반환된 직업 번호에 따라 백엔드에서는, 커리어넷 또는 워크넷의 api를 이용해 해당 직업에 대한 구체적인 상세 정보를 가져와 챗봇에 넘겨주는 동작을 하게 된다.


## 1. preprocessing_data_for_recommending_ai.ipynb에 대한 소개

### 1) 모델 별 성능 평가
- 이 파일에서는 분류형 ai로 머신러닝(1,2,3,4) 및 딥러닝 모델(5,6,7)들을 구축하여 성능을 평가하였다. 구축한 모델들은 아래와 같다.
  
#### (1) 다중 클래스 나이브 베이즈 (Multinomial Naive Bayes)

#### (2) 다중 클래스 로지스틱 회귀 (Multinomial Logistic Regression)

#### (3) 다중 클래스 서포트 벡터 머신 (Multiclass SVM)

#### (4) 랜덤 포레스트 분류기 (Random Forest Classifier)

#### (5) 다층 퍼셉트론 (Multilayer Perceptron (MLP))

#### (6) CNN(Convolution Neural Network)

#### (7) Transformer


### 2) 성능 평가 결과
<img src="/home/yeong/다운로드/분류형 ai 모델 성능 비교.png" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="<img src="분류형 ai 모델 성능 비교.png" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>"></img><br/>
- 다층 퍼셉트론의 정확도가 약 69%로, 가장 높게 나왔다. 따라서 분류형 ai 모델로 다층 퍼셉트론 모델을 채택하기로 하였다.

### 3) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/1-dhdeV4x4o7kpVwRuo6MoHCHoM4Ry_S1?usp=sharing



## 2. choosing_best_parameter_values(in MLP).ipynb에 대한 소개

### 1) 하이퍼 파라미터 별 성능 평가
- 이 파일에서는 공식 분류형 ai 모델로 채택된 다층 퍼셉트론 모델의 분류 성능을 높이고자 다층 퍼셉트론 모델의 하이퍼 파라미터 값을 바꿔가며 성능을 테스트해보았다.

### 2) 성능 평가 결과
<img src="/home/yeong/다운로드/mlp성능비교시각화.png" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="<img src="분류형 ai 모델 성능 비교.png" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="mlp성능비교시각화"></img><br/>"></img><br/>
- 테스트 결과, 다층 퍼셉트론의 hidden layer를 쌓을 수록 예측 성능이 떨어지는 것을 확인할 수 있었다. (반환해야 할 직업 번호를 반환하지 못함).
- 가장 예측 성능이 높은 하이퍼 파라미터 조합은 hidden layer를 1개만 쌓고 그 층의 노드 수는 100개로, 활성화 함수는 'relu'를,
  학습 중 검증용 데이터에 대한 성능이 떨어지는 것을 확인하면 조기에 학습을 중단하는 early_stopping 옵션을 켜주는 것이었다.
  이는 scikit-learn에서 불러온 다층 퍼셉트론 모델의 default 하이퍼 파라미터 값의 조합이었는데, 이 조합이 약 69%로 가장 높은 예측 성능을 보여주었다.

### 3) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/1kzWfUBhKGQ-CtXYfLkL6tbSfrErkQurf?usp=sharing



## 3. build_and_save_recommending_ai.ipynb에 대한 소개

### 1) 다층 퍼셉트론 모델 구축 후 로컬에 저장
- 다층 퍼셉트론은 transformer 모델이 아니기 때문에 허깅페이스에 업로드해 그 api를 이용할 수는 없었다.
  모델 자체가 17.2mb로 비교적 가볍기 때문에, 서버에 모델을 탑재하여 필요할 때 서버 내에서 불러와서 쓰는 방식을 이용하기로 하였다.
  따라서 모델을 서버에 저장할 수 있게 joblib 타입의 파일로 저장하였고, 이를 별도로 서버로 옮기는 작업을 하였다.
 
### 2) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/13et3P_uYkmwEZY-iTX7vqK82KeHVPM2V?usp=sharing
