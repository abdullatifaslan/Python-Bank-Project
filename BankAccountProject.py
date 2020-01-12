import os


class Account():

    def __init__(self,name,balance,acc_num,acc_type):
        self.name=name
        self.acc_num=acc_num
        self.balance=balance
        self.acc_type=acc_type

    def getName(self):
            return self.name
    def getAccnum(self):
            return self.acc_num
    def getBalance(self):
            return self.balance
    def getAcctype(self):
            return self.acc_type

    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount

    def transfer(self,amount):
        self.balance -= amount

    def bill(self,amount):
        self.balance -= amount

class CheckingAccount(Account):

    def getNameInfo(self):
        return "Account Name: "+str(Account.getName(self))
    def getBalanceInfo(self):
        return "Account Balance: "+str(Account.getBalance(self))
    def getAccNumInfo(self):
        return "Account Number: "+str(Account.getAccnum(self))
    def getAccTypeInfo(self):
        return "Account Type: "+str(Account.getAcctype(self))
    
class Investment(object):
    
    def __init__(self):
        self.generalinterest_rate=0.02
        self.goldinterest_rate=0.0080
        self.tlinterest_rate=0.09
        self.usdinterest_rate=0.02
        self.eurointerest_rate=0.0025

    def getGeneralInterestRate(self):
        return self.generalinterest_rate
    
    def getGoldInterestRate(self):
        return self.goldinterest_rate

    def getTlInterestRate(self):
        return self.tlinterest_rate

    def getUsdInterestRate(self):
        return self.usdinterest_rate

    def getEuroInterestRate(self):
        return self.eurointerest_rate


 

def GoldCalculation():
     
    invest=int(input("Enter amount to invest for gold: "))
    year=int(input("Year:"))
            
    interest=Investment()
    interest_rate=interest.generalinterest_rate

    future_value=0

    future_value+=invest
    income= (future_value)*interest_rate*year
    future_value+=income

    print("Future Value :",future_value)




def StockCalculation():
    
    future_value=0
    invest=float(input("Enter your current price for stock: "))
    year=int(input("Year:"))

    interest=Investment()
    interest_rate=interest.generalinterest_rate

    future_value+=invest
    income= (future_value)*interest_rate*year
    future_value+=income

    print("\nFuture Value:",future_value)

def CurrencyCalculation():

    
    future_value=0
    print("\nCurrency List")
    print("---------------")
    print("1.TL")
    print("2.USD")
    print("3.EURO")
    print("---------------")

    
    selection=int(input("\nEnter your selection: "))

    if selection==1:

        invest=float(input("Enter amount to invest for TL: "))
        year=int(input("Year:"))

        interest=Investment()
        interest_rate=interest.tlinterest_rate

        future_value+=invest
        income= (future_value)*interest_rate*year
        future_value+=income

        print("\nFuture Value:",future_value)

    
    if selection==2:

        invest=float(input("Enter amount to invest for USD: "))
        year=int(input("Year:"))

        interest=Investment()
        interest_rate=interest.usdinterest_rate

        future_value+=invest
        income= (future_value)*interest_rate*year
        future_value+=income

        print("\nFuture Value:",future_value)

    
    if selection==3:

        invest=float(input("Enter amount to invest for Euro: "))
        year=int(input("Year:"))

        interest=Investment()
        interest_rate=interest.eurointerest_rate

        future_value+=invest
        income= (future_value)*interest_rate*year
        future_value+=income

        print("\nFuture Value:",future_value)






def main():
    
      
   
    while True:
        print("\n\tMenu")
        print("--------------------")

        print("1.Create Bank Account")
        print("2.View Account")
        print("3.Check Balance")
        print("4.Withdraw")
        print("5.Deposit")
        print("6.Money Transfer")
        print("7.Paying Bills")
        print("8.Credit Inquiry")
        print("9.ROI Calculation")
        print("10.Exit")

        print("--------------------")

        
        selection=int(input("Enter your selection: "))
      
        os.system("cls")

        if selection==1:

            ac1=Account(
            input('Name: '),
            int(input('Balance: ')), 
            int(input('Account number: ')),
            (input('Account type: ')),

            )
            accounts=[ac1.getName(),ac1.getBalance(),ac1.getAccnum(),ac1.getAcctype()]

            allaccount=[]

            for i in allaccount:
                allaccount.append(accounts)
            
            
            print("\nAccount is created")
            

        if selection==2:

            chckaccount=CheckingAccount(ac1.name,ac1.balance,ac1.acc_num,ac1.acc_type)
            print(chckaccount.getNameInfo())
            print(chckaccount.getBalanceInfo())
            print(chckaccount.getAccNumInfo())
            print(chckaccount.getAccTypeInfo())
      

        if selection==3:

            print("Balance:",ac1.getBalance())


        if selection==4:
            amt = float(input("\nEnter amount to withdraw: "))

            if amt <= ac1.getBalance():
                 
                  ac1.withdraw(amt)
                  print("\nUpdated Balance: ",ac1.getBalance())
            else:
                  print("\nYou're balance is less than withdrawl amount: ", ac1.getBalance())
                  print("\nPlease make a deposit.")
 
        
            
        elif selection == 5:
            amt = float(input("\nEnter amount to deposit: "))
              
            ac1.deposit(amt)
                
            print("\nUpdated Balance: ",ac1.getBalance())
               
        elif selection == 6:

            amt=float(input("Enter amount to transfer: "))

            if amt<ac1.getBalance():
                ac1.transfer(amt)

                print(amt,"amount was successfully transferred")
                print("Updated Balance: ",ac1.getBalance())
            else:
                print("\nYou're balance is less than transfer amount: ", ac1.getBalance())
                print("\nPlease make a deposit.")

    
        elif selection==7:
            bill=150
            print("There is an bill of 150 TL waiting for payment.")
            
            if (ac1.getBalance()<bill):
                print("You can not pay for bill ")
            if(bill==0):
                print("Your bills have been paid.")

            elif(bill>0):

                select=input("Do you want to pay the bill? (y/n): ")

                if select.lower()=="y":
                    
                    ac1.bill(bill)

                    bill-=150
                    print("The bill was paid successfully.")

                else:
                    continue
        elif selection==8:
            
            if ac1.getBalance()>=1500:
                print("You are eligible to receive credit.")

            elif ac1.getBalance()<1500:
                print("You are not eligible to receive credit.")

                print("\nInfo:Your credit status is based on the current balance of your account.")

        elif selection==9:
            
            print("\nReturn on Investment Calculator")
            print("----------------------")
            print("1.Gold")
            print("2.Stock")
            print("3.Currency")

            selection=int(input("\nEnter your selection: "))

            
            if selection==1:
                
                GoldCalculation()
            
            elif selection==2:

                StockCalculation()
            
            elif selection==3:

                CurrencyCalculation()

        elif selection==10:
            break
            
            
if __name__ == "__main__":
    main()


