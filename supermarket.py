import sys #we use it at the end to stop the code
Meats= []
Seafoods =[]
Frozenfoods = []
Groceries = []
Bakeries= []
Bakery={
        'bread': 5,
        'roll':15,
        'pie':25,
        'pastry':30,
        'muffin':25
    }

Seafood={
    'catfish' : 40,
    'tilapia' :50,
    'pacific halibut':60,
    'sole':25,
    'snow crab':80
}

Frozenfood={
    'frozen check meet pizza' :20,
    'frozen kibbah': 18,
    'frozen charry' : 15,
    'frozen berries' :15,
    'ice cream' :20
}

Meat={
    "cow" :30,
    "goat": 20,
    "chicken":25
}

Grocery={
      'milk' : 15  ,
      'yogurt'   :10,
      'chips' : 25  ,
      'candy' : 35 ,
      'sodas' : 30
}
def CreateAcc():
    Users = open("Login.txt", "r");
    login = input("Create a Username : ");
    Password1 = input("Create a Password : ");
    Password2 = input("Confirm Password : ");
    usr = []; #Making a list of users
    pss = []; #making a list of passwords
    spliter = 0;
    for i in Users:
        sp =  i.split("|| "); #in the txt file its 'user|| password" so we split each variable on an array called sp
        for x in sp :
            if spliter%2 != 0: # this is complicated , so the first user would be 1 on sp , the password is the 2 , so we store 1 in usr and 2 in pass 3 in user 4 in pass etc...
                x = x[:-1] #lenght -1 cause we have the \n at the end
                usr.append(x);
            else:
                pss.append(x);
            spliter=spliter+1;
    if Password1 != Password2: #check if the passwords match
        print("checkpassword");
        CreateAcc();
    else:
        if login in Users : #check if username is taken
            print("Username is already taken");
            CreateAcc();
        else:
            Users = open("Login.txt", "a");
            Users.write(login +"|| "+Password1+"\n")# we store in file
            print("Success !")

def conection():
    x = 0
    Users = open("Login.txt", "r");
    login = input("User : ");
    Password1 = input("Pass : ");
    if not len(login or Password1) < 1 :
        Spliter = 0;
        usr = [];
        pss = [];
        for i in Users:
            sp = i.split("|| ");
            for x in sp:
                if Spliter % 2 == 0:#same as before
                    usr.append(x);
                else:
                    x = x[:-1]
                    pss.append(x);
                Spliter = Spliter + 1;
        json = dict(zip(usr, pss))#turning everything to a json
        try:
            if json[login]:
                if Password1 == json[login]: #checking if the password is owned by user
                    print("Success");
                    print("Hi !", login);
                    x=1
        except:
            print("pass or username invalid")
    if x == 1:
        supermarket()
def hub ():

    option = input("For login press 1 and for signup press 2 \n")
    if option == "1":
        conection();
    elif option == "2":
        CreateAcc();
    else:
        print("invalid option")

