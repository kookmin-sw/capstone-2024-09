import joblib
from konlpy.tag import Okt

mlp_model = joblib.load('./mlp_model.joblib')
okt = Okt()

conversation_X = []
sentence = "저는 축구 선수가 되고 싶습니다. 어떻게 하면 되는지 알려주세요."

conversation_X.append(" ".join(okt.nouns(sentence)))

vectorizer = joblib.load('tfidfvectorizer.joblib')
X_tfidf = vectorizer.transform(conversation_X).toarray()

predictions = mlp_model.predict(X_tfidf)
