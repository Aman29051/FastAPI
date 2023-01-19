import uvicorn
from fastapi import FastAPI
from banknotes import Banknote
import pickle

app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello Aman!'}


@app.get('/{name}')
def get_name(name: str):
    return {'welcome : 'f'{name}'}


@app.post('/predict')
def predict_banknote(data: Banknote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    kurtosis = data['kurtosis']
    entropy = data['entropy']

    prediction = classifier.predict([[variance, skewness, kurtosis, entropy]])

    if prediction[0] > 0.5:
        prediction = "Fake Note"
    else:
        prediction = "Bank Note"

    return {'prediction': prediction}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# RUN : uvicorn app:app --reload
