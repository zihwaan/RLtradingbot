from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from processors.data_processor import process_data
from config.settings import settings

app = FastAPI(title="Data Processor Service")

class DataInput(BaseModel):
    code: str
    date_from: str
    date_to: str
    ver: str = 'v4'

@app.post("/process")
async def process_data_api(input_data: DataInput):
    try:
        chart_data, training_data = process_data(input_data.code, input_data.date_from, input_data.date_to, input_data.ver)
        return {
            "chart_data": chart_data.to_dict(orient='records'),
            "training_data": training_data.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.DATA_PROCESSOR_PORT)