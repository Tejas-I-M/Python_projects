import json 
import os
import base64

class PasswordManager:
    def __init__(self,file_name="passwords.json"):
        self.file_name  = file_name
        self.data = self.load_data()
    def load_data(self):
        if not os.path.exists(self.file_name):
            return {}
        with open(self.file_name,'r') as f:
            json.load(f)
    def save_data(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data,f,indent=4)
    def encode_password(self,password):
        return base64.b64encode(password.encode()).decode()
    def decode_password(self,encoded_password):
        return base64.b64decode(encoded_password.encode()).decode()
    def add_account(self,service,password):
        encode = self.encode_password(password)
        self.data[service] = encode
        self.save_data()
        print("account added")
    def get_password(self,service):
        if service not in self.data:
            print("no service found")
            return
        decoded  = self.decode_password(self.data[service])
        print(f"the password of {service} is: {decoded}" )
pm =PasswordManager()

while True:
    print("\n1.Add 2.get 3.exit")
    choice =input("choose the option: ")

    if choice == "1":
        service = input("enter the service: ")
        password = input("enter the password: ") 
        pm.add_account(service,password)
    elif choice =="2":
        service = input("enter the serivece: ")
        pm.get_password(service)
    elif choice =="3":
        break
    else:
        print("invalid input")
