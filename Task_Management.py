task = []

while True:
    print("\n-------------------------------")
    print("WELCOME TO TASK MANAGEMENT APP")
    print("-------------------------------")
    
    print("\n1: Add Task")
    print("2: View task")
    print("3: Delete task")
    print("4: Exit ! ")
    
    choice = input("\nEnter your choice : ")
    
    if choice == "1":
        Add__Task = input("Enter your today task : ")
        task.append(Add__Task)
        print("Task added successfully ! ")
        
    elif choice == "2":
        if len(task) ==0:
            print("No task available : ")
        else:    
            for i in range(len(task)):
                print(i+1 , task[i])
            
    elif choice == "3":
        if len(task) == 0:
            print("No tasks to delete! ")
        else:       
            num = int(input("Enter your task number :  "))
            if num > 0 and num <= len(task):        
                task.pop(num-1)
                print("Your task deleted sucessfully (*_*) ")
            else:
                print("Invalid task number ! ")    
    
    elif choice == "4":
        print("Thank you : ")
        break     
    
    else:
        print("invalid option ! Please try again... " )        
    
    