from tkinter import *
root=Tk()
root.geometry("500x500")
label_user=Label(root,text="User Name : ")
label_user.place(relx=0.3,rely=0.2,anchor=CENTER)
Entry_Name=Entry()
Entry_Name.place(relx=0.6,rely=0.2,anchor=CENTER)
label_email=Label(root,text="Email Id : ")
label_email.place(relx=0.3,rely=0.3,anchor=CENTER)
Entry_email=Entry()
Entry_email.place(relx=0.6,rely=0.3,anchor=CENTER)
label_all=Label(root)
label_all.place(relx=0.5,rely=0.6,anchor=CENTER)
database={}
class Parent():
    def __init__(self):
        print("Hello")
    def addUser(user,email):
        database[user]=email
        label_all["text"]=database
class User(Parent):
    def __init__(self,user_id,email_id):
        self.user=user_id
        self.email=email_id
    def add(self):
        print("work")
        Parent.addUser(self.user,self.email)
def do():
    obj=User(Entry_Name.get(),Entry_email.get())
    obj.add()
btn=Button(root,text="Add user detail",command=do)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()