expence_entry=[] #list ()tuple
s=0
while(s==0):
    name=input("Enter Payee")
    purpose=input("Enter purpose")
    amount=input("Enter Amount")
    exp_date=input("Date of Entry")
    #print(name+" "+purpose+" "+amount+" "+exp_date)
    expence_entry.append((name,purpose,amount,exp_date))
    print(expence_entry)
    s=int(input("Do you want to continue?press 0 for yes"))
