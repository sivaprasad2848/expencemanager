def write_data(expences):
    #print("We will write data here")
    fp=open("expences.txt","w")
    for item in  expences:
        line=item[0]+"-"+item[1]+"-"+item[2]+"-"+item[3]+"\n"
        fp.write(line)
    fp.close()    
def read_data():
    print("We will reada data from here")