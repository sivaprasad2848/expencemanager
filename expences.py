from helper import *
from fileoperations import *
s=0
expence_init=read_data()
set_expences(expence_init)
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
    if(option==3):
        delete_expence()
    if(option==4):
        update_expence()
    s=int(input("Do you want to continue?press 0 for yes"))
    if(s!=0):
         expences=get_expence()
         write_data(expences)

