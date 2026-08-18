from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title='Data Validation API')

class DataPayModel(BaseModel):
    record_id : int
    metric_value : float

@app.get("/")
def health_check():
    return {"status" : "healthy", "environment":"production"}

@app.post("/validate")
def validate_data(payload: DataPayModel):
    if payload.metric_value < 0:
        raise HTTPException(status_code=400,detail='Metric cannot be negative')
    return{"record_id":payload.record_id,"status":"VALID"}