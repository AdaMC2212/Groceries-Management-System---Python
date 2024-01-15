#CHIA YONG XIANG
#TP068455

def login_page():                                                                                           #This is the login page written in a function    
                                                                        
    while True:                                                                                                #The function is in a loop
        print("Welcome to FRESHCO online grocery store")                                                       #When user enter this function
        print("Select the type of user you are\n")                                                             #It'll print several lines
        print("1. Admin")
        print("2. New Customer")
        print("3. Registered Customer")
        print("4. Exit\n")
        
        try:                                                                                                   #try and except is to prevent user from entering input outside from the selection given
            user_choice = int(input("Enter your selection: "))                                                 #Then let user enter their input
            print()                                                                                            #print()is for spacing
            if user_choice == 1:                                                                               #If user's input is 1, he'll be brought to the admin function
               admin()
            elif user_choice == 2:                                                                             #If user's input is 2, he'll be brought to the new customer function
                new_customer()
            elif user_choice == 3:                                                                             #If user's input is 3, he'll be brought to the registered customer function
                registered_customer()
            elif user_choice == 4:                                                                             #If user's input is 4, the loop will be break and end the whole thing
                print("Thanks for using FRESHCO online grocery\nSee you next time")
                break
            else:
                print("\nInvalid input\nPlease try again\n")
                continue                                                                                       #if user enter input not in the selection, the loop will rerun 

        except:                                                                                                #except user enter input not integer, the loop will rerun 
            print("\nInvalid input\nPlease try again\n")
            continue                                                   

############################################################################################
        
def admin():                                                            #Admin function
    
    admin_username = input("Enter username: ")
    admin_pwd = input("Enter password: ")                               #Let admin user enter their username and password
    print()
    
    while True:                                                         #the loop in admin page is after the input of username and pwd so admin will not need to enter it everytime
        if admin_username == "FRESHCO.admin":                           #if the username is FRESHCO.admin
            if admin_pwd == "FRESHCO.admin.12345":                      #and if the password is FRESHCO.admin.12345
                
                print("Hi admin, what action do you need to do?\n")     #they can enter the admin page
                print("1. Upload groceries detail")                     #and several selection can be made by them
                print("2. View all uploaded groceries ")
                print("3. Modify groceries information")#update
                print("4. Delete groceries information")
                print("5. Search specific groceries detail")
                print("6. View all orders of customers")#all
                print("7. Search orders of specific customers")
                print("8. Exit back to login page\n")
                        
                try:                                                    #try (prevent entering input outside from the selection given)
                    admin_choice = int(input("Enter your selection: ")) #admin can input his selection
                    print()
                    if admin_choice == 1:                               #If input is 1, we'll be brought to the groceries_upload function to upload groceries
                        groceries_upload()
                    elif admin_choice == 2:                             #If input is 2, we'll be brought to the groceries_view function to view all groceries
                        groceries_view()
                    elif admin_choice == 3:                             #If input is 3, we'll be brought to the groceries_modify function to update groceries
                        groceries_modify()
                    elif admin_choice == 4:                             #If input is 4, we'll be brought to the groceries_delete function to delete groceries
                        groceries_delete()
                    elif admin_choice == 5:                             #If input is 5, we'll be brought to the groceries_search function to search for specific groceries
                        groceries_search()
                    elif admin_choice == 6:                             #If input is 6, we'll be brought to the order_view_all function to search for all orders by every customer
                        order_view_all()
                    elif admin_choice == 7:                             #If input is 7, we'll be brought to the order_view_search function to search for orders by a specific customer
                        order_view_search()
                    elif admin_choice == 8:                             #If input is 8, the loop will break and we'll be brought back to the login_page
                        print("Have a nice day\n")
                        break
                            
                except:                                                 #except user enter input not in the selection the loop will rerun
                    print("\nInvalid input\nPlease try again")
                    continue
            else:                                                       #if username is wrong, we'll be brought back to the loop in login_page
                print("Wrong username or password\n")
                break
        else:                                                           #if password is wrong, we'll be brought back to the loop in  login_page
            print("Wrong username or password\n")
            break

