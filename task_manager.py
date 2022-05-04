#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
# Promt user for their useername and password
# Create a count variable 
username_count = 0
username = input("Please Enter Your Username: ")
password = input("Please Enter Your Password: ")
username_list = " "
password_list = " "

# Open file and create a list
# Use try and except so that the indexes stay in range
# Count the iterations for the statistics  
with open("user.txt","r") as user_file:
    for lines in user_file:
        lines = lines.replace(",","") 
        lines = lines.split()
        try:
            username_list += lines[0]
            username_count += 1 
            password_list += lines[1]
        except:
            continue
user_count = username_count            
user_file.close()        

# Use if variable to validate username and password
# Use x and y as control variables to make sure both username and password are validated
x = 0
y = 0
while x == 0 or y == 0:
    if username in username_list:
        print("Username found\n")
        x = 1
    elif username not in username_list:
        print("Username not found\n")
        username = input("Please Enter Your Username: ")  
    if password in password_list:
        print("Password found\n")
        y = 1
    elif password not in password_list:
        print("Password not found\n")
        password = input("Please Enter Your Password: ")
    else:
        print("Unknown error, Please try again.\n") 
        


while True:
    #Presenting the menu to the user and display a seperate menu for admin
    if username in "admin":
        menu = input("""\nSelect one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
e -  Exit
s -  Statistics\n\nEnter here: """).lower()
    else:
        menu = input("""\nSelect one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
e -  Exit\n\nEnter here: """).lower()

    if menu == 'r':
        pass
        # Promt user for info about the new user that they are logging
        # Validate passwords to make sure they are correct 
        if username in "admin":
            with open("user.txt","a+") as userfile_add:
                new_username = input("Please Enter New Users Username: ")
                new_password = input("Please Enter New Users Password: ")
                new_password_check = input("Please re-enter your password: ")
                if new_password == new_password_check:
                    userfile_add.write(new_username + "," + " " + new_password)
                    print("\nNew user entered \n")
                else:
                    print("\nPasswords are not the same, please try again.\n")  
            userfile_add.close()
        else:
            print("You do not have administration permissions")                  

    elif menu == 'a':
        pass
        # Promt user for info about new task 
        # Write that task to the tasks,txt file 
        task_user = input("Please enter the username of the person who needs to complete this task:  ")
        task_title = input("What is the name of this task: ")
        task_disc = input("Please describe the task: ")
        due_date = input("Please enter the due date in the format of dd/mm/year: ")
        current_date = input("What is todays date in the format of dd/mm/year: ")
        task_finished = "No"
        task_info = task_title + ", " + task_user + ", " + current_date + ", " + due_date + ", " + task_finished + ", " + task_disc + ", "
        
        with open("tasks.txt",'a+') as task_add:
            task_add.write("\n" + task_info)
            task_add.close()

    elif menu == 'va':
        pass
        # Print all the tasks that are logged
        # Use try and except so that the indexes stay in range
        # Create if statement to ensure that the strings have text 
        with open("tasks.txt",'r+') as view_all:
            for line in view_all :
                line = line.strip()
                line = line.split(", ")
                try:
                    if len(line) > 0:
                        try:
                            print("""\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(line[0],line[1],line[2],line[3],line[4],line[5]))
                        except:
                            continue
                except:
                    print("There are no tasks currently")        

    elif menu == 'vm':
        pass
        # Open tasks file and print all the tasks for a particular user 
        # Use try and except so that the indexes stay in range
        # if statement to print only the users tasks 
        with open("tasks.txt",'r') as view_1:
            for line in view_1 :
                    line = line.strip()
                    line = line.split(", ")
                    try:
                        if username in line:
                            try:
                                print("""\n\nTask:\t\t\t{}\nAssigned To:\t\t{}\nDate Assigned:\t\t{}\nDue Date:\t\t{}\nTask Complete:\t\t{}\nTask Description:\n{}\n""".format(line[0],line[1],line[2],line[3],line[4],line[5]))
                            except:
                                break
                    except:
                        print("There are no tasks for you")        

    # Closing statement    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    # Use view all in order to iterate through tasks logged
    # Use user_counter variable from the top for user stats  
    elif menu == 's':
        count = 0
        with open("tasks.txt",'r+') as view_all:
            for line in view_all :
                line = line.strip()
                line = line.split(", ")
                try:
                    if len(line) > 0:
                        try:
                            count += 1
                        except:
                            continue
                except:
                    continue
        print("\nThere are currently {} tasks logged.".format(count))
        print("There are currently {} users.\n".format(user_count))        

    else:
        print("You have made a wrong choice, Please Try again")
