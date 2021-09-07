import pymongo
import random
from bson.objectid import ObjectId
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=client["bankserver"]
mydoc=mydb.citybank
Id =''
print("Welcome to Citybank services")

def printtt(customer):
    print('ID: -',customer['customer_id'])
    print('Name:- ',customer['customer_name'])
    print('contactno.:- ',customer['mobilenumber'])
    print('accountno.:- ', customer['accountnumber'])
    print('ifsc:- ', customer['ifsccode'])
    print('address:- ', customer['address'])
    print('password:- ', customer['password'])



def type_of_account():
    
    while(True):
        print("A-LogIn\nB-SignUp\nX-Exit")
        c=input("Enter your selection : ")
        if c=="A":
            Exsisting_user()
        elif c=="B":
            New_user()
        else:
            print("Invalid Selection")
            E=input("If wanna try again!! Give enter G")
            if E=="G":
                type_of_account()
            else:
                break
''' Here using type_of_account(),
we will choose whether to 
1.create account or 2. loginto account.'''


def update_accountdetails():
    for up in mydoc.find({"customer_id":Id}):       
        print("THe updating services are : \n1.To update your name\n2.To update your contactno.\n3.To update ypur address : \n4.To update your password")
        updateservices=int(input("Enter the update service : "))
        if updateservices==1:
            updated_name = input('Enter the new name:- ')
            mydoc.update_one({'customer_id':Id},{'$set':{'customer_name':updated_name}})
        elif updateservices==2:
            updated_number = int(input("Enter your new contactno."))
            mydoc.update_one({'customer_id':Id},{'$set':{'mobilenumber':updated_number}})   
        elif updateservices==3:
            updated_address=input("Enter your new address : ")
            mydoc.update_one({'customer_id':Id},{'$set':{'address':updated_address}})
        elif updateservices==4:
            updated_password=input("Enter your new password")
            mydoc.update_one({'customer_id':Id},{'$set':{'password':updated_password}})
        else:
            print("Enter valid update service ")     
    input()

    
def Exsisting_user():
    global Id
    Id=int(input("Enter your customer_id : "))
    pwd=input("enter your password : ")
    for y in mydoc.find({"customer_id":Id,"password":pwd}):
        if Id == y['customer_id'] and pwd == y['password']:
            print("suucessfully loggedin!")
            a=random.randint(1111,9999)
            print("your otp for tansaction 43445456 is : ",a)
            T=int(input("Enter your otp : "))
            while (a!=T):
                print("otp not validated")
                b=eval(input("enter otp again : "))
            print("\n otp validataed successfully")
            services()

        else:
            print("enter correct customer_id and password")
            Exsisting_user()
'''Here Exsisting_user() defines that 
if you are already a customer in bank u need to
give your customerid,password,
and the otp received ,,so you can get logged in.  '''





def services():
    print("The services we provide are : \n1.To get account number\n2.To get Ifsccode\n3.To get your address\n4.To delete your account\n5.To update your account")
    services=int(input("Enter the service you need : "))
    if (services==1):
        for ac in mydoc.find({"customer_id":Id},{"accountnumber":1,"_id":0}):
            print("Your account number is : ",ac)
    elif(services==2):
        for ic in mydoc.find({"customer_id":Id},{"ifsccode":1}):
            print("Your Ifsccode is : ",ic)
    elif(services==3):
        for ad in mydoc.find({"customer_id":Id},{"address":1}):
            print("Your address is : ",ad)
    elif(services==4):
        h=random.randint(1111,9999)
        print("your otp for tansaction 43445456 is : ",a)
        k=int(input("enter your otp : "))
        if h==b:
            myquery={"customer_id":Id}
            mydoc.delete_one(myquery)
    elif(services==5):
        update_accountdetails()





def New_user():
    print("1.To create a new account\n2.To know the services of bank.")
    v=int(input("Enter your selection : "))
    if v==1:
        new_id=random.randint(1111,9999)
        print("Your customer id is : ",new_id)
        name=input("Enter your name : ")
        contactno=int(input("Enter your mobilenumber : "))
        accountno=random.randint(11111111111111,99999999999999)
        print("Your account number is",accountno)
        code=random.randint(1111,9999)
        ifsc_code=("andb",code)
        street=input("Enter your street name : ")
        city=input("Enter your city name : ")
        state=input("Enter your state name : ")
        address=(street,",",city,",",state)
        password=input("choose your password")
        Document={
            "customer_id":new_id,
            "customer_name":name,
            "mobilenumber":contactno,
            "accountnumber":accountno,
            "ifsccode":ifsc_code,
            "address":address,
            "password":password
            }
        mydoc.insert_one(Document)
        print("Account created succesfully\n welcome to city bank services")
    elif v==2:
        print("The bank services we provide are : \n 1.Creation of bank account\n2.To get the all the bank details\n3.To update the details\n4.To delete the account")
    input()
    type_of_account()



type_of_account()