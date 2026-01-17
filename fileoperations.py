def write_data(expences):
    #print("We will write data here")
    fp=open("expences.txt","w")
    for item in  expences:
        line=item[0]+"-"+item[1]+"-"+item[2]+"-"+item[3]+"\n"
        fp.write(line)
    fp.close()    
def read_data():
    expences = []
    try:
        fp = open("expences.txt", "r")
        for line in fp:
            line = line.strip()  # remove newline
            parts = line.split("-")  # split by hyphen
            if len(parts) == 4:
                expences.append(tuple(parts))  # convert list to tuple
        fp.close()
    except FileNotFoundError:
        print("expences.txt not found.")

    return expences
