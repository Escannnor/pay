import requests

class Payment:
    def __init__(self,key,email,amount):
        self.key = key
        self.email = email
        self.amount = amount
        
    def pay(self):
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            'email': self.email,
            'amount' : self.amount * 100
        }
        
        headers = {
            "Authorization": 'Bearer' + self.key,
            "Content-Type" : 'application/json'
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            # print('Done')
            # print(data)
            return data
        else:
            print('Error:', response.status_code)
            
secret = "sk_test_d25e54d744a1c43e905544afd02569ce7ccb2403"
email = 'sawdickagboke@gmail.com'
cash = 500000
apple = Payment(secret ,email, cash)
print(apple.pay())