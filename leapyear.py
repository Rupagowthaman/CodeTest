



def leap_year():
    year=int(input("Enter Year : "))
    if (year % 4==0) and (year % 400==0):
        print(f" {year}  is a leap Year")
        return year
    elif (year % 4==0)and(year % 100 !=0) :
        print(f"{year} is a Leap Year")
        return year
    else:
        print(f" {year} is  not a Leap year ")

if __name__=="__main__":
    leap_year()

