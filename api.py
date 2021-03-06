from fastapi import FastAPI
import joblib
import ast
import uvicorn

app = FastAPI()


model = joblib.load(open("model.pkl", "rb"))

@app.get("/")
def root():
   return {"message": "Scoring prediction"}

@app.get("/predict/")
def predict(data):
    data = data.replace("(","[[")
    data =data.replace(")","]]")
    data = ast.literal_eval(data)
    prediction = model.predict(data)
    proba = model.predict_proba(data)
    return {
       'prediction': prediction[0],
        'proba' : proba
   }


if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)

