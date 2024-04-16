## 0. 개요
분류형 ai는 챗봇과 이용자(학생)간의 대화 내용을 받아 그 대화 내용을 토대로 이용자에게 적합한 직업을 직업 번호(0~42)로 반환하는 역할을 한다. 

반환된 직업 번호에 따라 백엔드에서는, 커리어넷 또는 워크넷의 api를 이용해 해당 직업에 대한 구체적인 상세 정보를 가져와 챗봇에 넘겨주는 동작을 하게 된다.


## 1. preprocessing_data_for_recommending_ai.ipynb에 대한 소개

### 1) 모델 별 성능 평가
- 이 파일에서는 분류형 ai로 머신러닝(1,2,3,4) 및 딥러닝 모델(5,6,7)들을 구축하여 성능을 평가하였다. 구축한 모델들은 아래와 같다.
  
##### (1) 다중 클래스 나이브 베이즈 (Multinomial Naive Bayes)

##### (2) 다중 클래스 로지스틱 회귀 (Multinomial Logistic Regression)

##### (3) 다중 클래스 서포트 벡터 머신 (Multiclass SVM)

##### (4) 랜덤 포레스트 분류기 (Random Forest Classifier)

##### (5) 다층 퍼셉트론 (Multilayer Perceptron (MLP))

##### (6) CNN(Convolution Neural Network)

##### (7) Transformer


### 2) 성능 평가 결과
![분류형 ai 모델 성능 비교](https://github.com/kookmin-sw/capstone-2024-09/assets/29187870/9bf6310e-1cb5-46aa-aadd-6738ba1c73e2)
- 다층 퍼셉트론의 정확도가 약 69%로, 가장 높게 나왔다. 따라서 분류형 ai 모델로 다층 퍼셉트론 모델을 채택하기로 하였다.

### 3) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/1-dhdeV4x4o7kpVwRuo6MoHCHoM4Ry_S1?usp=sharing



## 2. choosing_best_parameter_values(in MLP).ipynb에 대한 소개

### 1) 하이퍼 파라미터 별 성능 평가
- 이 파일에서는 공식 분류형 ai 모델로 채택된 다층 퍼셉트론 모델의 분류 성능을 높이고자 다층 퍼셉트론 모델의 하이퍼 파라미터 값을 바꿔가며 성능을 테스트해보았다.

### 2) 성능 평가 결과
![mlp성능비교시각화](https://github.com/kookmin-sw/capstone-2024-09/assets/29187870/5144cfe9-5311-4498-bf3b-81cf1bd24789)
- 테스트 결과, 다층 퍼셉트론의 hidden layer를 쌓을 수록 예측 성능이 떨어지는 것을 확인할 수 있었다.(반환해야 할 직업 번호를 반환하지 못함)
- 가장 예측 성능이 높은 하이퍼 파라미터 조합은 hidden layer를 1개만 쌓고 그 층의 노드 수는 100개로, 활성화 함수는 'relu'를,
  early_stopping 옵션(학습 중 검증용 데이터에 대한 성능이 떨어지는 것을 확인하면 학습을 조기 중단하는 기능)을 켜주는 것이었다.
  이는 scikit-learn에서 불러온 다층 퍼셉트론 모델의 default 하이퍼 파라미터 값의 조합이었는데, 이 조합이 약 69.4%로 가장 높은 예측 성능을 보여주었다.

### 3) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/1kzWfUBhKGQ-CtXYfLkL6tbSfrErkQurf?usp=sharing



## 3. build_and_save_recommending_ai.ipynb에 대한 소개

### 1) 다층 퍼셉트론 모델 구축 후 로컬에 저장
- 다층 퍼셉트론은 transformer 모델이 아니기 때문에 허깅페이스에 업로드해 그 api를 이용할 수는 없었다.
  모델 자체가 17.2mb로 비교적 가볍기 때문에, 서버에 모델을 탑재하여 필요할 때 서버 내에서 불러와서 쓰는 방식을 이용하기로 하였다.
  따라서 모델을 서버에 저장할 수 있게 joblib 타입의 파일로 저장하였고, 이를 별도로 서버로 옮기는 작업을 하였다.
 
### 2) 작업한 주피터 노트북 파일의 원본 링크
- https://colab.research.google.com/drive/13et3P_uYkmwEZY-iTX7vqK82KeHVPM2V?usp=sharing



## 4. 분류형 ai의 사용법
```python
import joblib

# 저장된 모델 불러오기
mlp_model = joblib.load('mlp_model.joblib')

# 파이썬 한국어 처리 패키지 설치
!pip install konlpy

# 문장들을 단어로 쪼갤 형태소 분석 라이브러리 불러오기
from konlpy.tag import Okt
okt = Okt()

# 상담에서 등장한 문장(conversation_X)을 명사 단위로 쪼갠 문자열로 변환해 저장할 리스트 생성
conversation_X = []

# 챗봇과 이용자(학생)간의 대화 내용인 data 변수 내의 문장을 sentence 변수에 저장하는 작업
sentence = data

# sentence 변수에 저장된 문장을 단어로 쪼개서 단어 별로 띄어쓰기해서 저장(나중에 문서 벡터를 만들때 띄어쓰기 단위로 벡터의 요소를 형성하기 때문에)
conversation_X.append(" ".join(okt.nouns(sentence)))


from sklearn.feature_extraction.text import TfidfVectorizer # 문장을 문서벡터로 변환시켜줄 TfidfVectorizer 라이브러리 불러오기
import numpy as np  # 데이터를 array로 변환시키기 위해 numpy 라이브러리 불러오기


# 학생과 상담사 간의 대화들을 문서벡터로 변환하기 위해 TF-IDF 벡터화를 수행
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(conversation_X).toarray()



# 모델에 문서벡터 넘겨주고 추천 직업 번호 반환받기
# 반환되는 값 : 0~42 (=integer 타입의 값)
predictions = mlp_model.predict(X_tfidf)


# 이후 predictions에 저장된 추천 직업 번호에 따라 db에 접근해서 해당 직업 정보를 가져오면 됨.
