import string as st
import random
import json
class AddPassword():
    def __init__(self):
        self.alph = st.ascii_letters + st.digits + st.punctuation
        self.generated_password = ''
        self.web_name = ''
        self.mail_name = ''
        self.pass_name = ''

    
    def generate_password(self,k):
        self.generated_password = ''
        for i in range(int(k)):
            self.generated_password += random.choice(self.alph)
        print(self.generated_password)
        return self.generated_password
    
    def add_password_in_json(self):
        new_data = {
            self.web_name.lower(): {
                "email": self.mail_name.lower(),
                "password": self.pass_name.lower()
            }
        }
        try:
            with open('password.json', mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        
            with open('password.json', mode="w") as write_file:
                json.dump(data, write_file, indent=4)
        except FileNotFoundError:
            with open('password.json', mode="w") as write_file:
                json.dump(new_data, write_file, indent=4)
    
    

