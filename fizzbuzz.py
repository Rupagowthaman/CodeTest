     

systeminput=1
count=0

print("*******************************")
print("Welcome to the Fizzbuzz Game")
print("*******************************")


name=input("Enter Your Name: ")
print(f"Hi {name} Welcome to the Fizzbuzz Game")
print("Lets get started")
print("")



def numbervalidation(myinput):

                                     
        if ( myinput % 3)==0 and (myinput % 5)==0:
                print(f"{myinput} : Fiizzbuzz")
        elif (myinput%3)==0:
                print(f"{myinput} : Fizz")
        elif (myinput%5)==0:
                print(f"{myinput}  : Buzz")
        else:
                print(myinput)

             
while True:

        numbervalidation(systeminput)
        mynumber = int(input("Enter your Number:  "))
        

        if(systeminput+1==mynumber):
                numbervalidation(mynumber)
                systeminput=systeminput+2
                count=count+1
                     
        else:
                print(f"{name} has played {count} times correctly")
                break
      
                
        
                

                



