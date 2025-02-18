##Imports
from fastapi import FastAPI, Request
import uvicorn
from data.fetch_data import fetchData
from data.return_data import returnData
from helper.encode_data import encodeData
from helper.encode_input import encodeInput
from model.predict import prediction
from model.model_struct import CompatibilityNN

##Initial
app = FastAPI()

##Routes

##Test route
@app.get('/') 
def home_route():
    return {"msg":"This route works!"}

##Model route
@app.post('/model')
async def model_route(request: Request):
      ip_json = await request.json()
      ip = encodeInput(ip_json)
      df = fetchData()
      X =  encodeData(df)
      indexes = prediction(ip, X)
      df2 = fetchData()
      op = returnData(df2, indexes)
      return op

##Uvi Server
if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=4000)