############################################################################################      

def new_customer():                                                             #new customer function 

    while True:                                                                 #this function is in a loop
        print("Hi new customer,Welcome to FRESHCO online grocery")
        print("What action do you need to do?\n")
        print("1. View groceries detail\t*Only registered customer can place order")
        print("2. Register for new account")
        print("3. Exit back to login page\n")
            
        try:                                                                    #try and except (prevent entering input outside from the selection given)
            new_cus_choice = int(input("Enter your selection: "))
            print()
            if new_cus_choice == 1:                                             #If input is 1, we'll be brought to the groceries_view function to view all groceries
                groceries_view()
            elif new_cus_choice == 2:                                           #If input is 2, we'll be brought to the information function to upload information
                register()
            elif new_cus_choice == 3:                                           #If input is 3, the loop will break and we'll be brought back to the loop in login_page
                print("Have a nice day\n")
                break
                    
        except:                                                                 #if user enter input not in the selection
            print("\nInvalid input\nPlease try again\n")
            continue                                                            #the loop will rerun

############################################################################################

def registered_customer():                                                      #registered_customer function

    try:
        fileHandler = open("information_list.txt","r")                          #open the information_list text file as read mode
    except:
        print("File cannot be found")                                           #except the file cannnot be opened, some lines will be printed 
        exit()                                                                  #and will exit this function using "exit()" back to the loop in login_page
    
    cus_username = input("Enter username:")                                     #user need to enter their username (also use as an argument to other function) 
    cus_password = input("Enter password:")                                     #user need to enter their password 
    print()
    count = 0                                                                   #count is set to 0

    for register in fileHandler:                                                #read strings in the information_list text file
        user_pwd = register.split()                                             #split the strings into list
        if len(user_pwd) >= 1:                                                  #if the length of the list >= 1 (to prevent from reading from empty line)
            if cus_username == user_pwd[5] and cus_password == user_pwd[6]:     #if the username and pasword are the 6th and 7th index of the list, run code below it
                count += 1                                                      #and count will be added
                
                while True:                                             #this function's loop starts here(everytime user back to this page they dont need to enter username n pwd again)
                    print("Hi, Welcome back to FRESHCO online grocery")         #print lines
                    print("What action do you need to do?\n")
                    print("1. View groceries detail")
                    print("2. Place order")
                    print("3. View own order")
                    print("4. Do payment")
                    print("5. View personal information")
                    print("6. Exit to login page\n")
                    
                    try:                                                        #try (prevent entering input outside from the selection given)
                        cus_choice = int(input("Enter your selection: "))
                        print()
                        if cus_choice == 1:                                     #If input is 1, we'll be brought to the groceries_view function to view all groceries
                            groceries_view()
                        elif cus_choice == 2:                                   #If input is 2, we'll be brought to the place_order function to place order
                            place_order(cus_username)                           #username that is entered above will be using as a parameter to this function
                        elif cus_choice == 3:                                   #If input is 3, we'll be brought to the order_view function to view own order
                            order_view(cus_username)                            #username that is entered above will be using as a parameter to this function
                        elif cus_choice == 4:                                   #If input is 4, we'll be brought to the payment function to do payment
                            payment(cus_username)                               #username that is entered above will be using as a parameter to this function
                        elif cus_choice == 5:                                   #If input is 5, we'll be brought to the information_view function to view own information
                            information_view(cus_username)                      #username that is entered above will be using as a parameter to this function
                        elif cus_choice == 6:                                   
                            print("Have a nice day\n")                          #If input is 6, the loop will break and we'll be brought back to the loop in login_page
                            break
                                        
                    except:                                                     #except user enter input not in the selection
                        print("\nInvalid input\nPlease try again\n")
                        continue                                                #the loop will rerun
                                                                              
    if count == 0:                                                              #if the count remain 0
        print("Wrong username or password\n")                                   #means that username and pasword are not the 5th and 6th index of the list
        login_page()                                                            #we'll be brought back to the login_page function 
                   
    fileHandler.close()                                                         #close the information_list text file
    
