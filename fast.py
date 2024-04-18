import os
from fastapi import FastAPI
from pydantic import BaseModel
from paystack import Payment
import secret
from dotenv import load_dotenv

load_dotenv()
sk = os.environ.get("secret")

class User(BaseModel):
    email : str
    cash : float
    key : str
    
app = FastAPI()

@app.post("/user/")
async def get_user_info(user_input: User):
     email = user_input.email
     cash = user_input.cash
     app = Payment(secret.secret, email, cash)
     return {"message":app.pay()}