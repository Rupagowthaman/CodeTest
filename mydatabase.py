



from rich.console import Console
from rich.table import Table

from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker




database = create_engine("sqlite:///myfriendbook.db")
Base = declarative_base()

Session =sessionmaker(bind=database)
session=Session()

console=Console()


class Pet(Base):
    __tablename__ = "petanimals"
    id = Column(Integer, primary_key=True)
    petname = Column(String)



class Friend(Base):
    __tablename__ =  "Friendbook"


    id = Column(Integer,primary_key=True)
    firstname =Column(String)
    lastname =Column(String)
    # birthday =Column(String)
    # hobbies=Column(String)
    #email =Column(String)
    # city=Column(String)
    # country=Column(String)
    
    petname_id=Column(Integer,ForeignKey("petanimals.id"))



def initialize_database():
    Base.metadata.create_all(database)




def show_menu():

    
    MENU_TEXT = """
    Menu: 
    - (A)dd new Friend
    - (L)ist all Friends
    - (E)xit
    - (D)elete a record
    - (U)pdate a Friend
    """
    print(MENU_TEXT)



def getuserinput():

    menu_choice = input("Enter your Choice: ")
    
    if menu_choice == "A":
        add_newfriend()
    
    elif menu_choice =="L" :
        tolist_friends()

    elif menu_choice == "E":
        exit(1)
    
    elif menu_choice =="D" :
        
        deletefriends()
        print("record deleted")
    
    elif menu_choice=="U":
        updatefriends()
        print("The Record is updated")
            


def updatefriends():
    id = input("Pleses Enter id wnich you would like to Update\t:")
    firstname = input('Enter Firstname :\t')
    lastname = input("Enter Lastname :\t")
    update_friends= "UPDATE Friendbook SET lastname = '%s' , firstname= '%s'  WHERE id= '%s'" %(lastname,firstname,id)
    session.execute(update_friends)
    session.commit()



def add_newfriend():
    firstname = input('Enter Firstname :\t')
    lastname = input("Enter Lastname :\t")
    new_friend = Friend(firstname=firstname,lastname=lastname)
    database_add_friend(new_friend)    


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    """
    session.add(friend)
    session.commit()


def tolist_friends():

    friends = database_get_all_friends()
    table=Table(show_header=True,header_style="bold red")
    table.add_column("ID",style="bright")
    table.add_column("FirstNmae")
    table.add_column("LastNmae")
    


    for friend in friends:

        table.add_row(str(friend.id), friend.firstname, friend.lastname)


    console.print(table)


def database_get_all_friends():

    #all_friends=session.query(Friend).all()
    #all_friends=session.execute("SELECT * FROM Friendbook;").fetchall()
    #print(all_friends)
    return session.query(Friend).all()


def deletefriends():
    id = input("Pleses Enter id wnich you would like to delete\t:")
    deletefriends1= session.execute("DELETE FROM Friendbook WHERE id = '%s'" %(id,))
    session.commit()
  
    
        
if __name__=="__main__":

    initialize_database()
        

while True:

    show_menu()
    getuserinput()
    

 

 
    # firstname = input('Enter your Firstname :\t')
    # lastname = input("Enter your Lastname :\t")
    # r=session.execute('INSERT INTO Friendbook(firstname, lastname) VALUES (?,?)', (firstname, lastname))
    #print(r)
    #database_add_newfriend()
    

    #new_friend = Friend(firstname=firstname,lastname=lastname)
    #database_add_friend(new_friend)


    
