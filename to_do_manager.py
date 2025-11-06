import sys

tasks=[]
def menu():
    '''SHOWS MENU AND RETURNS THE CHOSEN'''


    print("Menu:","1 Add Task","2 View Tasks","3 remove Task","4 Quit",sep="\n")
    while True:
        try:
            choosed=int(input("Enter(1,2,3,4):"))
            if choosed in (1,2,3,4):
                return choosed
            print("please enter between (1,2,3,4)")
        except ValueError:
            print("Enter Integer.")




def add():
    '''ADDS TASKS'''
    task=input("enter the task to add:")
    tasks.append(task)
    return




def view():
    '''YOU CAN VIEW ALL TASKS'''
    if len(tasks)==0:
        print("you have no tasks added.")
        return
    
    print("your tasks are ->")
    for i,v in enumerate(tasks):
        print(f"{i+1}:{v}")





def remove():
    '''THIS REMOVES TASKS'''
    view()
    if len(tasks)==0:
        return
    while True:
        value=input("Enter value to remove:")
        if value not in tasks:
            print("Enter valid task.")
        else:
            tasks.remove(value)
            return

    


        
def manager():
    '''THIS IS THE MAIN MANAGER'''
    while True:
        choosed=menu()
        if choosed==4:
            print("Thank you for using our task manager.")
            sys.exit()
        elif choosed==3:
            remove()
        elif choosed==2:
            view()
        elif choosed==1:
            add()
            
        




#WILL ADD DELETE HISTORY LATER
manager()


