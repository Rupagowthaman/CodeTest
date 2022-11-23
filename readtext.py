



def choice():
    print("- (A)dd new Names to the Text File\n")
    print("- (L)ist all Names from Text File\n")
    a=input("Enter Your choice :  ")
    if (a=='A'):
        writefile()
    elif (a=='L'):
        readfile()
        


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


if __name__=="__main__":
    
    choice()

    
