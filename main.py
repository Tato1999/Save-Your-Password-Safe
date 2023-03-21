import tkinter
from add import AddPassword
from search import Search_class

FONT_NAME = "Courier"
screen = tkinter.Tk()
screen.title("Password Everywhere")
screen.config(padx=100,pady=50)

def Add():
    global second_page, len_input, add_class, pass_input, web_input,mail_input
    try:
        screen.destroy()
    except:
        print("continue")
   
    add_class = AddPassword()
    second_page = tkinter.Tk()
    second_page.title("Password Everywhere")
    second_page.config(padx=100,pady=50)

    screen_label = tkinter.Label(text="Search or add Password", font=(FONT_NAME,16,"bold"),fg = "#6667ab")
    screen_label.grid(column=0,row=0)

    canvas = tkinter.Canvas(height=200,width=200)
    logo = tkinter.PhotoImage(file="png/logo.png")
    canvas.create_image(100,100,image=logo)
    canvas.grid(column=0,row=1)
    screen_label.config(text="Add Password")

    #input
    web_input = tkinter.Entry(width=16)
    web_input.insert(0, "Enter Site here...")
    web_input.bind("<FocusIn>", clear_placeholder_web)
    web_input.bind("<FocusOut>", add_placeholder_web)
    # web_input.insert(0,"Site Name")
    mail_input = tkinter.Entry(width=16)
    mail_input.insert(0,"Enter Email here...")
    mail_input.bind("<FocusIn>", clear_placeholder_email)
    mail_input.bind("<FocusOut>", add_placeholder_email)
    pass_input = tkinter.Entry(width=16)
    pass_input.insert(0, "Enter password here...")
    pass_input.bind("<FocusIn>", clear_placeholder_pass)
    pass_input.bind("<FocusOut>", add_placeholder_pass)
    len_input = tkinter.Spinbox(from_=8, to=16, width=2)
    #button
    back_button = tkinter.Button(text="Back", width=16, command=first_page)
    add_button = tkinter.Button(text="Add Password", width=16, command=add_attribute)
    # back_button = tkinter.Button(text="back", width=16)
    gen_button = tkinter.Button(text="Gen", command=gen)

    #grid
    web_input.grid(column=0,row=2)
    mail_input.grid(column=0,row=3)
    pass_input.grid(column=0,row=4)
    len_input.grid(column=1,row=4)
    add_button.grid(column=0, row=5)
    gen_button.grid(column=1,row=5)
    back_button.grid(column=0,row=6)


    #placeholder default color
    web_input.config(fg="gray")
    mail_input.config(fg="gray")
    pass_input.config(fg="gray")
    second_page.mainloop()

def gen():
    password = add_class.generate_password(int(len_input.get()))
    pass_input.delete(0, "end")
    pass_input.config(fg="black")
    pass_input.insert(0,password)
    
def clear_placeholder_web(k):
    if web_input.get() == "Enter Site here...":
        web_input.delete(0, "end")
        web_input.config(fg="black")
        print("clear")
def clear_placeholder_email(k):
    if mail_input.get() == "Enter Email here...":
        mail_input.delete(0, "end")
        mail_input.config(fg="black")
        print("clear")
def clear_placeholder_pass(k):
    if pass_input.get() == "Enter password here...":
        pass_input.delete(0, "end")
        pass_input.config(fg="black")
        print("clear")
   

def add_placeholder_web(k):
    if not web_input.get():
        web_input.insert(0, "Enter Site here...")
        web_input.config(fg="gray")
        print("insert")
def add_placeholder_email(k):
    if not mail_input.get():
        mail_input.insert(0, "Enter Email here...")
        mail_input.config(fg="gray")
        print("insert")
def add_placeholder_pass(k):
    if not pass_input.get():
        pass_input.insert(0, "Enter password here...")
        pass_input.config(fg="gray")
        print("insert")


def add_attribute():
    add_class.web_name = web_input.get()
    add_class.mail_name = mail_input.get()
    add_class.pass_name = pass_input.get()

    add_class.add_password_in_json()


def Search():
    global second_page, len_input, add_class, pass_input, web_input, mail_input, search_pass
    search_pass = Search_class()
    
    try:
        screen.destroy()
    except:
        print("continue")
    
    second_page = tkinter.Tk()
    screen_label = tkinter.Label(text="Search or add Password", font=(FONT_NAME,16,"bold"),fg = "#6667ab")
    screen_label.grid(column=0,row=0)

    second_page.title("Password Everywhere")
    second_page.config(padx=100,pady=50)

    canvas = tkinter.Canvas(height=200,width=200)
    logo = tkinter.PhotoImage(file="png/logo.png")
    canvas.create_image(100,100,image=logo)
    canvas.grid(column=0,row=1)
    screen_label.config(text="Search Password")

    #input
    web_input = tkinter.Entry(width=16)
    web_input.insert(0, "Enter Site here...")
    web_input.bind("<FocusIn>", clear_placeholder_web)
    web_input.bind("<FocusOut>", add_placeholder_web)
    # web_input.insert(0,"Site Name")
    mail_input = tkinter.Entry(width=16)
    mail_input.insert(0,"Result: Email...")
    mail_input.bind("<FocusIn>", clear_placeholder_email)
    mail_input.bind("<FocusOut>", add_placeholder_email)
    pass_input = tkinter.Entry(width=16)
    pass_input.insert(0, "Result: password...")
    pass_input.bind("<FocusIn>", clear_placeholder_pass)
    pass_input.bind("<FocusOut>", add_placeholder_pass)

    #button
    back_button = tkinter.Button(text="Back", width=16, command=first_page)

    search = tkinter.Button(text="Search Password", width=16, command=search_attribute)

    #disable
    
    #placeholder default color
    web_input.config(fg="gray")
    mail_input.config(fg="gray")
    pass_input.config(fg="gray")
    #grid
    web_input.grid(column=0,row=2)
    mail_input.grid(column=0,row=3)
    pass_input.grid(column=0,row=4)
    search.grid(column=0,row=5)
    back_button.grid(column=0,row=6)
    second_page.mainloop()

def search_attribute():
    search_pass.web_name = web_input.get()
    mail_input.config(fg="black")
    pass_input.config(fg="black")
    pass_input.delete(0,'end')
    pass_input.insert(0,search_pass.search_data()[1])
    mail_input.delete(0,'end')
    mail_input.insert(0,search_pass.search_data()[0])

def first_page():
    global screen
    try:
        screen.destroy()
    except:
        pass
    try:
        second_page.destroy()
    except:
        print("continue")
    screen = tkinter.Tk()
    screen.title("Password Everywhere")
    screen.config(padx=100,pady=50)
    screen_label = tkinter.Label(text="Search or add Password", font=(FONT_NAME,16,"bold"),fg = "#6667ab")
    screen_label.grid(column=0,row=0)

    canvas = tkinter.Canvas(height=200,width=200)
    logo = tkinter.PhotoImage(file="png/logo.png")
    canvas.create_image(100,100,image=logo)
    canvas.grid(column=0,row=1)

    add_button = tkinter.Button(text="Add Password", width=16, command=Add)
    search = tkinter.Button(text="Search Password", width=16, command=Search)
    search.grid(column=0,row=3)
    add_button.grid(column=0,row=4)

    screen.mainloop()

first_page()




