from helper import *
s=0
while(s==0):
    print("===================")
    print("1->For Insert")
    print("2->For Display")
    print("3->For delete")
    print("4->For Update")
    print("===================")
    option=int(input("Enter the option"))
    if(option==1):
        create_expence()
    if(option==2):
        #print(expence_entry)
        display_expences()
    s=int(input("Do you want to continue?press 0 for yes"))