############################################################################################

def groceries_upload():                                                         #groceries_upload function
    
    all_groceries = []                                                          #main list to store all the sub lists

    while True:                                                                 #this function is also in a loop

        try:                                                                    #try (prevent entering input outside from the selection given)
            grocery_num = int(input("Please enter the number of groceries you want to upload: "))
            print()
            for i in range (grocery_num):                                       #for loop (run the loop n times)*n means the integer entered in grocery_num
                grocery = []                                                    #sub list to store all the data
                grocery_category = input("Enter grocery category: ")
                grocery.append(str(grocery_category.lower()))                   #append the grocery category in lowercase to a sublist
                grocery_name = input("Enter grocery name: ")
                grocery.append(str(grocery_name.lower()))                       #append the grocery name in lowercase to a sublist
                grocery_price = float(input("Enter grocery price: RM"))
                grocery.append("RM"+str(grocery_price))                         #append the grocery price to a sublist
                grocery_expdate = input("Enter grocery expiry date: ")
                grocery.append(str(grocery_expdate))                            #append the grocery expiry date to a sublist
                print()
                all_groceries.append(grocery)                                   #append all sublists into the main list

            print("All groceries have been uploaded\n")
            break
                
        except:                                                                 #except user enter input not in the selection
            print("\nInvalid input")
            try_again = input("Press ENTER to try again or press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if their input is ENTER
                continue                                                        #the loop will rerun
            
            else:                                                               #if their input is other keys
                print ("Leaving page\n")
                break                                                           #the loop will break and we'll be brought back to the loop in admin page

    try:
        fileHandler = open('groceries_list.txt','a')                            #open the groceries_list text file as append mode
    except:                                                                     #except the file cannnot be opened
        print("File cannot be found")
        exit()                                                                  #exit this function and back to the loop in admin page

    for grocery in all_groceries:                                               #read the sublists from the main list
        for i in grocery:                                                       #read the data in sublist
            fileHandler.write(i)                                                #write out every data
            fileHandler.write("\t\t")                                           #tab between every data
        fileHandler.write("\n")                                                 #new line between every sublist
    fileHandler.close()                                                         #close the groceries_list text file

############################################################################################

def groceries_view():                                                           #the groceries_view function
    
    try:
        fileHandler = open('groceries_list.txt','r')                            #open the groceries_list text file as read mode
    except:                                                                     #except the file cannnot be opened
        print("File cannot be found")
        exit()                                                                  #exit this function and back to the loop in admin page

    for groc in fileHandler:                                                    #read every line in the file
        print(groc)                                                             #print every line
        
    fileHandler.close()                                                         #close the groceries_list text file

############################################################################################

def groceries_modify():                                                         #the groceries_modify function
    
    modify_list = []                                                            #main list to store data

    while True:                                                                 #loop this function

        try:
            fileHandler = open('groceries_list.txt','r')                        #open the groceries_list text file as read mode
        except:                                                                 
            print("File cannot be found")                                               
            exit()                                                              
            
        count = 0                                                               #set count as 0
        groceries_view()                                                        #call out the groceries view function to see all he groceries detail
        modify = input("What grocery do you want to modify (grocery name): ")
            
        for line in fileHandler:                                                #read every line from file
            line = line.split()                                                 #split every thing in the line into lists
            modify_list.append(line)                                            #append all lists into the main list (modify_list)
            if len(line) > 1:                                                   #if the length of the list >= 1 (to prevent from reading from empty line)
                if modify.lower() == line[1]:                                   #if the input is the second index from the list, run code below
                    count += 1                                                  #count is added
                    print()
                    print("1. Groceries category")
                    print("2. Groceries name")
                    print("3. Groceries price")
                    print("4. Groceries expiry date\n")
                    try:                                                        #try (prevent entering input outside from the selection given)
                        index =  int(input("Select which detail you want to update: "))
                        print()
                        if index == 1:                                          #if input is 1
                            replace = input("What you want to replace the category as: ")
                            print()
                            line[0] = (replace)                                 #replace the first index with another input (same thing with the lines after)

                        elif index == 2:                                          
                            replace = input("What you want to replace the name as: ")
                            print()
                            line[1] = (replace) 

                        elif index == 3:
                            while True:                                     #another loop
                                try:                                        #try (prevent entering input outside from the selection given)
                                    replace = float(input("What you want to replace the price as: RM"))
                                    print()
                                    if replace > 0:                         #if input is > 0 
                                        line[2] = ("RM"+str(replace))
                                        break                               #break the loop and run line after

                                except:                                     #except user enter input not > 0
                                    print("\nInvalid input\nPlease try again\n")
                                    continue                                #rerun the loop

                        elif index == 4:
                            replace = input("What you want to replace the expiry date as: ")
                            print()
                            line[3] = (replace)                  

                        print("Grocery's detail have been replaced\n")
                                                                                         
                    except:                                                     #except user enter input not in the selection
                        print("\nInvalid input\nPlease try again\n")
                        continue                                                #rerun the loop
                    
        if count == 0:                                                          #if the count remain 0
            print("\nGrocery not found")
            try_again = input("Press ENTER to try again or Press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if their input is ENTER
                continue                                                        #rerun the loop
                            
            else:                                                               #if not ENTER
                print ("Leaving page\n")                                                                       
                                                                           

        break                                                                   #break the loop so code below can run
    
    try:
        fileHandler = open('groceries_list.txt','w')                            #open the groceries_list text file as write mode
    except:
        print("File cannot be found")                                           
        exit()

    for sub in modify_list:                                                     #read all lists from the main list(modify_list)
        for data in sub:                                                        #read all the data from list
            if len(data) > 0:
                fileHandler.write(data)                                         #write out every data into the text file
                fileHandler.write("\t\t")                                       #tab between every data
        fileHandler.write("\n")                                                 #new line between every sublist

    fileHandler.close()                                                         #close the groceries_list text file
                                                                                #back to the loop in admin page
           
###########################################################################################

def groceries_delete():                                                         #the groceries_delete function
    
    while True:                                                                 #in a while loop

        try:
            fileHandler = open('groceries_list.txt','r')                        #open the groceries_list text file as read mode
        except:
            print("File cannot be found")
            exit()
            
        read = fileHandler.readlines()                                          #readlines(read all line n turn them into seperate lines)
        groceries_view()                                                        #call out the groceries view function to see all he groceries detail

        try:
            fileHandler = open('groceries_list.txt','w')                        #open the groceries_list text file as write mode
        except:
            print("File cannot be found")
            exit()
             
        delete = input("\nWhat grocery do you want to delete: ")
        count = 0                                                               #set count as 0
        
        for data in read:                                                       #read all data from the seperate lines
            grocery_index = data.split()                                        #split every data in line into lists
            if delete.lower() == grocery_index[1]:                              #if input is the 2nd index of data 
                count += 1                                                      #count will be added
                print("\nGrocery has been deleted\n")
                
        
            else:                                                               #if input is not the 2nd index of data
                fileHandler.write(data)                                         #write the data back into the text file
                
        if count == 0:                                                          #if the count remain 0
            print("\nGrocery not found")
            try_again = input("Press ENTER to try again or Press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if input is ENTER
                continue                                                        #rerun the loop
                
            else:                                                               #if not ENTER
                print ("Leaving page\n")
        break                                                                   #break the loop back to the loop in the admin page

    fileHandler.close()                                                         #close the groceries_list text file
    
############################################################################################

def groceries_search():                                                         #the groceries_search function
    
    while True:                                                                 #in a while loop
        
        try:
            fileHandler = open('groceries_list.txt','r')                        #open the groceries_list text file as read mode
        except:
            print ("File cannot be found:")
            exit()

        search = input("What you want to search: ")
        count = 0                                                               #set count as 0

        for data in fileHandler:                                                #read all data from file
            view = data.split()                                                 #split every data in line into lists
            if len(view)> 1:                                                    #if the length of the list >= 1 (to prevent from reading from empty line)
                if search.lower() == view[1]:                                   #if input is the 2nd index of data
                    count += 1                                                  #count will be added
                    print(data)                                                 #print
                
        if count == 0:                                                          #if the count remain 0
            print("\nGrocery not found")
            try_again = input("Press ENTER to try again or Press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if input is ENTER
                continue                                                        #rerun the loop
                
            else:                                                               #if not ENTER
                print ("Leaving page\n")
        break                                                                   #break the loop back to the loop in the admin page
                
    fileHandler.close()                                                         #close the groceries_list text file

############################################################################################

def order_view_all():                                                           #order_view_all function
    
    try:
        fileHandler = open('order_list.txt','r')                                #open the order_list text file as read mode
    except:
        print("File cannot be found")
        exit()

    for all_order in fileHandler:                                               #read the data from text file
        print(all_order)                                                        #print all data
        
    fileHandler.close()                                                         #close the order_list text file
                                                                                #back to the loop in admin page

############################################################################################

def order_view_search():                                                        #order_view_search function
    
    while True:                                                                 #in a while loop
        
        try:
            fileHandler = open('order_list.txt','r')                            #open the order_list text file as read mode
        except:
            print("File cannot be found")
            exit()

        search_cus = input("Which customer's order you want to search: ")
        print()
        count = 0                                                               #set count as 0
        
        for order in fileHandler:                                               #read the data from text file 
            order_index = order.split()                                         #split every data in line into lists
            if len(order_index)>1:
                if search_cus == order_index[0]:                                #if input is the 2nd index of data, run codes below
                    count += 1                                                  #count will be added
                    print(order_index)
                    print()

        if count == 0:                                                          #if the count remain 0
            print("\nUsername not found")
            try_again = input("Press ENTER to try again or Press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if input is ENTER
                continue                                                        #rerun the loop
                        
            else:                                                               #if not ENTER
                print ("Leaving page\n")
        break                                                                   #break the loop back to the loop in the admin page
        
    fileHandler.close()                                                         #close the order_list text file

############################################################################################
    
def register():                                                                 #register function

    info = []                                                                   #main list
    while True:                                                                 #in a while loop
        
        print("Enter your information for registration\n")
        name    =   input("Enter name: ")
        info.append(str(name))                                                  #append the name (and others) to the main list
        address =   input("Enter address: ")
        info.append(str(address))                                               
        email   =   input("Enter email: ")
        info.append(str(email))                                                 
        
        while True:                                                         #another while loop
            try:
                contact =   int(input("Enter contact number: +60"))
                if contact > 0:
                    info.append(str(contact))                               #append the contact to the main list if the user input is > 0
                    break                                                   #break this loop
            except:
                print("This is not a legit contact number\n")
                continue                                                    #if not rerun this loop
            
        birthdate = input("Enter date of birth (exp.01JAN2002): ")
        info.append(str(birthdate))                                             
        username=   input("Enter username: ")
        info.append(str(username))
        pwd     =   input("Enter password: ")
        
        while True:                                                         #another while loop
            repwd =  input("Rewrite password: ")
            print()
            if pwd != repwd:                                                #if the passwords arent same
                print("Password not same")
                continue                                                    #break this loop
            else:
                info.append(str(pwd))                                       #if same append password into main list n break this loop
                break

        print("Name: ",name,"\nAddress: ",address,"\nEmail: ",email)
        print("Contact number: +60",contact,"\nDate of birth: ",birthdate,"\nUsername: ",username,"\nPassword: ",repwd)
        print("Are all the information entered correct?")
        confirm = input("Press ENTER to confirm or Press ANY KEY to try again ")
        print()
        if confirm == "":                                                       #if input is ENTER                                                   
            break                                                               #break the loop and back to run code below
        else:
            continue                                                            #rerun the loop if not ENTER
            
    print("All information has been saved\n")
    
    try:
        fileHandler = open('information_list.txt','a')                          #open the information_list text file as append mode
    except:
        print("File cannot be found")
        exit()

    for data in info:                                                           #read the data from the main list
        fileHandler.write(data)                                                 #write data in text file
        fileHandler.write("\t\t")
    fileHandler.write("\n")
    fileHandler.close()                                                         #close the information_list text file
                                                                                #back to the loop in admin page

############################################################################################

def information_view(cus_username):                                 #information_view function with cus_username(entered in registered_customer page)as parameter
    
    try:
        fileHandler = open('information_list.txt','r')                          #open the information_list text file as read mode
    except:
        print("File cannot be found")
        exit()
    
    for info in fileHandler:                                                    #read the data from the text file
        view = info.split()                                                     #split every data in line into lists
        if len(view) >= 1:
            if cus_username == view[5]:                                         #if cus_username(entered in registered_customer page)is the 6th index,run codes below
                print("Name: " + view[0])
                print("Address: " + view[1])
                print("Email: " + view[2])
                print("Contact number: " + view[3])
                print("Date of birth: " + view[4])
                print("Username: " + view[5])
                print("Password: " + view[6])
                print()
        
    fileHandler.close()                                                         #close the information_list text file
                                                                                #back to the loop in registered_customer page

############################################################################################

def place_order(cus_username):                                  #place_order function with cus_username(entered in registered_customer page)as parameter

    all_order = []                                                              #main list
    while True:                                                                 #in a while loop
        
        try:
            fileHandler = open('groceries_list.txt','r')                        #open the groceries_list text file as read mode
        except:
            print ("File cannot be found:")
            exit()
        
        buy = input("Please select which grocery you want to order: ")
        count = 0                                                               #set count as 0
            
        for line in fileHandler:                                                #read the data from the text file
            buy_grocery = line.split()                                          #split every data in line into lists 
            if buy.lower() == buy_grocery[1]:                                   #if input is the 2nd index
                
                count += 1                                                      #count will be added
                print(buy_grocery)             
                order = []                                                      #sub list
                
                order.append(str(cus_username))                                 #append into sub list
                order.append(str(buy))
                
                price = buy_grocery[2]
                order.append(str(price))
                
                while True:                                                 #another while loop(to make sure input is integer)
                    try:
                        quantity = int(input("\nHow many would you like to order?: "))
                        if quantity > 0:
                            order.append(str(quantity))
                            break                                           #break this loop to run code below
                    except:
                        print("\nInvalid input\nPlease try again")
                        continue                                            #rerun the loop if input not > 0
                    
                total_price = float(price[2:]) * quantity                       #calculate total price(price[2:] is to slice the RM from price)
                order.append(str(total_price))
                
                all_order.append(order)                                         #sub lists append into main list   

                print("\nYour order have been placed\n")
                
                try:
                    fileHandler = open('order_list.txt','a')                    #open the order_list text file as append mode
                except:
                    print("File cannot be found")
                    exit()

                for sub in all_order:                                           #read sub lists from main list                            
                    for data in sub:                                            #read data from sub list
                        fileHandler.write(data)                                 #write data into text file
                        fileHandler.write("\t\t")
                    fileHandler.write("\n")
                fileHandler.close()                                             #close the order_list text file
                          
        if count == 0:                                                          #if the count remain 0
            print("\nGrocery not found")
            try_again = input("Press ENTER to try again or Press ANY KEY to exit ")
            print()
            if try_again == "":                                                 #if input is ENTER
                continue                                                        #rerun the loop
                        
            else:                                                               #if not ENTER
                print ("Leaving page\n")
                break                                                           #break the loop back to the loop in the registered_customer page

        else:                                                                   #if count not remain 0
            print("Do you still have other orders?")
            confirm = input("Press ENTER to take other orders or Press ANY KEY to exit")
            print()
            
            if confirm == "":                                                   #if input is ENTER  
                place_order(cus_username)                                       #back to place_order function
            
            else:                                                               #if not ENTER
                print ("Thank you for ordering")
                payment(cus_username)                                           #go to payment function
                
        break                                                                   #break the loop and back to the loop in registered_customer page

############################################################################################
    
def order_view(cus_username):                                                   #order_view function with cus_username(entered in registered_customer page)as parameter
    
    try:
        fileHandler = open('order_list.txt','r')                                #open the order_list text file as read mode
    except:
        print("File cannot be found")
        exit()
    
    for order in fileHandler:                                                   #read the data from text file 
        order_index = order.split()                                             #split every data in line into lists
        if len(order_index)>1:
            if cus_username == order_index[0]:                                  #if cus_username(entered in registered_customer page)is the 1st index,run codes below
                print(order_index)
                print()
        
    fileHandler.close()                                                         #close the groceries_list text file
                                                                                #back to the loop in registered_customer page

############################################################################################

def payment(cus_username):                                                      #payment function with cus_username(entered in registered_customer page)as parameter
    
    while True:                                                                 #in a while loop
        
        try:
            fileHandler = open('order_list.txt','r')                            #open the order_list text file as read mode
        except:
            print("File cannot be found")
            exit()

        read = fileHandler.readlines()                                          #readlines(read all line n turn them into seperate lines)
        total = 0                                                               #set total = 0

        print("\nPay now or Pay later?")
        pay = input("Press ENTER to pay now or Press ANY KEY to pay later ")
        print()
        if pay == "":                                                           #if input is ENTER
            
            for line in read:                                                   #read data from the seperate lines
                order_index = line.split()                                      #split every data in line into lists
                if len(line)>1:
                    if cus_username == order_index[0]:                          #if cus_username(entered in registered_customer page) is the 1st index of data, run code below

                        print(order_index[1].upper(),"\t Single price: ",order_index[2],"\t Quantity: ",order_index[3],"\t Total price: RM",order_index[4])

                        total_price = order_index[4]

                        total += float(total_price)                             #calculate the total by adding the total price from each seperate lines
                            
                
            if total == 0:                                                      #if total remain 0
               print("No order placed\n")
               break                                                            #break the loop and back to loop in registered_customer page

        else:                                                                   #if input not ENTER
            break                                                               #break the loop and back to loop in registered_customer page

        print("\nTotal amount: RM",str(total))

        try:
            amount = float(input("Enter amount: RM "))                          #Enter amount(must be integer)
            if amount > 0:
                if amount < total:                                              #if amount not enough
                    print("Insufficient balance")
                    continue                                                    #rerun this loop
                            
                else:
                    print("Changes: RM",(amount-total))
                    print("Thank you for using FRESHCO online grocery store\n")
                    
                        
        except:
            print("Invalid input\nPlease try again\n")
            continue                                                            #except input not integer, rerun this loop

                            
        try:
            fileHandler = open('order_list.txt','w')                            #open the order_list text file as write mode
        except:
            print("File cannot be found")
            exit()
            
        for line in read:                                                       #read data from the seperate lines
            order_indexx = line.split()                                         #split every data in line into lists
            if len(order_indexx)>1:
                if cus_username == order_indexx[0]:                             #if cus_username(entered in registered_customer page)is the 1st index of data, run code below                    
                    print("")

                else:                                                           #if cus_username not in 1st index
                    fileHandler.write(line)                                     #write data into text file

        
        break                                                                   #break loop into the loop in registered_customer page
        fileHandler.close()                                                     #close the groceries_list text file
                         
############################################################################################     
login_page()
