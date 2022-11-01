



from datetime import date, datetime
from datetime import date
from re import A
import time
import datetime
from sqlite3 import Date
from rich.console import Console
from rich.table import Table

from rich.console import Console
from rich.table import Table



from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

database = create_engine("sqlite:///todo2.db")
Base = declarative_base()

Session =sessionmaker(bind=database)
session=Session()

console = Console()

task_date = str
task_time = str

class Task(Base):

    __tablename__ =  "Tododatabase"

    task_id =Column(Integer,primary_key=True)
    task_Name =Column(String)
    task_date = Column(String)
    task_time = Column(String)
    task_Status =Column(String)
    

def initialize_database():
    Base.metadata.create_all(database)


def show_menu():

    
    Taskmenu = """
    Task: 
    - (A)dd new Task
    - (L)ist all Tasks
    - (U)date Tasks
    - (C)ompleted Task
    - (P)ending Tasks
    - (D)elete a Task
    - (E)it
    
    """
    print(Taskmenu)
    


def getuserinput():

    menu_choice = input("Enter your Choice: ")
    
    if menu_choice == "A":
        add_Task()
    
    elif menu_choice =="L" :
        
        tolist()

    elif menu_choice == "E":
        exit(1)
    
    elif menu_choice =="D" :
        deletetask()

    elif menu_choice=="U":
        update_Task()

    elif menu_choice=="C":
        completed_list()
    elif menu_choice=="P":
        pendinglist()
        





def add_Task():
    
    task_Name = input("enter the task: ")
    task_date = input("Enter a date in YYYY-MM-DD format: ")
    task_time=input("Enter the  Time (H:M)format: ")
    
    c=(task_date+" "+task_time)
    x = datetime.datetime.now()
    d = datetime.datetime.strptime(c, '%Y-%m-%d %H:%M')
    
    print(d)
    if d > x:
          
        addtask = "INSERT INTO Tododatabase (task_Name, task_date, task_time, task_Status) VALUES ('%s','%s',' %s','pending')" %(task_Name,task_date,task_time)
   
        a=session.execute(addtask)
        print("Task Created Sucsessfully")
    
        session.commit()
    else:
        print("Enter the valid Date and Time")


def update_Task():

    x=datetime.datetime.now()
    #print(x)
    #print(task_date)
    updatetask= "UPDATE Tododatabase SET task_Status= 'Completed' where task_date <= '%s'" %(x)
    session.execute(updatetask)
    session.commit()
    print("The tasks are  Sucessfully Updated")
    
    
     
def completed_list():

   
    s=session.execute("SELECT * FROM Tododatabase WHERE task_Status = 'Completed'").fetchall()
    print(s)
    


    tasks2 = session.query(Task).all()
    table1=Table(show_header=True,header_style="bold red")
    table1.add_column("ID",style="bright")
    table1.add_column("TaskName")
    table1.add_column("Taskdate")
    table1.add_column("Task_time")
    table1.add_column("TaskStatus")
       

    for task in s:

        table1.add_row(str(task.task_id), task.task_Name, task.task_date, task.task_time, task.task_Status)

    console.print(table1)



def pendinglist():
    s=session.execute("SELECT * FROM Tododatabase WHERE task_Status = 'pending'").fetchall()
    print(s)
    


    tasks2 = session.query(Task).all()
    table1=Table(show_header=True,header_style="bold red")
    table1.add_column("ID",style="bright")
    table1.add_column("TaskName")
    table1.add_column("Taskdate")
    table1.add_column("Task_time")
    table1.add_column("TaskStatus")
       

    for task in s:

        table1.add_row(str(task.task_id), task.task_Name, task.task_date, task.task_time, task.task_Status)

    console.print(table1)




def tolist():

    all_tasks=session.query(Task).all()
    all_tasks=session.execute("SELECT * FROM Tododatabase;").fetchall()
    print(all_tasks)
    

    tasks1 = session.query(Task).all()
    table=Table(show_header=True,header_style="bold red")
    table.add_column("ID",style="bright")
    table.add_column("TaskName")
    table.add_column("Taskdate")
    table.add_column("TaskTime")
    table.add_column("TaskStatus")

    for task in tasks1:

        table.add_row(str(task.task_id), task.task_Name, task.task_date, task.task_time,task.task_Status)

    console.print(table)


def deletetask():
    task_id =input("Pleses Enter the taskID to be Deleted\t:")
    deletetask= session.execute("DELETE FROM Tododatabase WHERE task_id = '%s'" %(task_id,))
    session.commit()
    print(f"The task '{task_id}' is deleted Sucessfully")


if __name__=="__main__":

    initialize_database()
    task = Task()
  
while True:  
    

    show_menu()
    getuserinput()
    
   

