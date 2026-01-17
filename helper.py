expence_entry=[] #list ()tuple
def create_expence():
    name=input("Enter Payee")
    purpose=input("Enter purpose")
    amount=input("Enter Amount")
    exp_date=input("Date of Entry")
    #print(name+" "+purpose+" "+amount+" "+exp_date)
    expence_entry.append((name,purpose,amount,exp_date))
def display_expences():
     for item in expence_entry:
            #print(item)
            print(item[0]+" "+item[1]+" "+item[2]+" "+item[3]) 
def delete_expence():
     display_expences()
     position=int(input("Enter the position you want to delete"))
     del expence_entry[position] 
def update_expence():
     display_expences()
     position=int(input("Enter the position you want to update"))
     name=input("Enter Payee")
     purpose=input("Enter purpose")
     amount=input("Enter Amount")
     exp_date=input("Date of Entry")
     expence_entry[position]=(name,purpose,amount,exp_date)
def get_expence():
     return expence_entry
def set_expences(data):
     global expence_entry
     expence_entry=data
     