def supermarket():

    total = 0
    Command = open("Shop.txt", "w");
    print("1 for bakery || 2 for meat || 3 for seafood || 4 for frozen food || 5 for grocery || 0 for bills ");
    choice = int(input("enter your choice :"));
    print(choice)
    if choice == 1:
        for i in range(len(Bakery)): #Here we do a loop , we could do While true , just like a BIG loop
            print("bread 5SR || roll  15SR || pie 20SR || pastry 30SR || muffin 25SR ");
            xz = input("if you want to buy press 1 if you wanna go back to the section press 0 :");
            if xz == "0":
                supermarket()
            if xz == "1":
                item=input("Enter your item : \n")
                item = item.lower() #we lower input , it bugs sometimes
                quantity=int(input("Enter quantity : \n"))
                if quantity != 0 :
                    if item in Bakery.keys(): #we check if the item the user typed is on the item object
                        price = quantity * (Bakery[item]); # we calculate the price
                        Bakeries.append((item ,quantity, price)) # we add everything to an array of tuples
    elif choice == 2: #same for everything , just copy paste code and changing variable names
        for i in range(len(Meat)):
            print("cow 30SR/kg || goat  20SR/kg || chicken 25SR/kg ");
            xz = input("if you want to buy press 1 if you wanna go back to the section press 0 :");
            if xz == "0":
                supermarket()
            if xz == "1":
                item = input("Enter your item : \n")
                item.lower()
                quantity = int(input("Enter how many KG: \n"))
                if quantity != 0:
                    if item in Meat.keys():
                        price = quantity * (Meat[item]);
                        Meats.append((item, quantity, price))
    elif choice == 4:
        for i in range(len(Frozenfood)):
            print("frozen pizza 20SR || frozen kibbah  18SR || frozen charry 15SR || frozen berry 15SR || ice cream 20SR ");
            xz = input("if you want to buy press 1 if you wanna go back to the section press 0 :");
            if xz == "0":
                supermarket()
            if xz == "1":
                item = input("Enter your item : \n")
                item.lower()
                quantity = int(input("Enter quantity : \n"))
                if quantity != 0:
                    if item in Frozenfood.keys():
                        price = quantity * (Frozenfood[item]);
                        Frozenfoods.append((item, quantity, price))
    elif choice == 3:
        for i in range(len(Seafood)):
            print("catfish 40SR/kg  || tilapia  50SR/kg  || pacific halibut 60SR/kg  || sole 25SR/kg  || snow crab 80SR/kg ");
            xz = input("if you want to buy press 1 if you wanna go back to the section press 0 :");
            if xz == "0":
                supermarket()
            if xz == "1":
                item = input("Enter your item : \n")
                item.lower()
                quantity = int(input("Enter how many KG: \n"))
                if quantity != 0:
                    if item in Seafood.keys():
                        price = quantity * (Seafood[item]);
                        Seafoods.append((item, quantity, price))
    elif choice == 5:
        for i in range(len(Grocery)):
            print( "milk 15SR  || yogurt   10SR  || chips 25SR  || candy 35SR || sodas 30SR ");
            xz = input("if you want to buy press 1 if you wanna go back to the section press 0 :");
            if xz == "0":
                supermarket()
            if xz == "1":
                item = input("Enter your item : \n")
                item.lower()
                quantity = int(input("Enter quantity: \n"))
                if quantity != 0:
                    if item in Grocery.keys():
                        price = quantity * (Grocery[item]);
                        Groceries.append((item, quantity, price))

    elif choice == 0:
        if Groceries: #Check if groceries is empty
            Command.write("\n Grocers\n")
        for a, b, c in Groceries: #Loop through grocery A for item B for quantity C for price
            total = total + c #we count everything in total
            Command.write(a + "\t \t \t" + str(b) + "\t \t \t" + str(c) + "\n")
        if Bakeries: # everything from here is a repitition , like grocery
            Command.write("\n Bakeries\n")
        for a,b,c in Bakeries:
            total = total + c
            Command.write(a + "\t \t \t" + str(b) +"\t \t \t" + str(c) +"\n")
        if Meats:
            Command.write("\n Meats\n")
        for a,b,c in Meats:
            total = total + c
            Command.write(a + "\t \t \t" + str(b) +"\t \t \t" + str(c) +"\n")
        if Frozenfoods:
            Command.write("\n Frozen foods\n")
        for a,b,c in Frozenfoods:
            total = total + c
            Command.write(a + "\t \t \t" + str(b) +"\t \t \t" + str(c) +"\n")
        if Seafoods:
            Command.write("\n Sea foods\n")
        for a,b,c in Seafoods:
            total = total + c
            Command.write(a + "\t \t \t" + str(b) +"\t \t \t" + str(c) +"\n")
        Command.write("\n TOTAL : \t \t \t \t \t \t " + str(total))  #we write the total
        Command.write("\n Thannks for comming !\n")
        sys.exit() #To end the loop
hub();