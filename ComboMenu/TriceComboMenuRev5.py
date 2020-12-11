#typically at the very top you will create the global variables 

def yayNayCheck(q,s):   #taken from my mad lib, this function checks whether or not the user inputs a letter, and if they don't, ask the user again for a letter
    while True: 
        if s == "yay" or "nay": #while True, if the user's input is yay or nay, move on to the next block of code
                break
        s=input(q)      #if the user's input is not a letter, ask the user once again for a letter
    return s

orderList = []
totalList = []
subtotalList = []
mainCourse = ["krabby patty","double krabby patty","triple krabby patty","krabby meal",
"double meal","triple meal","salty sea dog","footlong","golden loaf"]
mainPrice = [1.25,2.00,3.00,3.50,3.75,4.00,1.25,2.00,2.00]
#list.append(item)
while True:
    order = []
    subtotal = 0                       #accumulative variable
    sandwhichSelected=False         #flag variable
    beverageSelected=False
    friesSelected=False

    print("""
    Ahoy, me matey! Welcome aboard the Krusty Krab! What kinda grub for me hungry sailor?
       
       ╔══════════════════════════════════════════════════════════╗
       ║  ╔═══  ╔══╗  ║   ║   ╔══  ║ ║   ╔═══   ╔══╗  ║  ║  ║     ║
       ║  ║ ═╗  ╠══╣  ║   ║   ╠══  ╚╦╝   ║ ═╗   ╠═╣╗  ║  ║  ╠══╗  ║
       ║  ╚══╝  ║  ║  ╚══ ╚══ ╚══   ║    ╚══╝   ║  ║  ╚══╝  ╚══╝  ║
       ║ KRABBY PATTY......  $1.25          KRABBY MEAL.... $3.50 ║
       ║     w/sea cheese..  $1.50          DOUBLE MEAL.... $3.75 ║
       ║ DOUBLE KRABBY PATTY $2.00          TRIPLE MEAL.... $4.00 ║
       ║     w/sea cheese... $2.25          SALTY SEA DOG.. $1.25 ║
       ║ TRIPLE KRABBY PATTY $3.00          FOOTLONG....... $2.00 ║
       ║     w/sea cheese... $3.25          GOLDEN LOAF.... $2.00 ║
       ║                                        w/sauce.... $2.50 ║
       ║ CORAL BITS                                               ║
       ║ Small.............. $1.00                                ║
       ║ Medium............. $1.25          KELP SHAKE..... $2.00 ║
       ║ Large.............. $1.50              SEAFOAM SODA      ║
       ║                                    Small.......... $1.00 ║
       ║ KELP RINGS......... $1.50          Medium......... $1.25 ║
       ║     salty sauce.... $0.50          Large.......... $1.50 ║
       ╚══════════════════════════════════════════════════════════╝
    """)
    

    sandwhich = input("Arr! What be yer main grub today?: ").lower()
    
    for i in range(len(mainCourse)):
        if (sandwhich == mainCourse[i]): #          another valid method for the discount
            sandwhichSelected=True
            subtotal += mainPrice[i]
    order.append(sandwhich)        
        
    if "meal" in sandwhich:
        
            
        order.append(sandwhich)   #appending adds to the bottom of the list
        #print(sandwhich)

    if "meal" not in sandwhich:
        beverage  = yayNayCheck("Ya got barnacles in yer brain? Lemme dumb it down fer ya: D'ya need a drink?: ",input("Do ye need some fluids fer ye ship?. Yay or nay, matey: ").lower())
        if beverage == "yay":
            beverageSelected=True
            beverage= input("Would ye like the seafoam soda or the kelp shake, matey?: ").lower()
            #print("you said ",beverage, " drink.")  #print(string,string,string,string)
            if beverage=="seafoam soda":
                beverage=input("What size for yer soda?: ").lower()
                if beverage == "small":
                    subtotal += 1.00
                elif beverage=="medium":
                    subtotal += 1.75
                elif beverage=="large":
                    subtotal += 2.25
            order.append(beverage)
            if beverage == "kelp shake":
                subtotal += 2.00
        order.append(beverage)



        #iteration 3 asking for fries
        fries = yayNayCheck("D'ya need a translator, landlubber? Yay or nay?: ",input("Do ye need coral bits or kelp rings fer yer grumbly tummy? Yay or nay, sailor: ").lower())
        if fries =="yay":
            fries = input("Ye need coral bits or kelp rings, matey?: ").lower()
            if fries == "coral bits":
                fries = input("What size o'bits for ye?: ")
                friesSelected=True
                if (fries == "small"):
                    subtotal = subtotal + 1
                elif (fries == "medium"):
                    subtotal = subtotal + 1.25
                elif (fries == "large"):
                    subtotal += 1.50
            if fries == "kelp rings":
                if yayNayCheck("It's sauce. Yay or nay?: ",input("D'ya need salty sauce, sailor? Only 50 cents more! Yay or nay: ").lower()) == "yay":
                    subtotal += 2.00
            else:
                    subtotal += 1.50
        order.append(fries)

    # #iteration 4
    # #if you do not convert input to int() it will be a sequence or a string
    # ketchup=int(input("How many ketchup packets would you like? "))
    # subtotal+=ketchup*.25
    # order.append(ketchup)
    # #but you could combine the top two lines into one

    # if(sandwhichSelected and beverageSelected and friesSelected):     #and looks for 2 true statements
    # #if variable==true   AND variable==true   AND variable==true
    #     subtotal-=1



    #print("You're total is",total)

    '''
    print("You ordered a " + sandwhich + " sandwich ")
    print("You ordered a",sandwhich,"sandwich")
    print(sandwhich + "sandwich")
    print(beverage + "beverage")
    '''

    #print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of {4}'.format(sandwhich,beverage,fries,ketchup,total))
    
    total = 1.07*subtotal       #allowing the program to take in the total from the subtotal
    orderList.append(order)     #order master list; allows the program to print out all the orders 
    totalList.append(total)     #total master list; allows the program to print out the final total for
                                    #each order
    subtotalList.append(subtotal)   #subtotal master list; allows the program to print out the final
                                        #subtotal for each order
    print(orderList)
    print(f"Yar! Ye have {len(orderList)} orders! Here they be: ")
    for i in range(len(orderList)):
        #for each of the orders, print whats in each of the orders
        print(f'''
        Order {i+1} is: 
        {orderList[i][0]} ,
        {orderList[i][1]} drink,
        {orderList[i][2]} side,
        
        Yer subtotal be: ${round(subtotalList[i],3)}
        Yer tax amount was: ${round((totalList[i]*0.07),2)}
        Yer total be: ${round(totalList[i],2)}
        ''')
    if yayNayCheck("Answer the question, ye slimy dog! Yay or nay?: ",input("D'ya need anything else, matey? Yay or nay: ")).lower() == "nay":
        print(f"Your final total will be: ${round(sum(totalList),3)}.")
        break
    

#print('${:,.2f}'.format(total))  #string formatting