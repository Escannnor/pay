import os
import requests
from dotenv import load_dotenv

load_dotenv()



class Paystack:
    def __init__(self, email, amount, key):
        self.key = key
        self.email = email
        self.amount = amount * 100

    def pay(self):
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount
        }

        headers = {
            "Authorization": "Bearer " + self.key,
            "Content-Type": "aplication/json"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            ref = data['data']['reference']
            auth_link = data['data']['authorization_url']
            result = {
                'reference_id': ref,
                'auth_url': auth_link
                }
            return result
        
class Verify:
     def __init__(self, reference, secret_key):
        self.reference = reference
        self.secret_key = secret_key
        
     def status(self):
        url = f"/transaction/verify/{self.reference}"
        headers = {
            "Authorization": "Bearer " + self.secret_key
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status == 200:
            data = response.json()
            gateway_response = data['gateway_response']
            if gateway_response == "Successful":
                return "successful"
            elif gateway_response == "The transaction was not completed":
                return "pending"
            else:
                return "failed"
        else:
            return "failed"
        
def main():
    while True:
        email = input("Enter your email: ")
        amount = float(input("Enter your amount: "))
        paystack = Paystack(email, amount, os.eniron.get("secret"))
        result = paystack.pay()
        print("Payment initialized. Please complete the payment by visiting the following link: ")
        print(result['auth_url'])
        reference_id = result['reference_id']
        print('Payment reference ID: ', reference_id)
        
        verify = Verify(reference_id, os.environ.get('secret'))
        status = verify.status()
        print('Payment status:', status)
        
        again = input("Do you want to amke another transaction? (yes/no): ")
        if again.lower() != 'yes':
            break
        
if __name__ =='__main__':
    main()