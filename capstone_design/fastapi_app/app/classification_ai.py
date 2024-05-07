import joblib
from konlpy.tag import Okt

mlp_model = joblib.load('/Final_Project/capstone_design/fastapi_app/app/mlp_model.joblib')
vectorizer = joblib.load('/Final_Project/capstone_design/fastapi_app/app/tfidfvectorizer.joblib')
okt = Okt()

def predict(sentence):
    conversation_X = []
    conversation_X.append(" ".join(okt.nouns(sentence)))
    # X_tfidf = vectorizer.transform(conversation_X).toarray()

    # predictions = mlp_model.predict(X_tfidf)
    # return predictions
    return 0