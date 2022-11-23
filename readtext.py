



def choice():
    print('\n')
    print("- (A)dd new Names to the Text File\n")
    print("- (L)ist all Names from Text File\n")
    print("- (E)xit")
    print('\n')
    a=input("Enter Your choice :  ")
    print('\n')
    if (a=='A'):
        writefile()
    elif (a=='L'):
        readfile()
    else:
        exit()
        


def writefile():
    name=input("Enter Name: ")
    f = open('mynames.txt','r+')  
    if name not in f.read():
        f.write(name)
        f.write('\n')
        f.close()
    else:
        print("Name already exits")
    return

def readfile():
    f=open("mynames.txt", "r")
    print(f.read())

while True:
    if __name__=="__main__":
    
        choice()

    
