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
    
app = FastAPI()

@app.post("/user/")
def get_user_info(user_input: User):
     email = user_input.email
     cash = user_input.cash
     app = Payment(sk, email, cash)
     data = app.pay()
     return data