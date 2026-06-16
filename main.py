import json
import random
import string
from pathlib import Path


class bank:
    database='data.json'
    data=[]
    try:

        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")


    @classmethod
    def __update(cls):
        with open(bank.database,'w') as fs:
            fs.write(json.dumps(bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spche=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spche
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info={
            "name":input("tell your name: "),
            "age":int(input("tell your age: ")),
            "email": input("tell your email: "),
            "pin":int(input("tell your pin: ")),
            "accountNo.":bank. __accountgenerate(),
            "balance":0
        }
        if info['age']<18  or len(str(info['pin']))!=4:
            print("you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            bank.data.append(info)

            bank.__update()

    def depositmoney(self):
        accountNumber=input("enter your acc. no: ")
        pin=int(input("enter pin: "))

        userdata=[i for i in bank.data if i['accountNo.']==accountNumber and i['pin']==pin]

        if not userdata:
            print("sorry no data found")
        else:
            amount=int(input("how much you want to deposit: "))
            if amount > 100000 or amount<0:
                print("amount is high deposit below 10000")
            else:

                userdata [0]['balance']+=amount
                bank.__update()
                print("ammount added successfully")


    def withdrawmoney(self):
        accountNumber=input("enter your acc. no: ")
        pin=int(input("enter pin: "))

        userdata=[i for i in bank.data if i['accountNo.']==accountNumber and i['pin']==pin]

        if not userdata:
            print("sorry no data found")
        else:
            amount=int(input("how much you want to withdraw: "))
            if userdata [0]['balance'] < amount:
                print("don't have that much money")

            else:

                userdata [0]['balance']-=amount
                bank.__update()
                print("ammount withdrawn successfully")


    def showdetails(self):
        accountNumber=input("enter your acc. no: ")
        pin=int(input("enter pin: "))

        userdata=[i for i in bank.data if i['accountNo.']==accountNumber and i['pin']==pin]

        print("___your informations are___\n\n")
        for i in userdata [0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accountNumber=input("enter your acc. no: ")
        pin=int(input("enter pin: "))

        userdata=[i for i in bank.data if i['accountNo.']==accountNumber and i['pin']==pin]

        if not userdata:
            print("user not found")
        else:
            print("you cannot change the age,account number,balance")

            print("Fill the details for change or leave it empty if no change")
            newdata={
                "name":input("enter new name or press enter to skip: \n"),
                "email":input("enter your new email or press enter to skip: \n"),
                "pin":input("enter your new pin or press enter to skip: ")
                      }

            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']

            newdata['age']=userdata[0]['age']

            newdata['accountNo.']=userdata[0]['accountNo.']
            newdata['balance']=userdata[0]['balance']

          
                
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            bank.__update()
            print("details updated successfully")

    def deletedetails(self):
        accountNumber=input("enter your acc. no: ")
        pin=int(input("enter pin: "))

        userdata=[i for i in bank.data if i['accountNo.']==accountNumber and i['pin']==pin]

        if userdata==False:
            print("no such data exist")
        else:
            check = input("enter y to delete or n to don't delete: ")
            if check=='n' or check =='N':
                print("pass")
            else:
                index=bank.data.index(userdata[0])
                bank.data.pop(index)
                print("account deleted")
                bank.__update()

user=bank()
print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details of account")
print("press 5 for updating details")
print("press 6 for deleting your account")

check=int(input("tell your response: "))

if check == 1:
    user.createaccount()
    
if check==2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()

if check==4:
    user.showdetails()

if check==5:
    user.updatedetails()

if check==6:
    user.deletedetails()