import json
from tkinter import messagebox

class Search_class():
    def __init__(self):
        self.web_name = ''
        self.result_arr = []

    def search_data(self):
        self.web_name = self.web_name.lower()
        
        try:
            with open("password.json", mode="r") as data:
                data_file = json.load(data)
                self.result_arr.append(data_file[self.web_name]['email'])
                self.result_arr.append(data_file[self.web_name]['password'])

            return self.result_arr
        except FileNotFoundError:
            print("first make password")   
            messagebox.showinfo('information', 'First Create Passwod')
        except Exception as err:
            print(err)
            messagebox.showinfo('information', 'We dont have information about this site')