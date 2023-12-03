# Everyone's Code

# client’s name, burger’s name, time of the day, and the total bill


# Name of the client number 10 - done 
# The client with the longest name - get from thomas 
# Top three most selling burgers (based on the number of burgers) 
# Top three best clients (highest bills)
# Name of the client with the second-to-last lowest bill - done 
# Busiest hour of the day (number of clients)
# Best hour of the day (sales)
# Total sales on the day - done 

# No more than 30 clients per day 
# 5 types of borgers 
# 11:00 am to 10:00 pm 



# First we need to create clients which would contain their name, burger, time of order, and total bill
# We need something to hold these values so we create classes which hold information about each client 

# Then we need to ask for the client's name 


# Then we need to ask for the client's burger order 

# We can create a function for this
# Print a list of burgers that the customer can order ( Five Burgers only)
# Ask the customer what kind of burger they want, using numbers only 
# We need to store the information of what the customers ordered so using empty list
# We also need to ask if they want anything else. 
# If they say yes and loop back to asking what kind of burger they want.
# else if say no then we break out of the loop then we ask time 

# I realized that no doesn't have input validation so maybe fix that 



# Then we need to input the time of order 
# Limits set = The restaurant works from 11:00 am until 10:00 pm 
# set a variable for time and ask what time the order was. 
# input validation - lenght of the time which is (##:##) 5 
# set which which part of the time are hours and minutes to 
# have input validation within 11:00 and 10:00 pm 
# If the time is less than 11:00 am and the time is more than 10:00 pm say that it was an invalid time
# input validation - make sure the inputed values are integers 
# 




# then we need to grab the total bill for the order 
# We will use another function
# we will call the burger selection function to grab the string value that the customer ordered
# We will use a dictionary which gives a key-value pair 
# we assign the keys 1, 2, 3, 4, 5 
# to the value of each price 
# to grab the total we need to assign the variale total to the sum
# so it wouuld be total is equal to the sum of burger selected by the customer converted to the key value pairs




# Client's name, burger's name, time of day, and the total bill
# Create something to hold information of each client which would include the 4 above info.
# A class Client defines the attributes name, burger, time, and total bill
# Attributes are the data stored in Client 


# class hold information about each client. 
# a class is like a recipe. "What creates a client?"
# def __init__, initializes a new object with its initial values 
# self refers to the specific object 
# self = "this particular client"
# when a new client is made, '__init__' is automatically called to set up that client. 
# It takes the client's name, burger, time, and total, and saves them so that this particular client remeber these details




class Client:
    def __init__(self, name, burger, time, total):
        self.name = name
        self.burger = burger
        self.time = time
        self.total = total
    def burger_selection():
        print("1.cheeseburger($5.99)\n2.hamburger($6.99)\n3.double_double($7.99)\n4.big mac($8.99)\n5.baconator($9.99)")
        selections = []
        while True:
            burger = input("Enter the number of the burger you would like to add to your order (or 'done' to finish): ")
            if burger.lower() == 'done':
            
                break
            
            if burger not in ("1", "2", "3", "4", "5"):
                print(f'{burger} is an invalid selection, please try again')
                print("1.cheeseburger($5.99), 2.hamburger($6.99), 3.double_double($7.99), 4.big mac($8.99), 5.baconator($9.99)")
                continue
            selections.append(burger)
        return selections
        # burger = input("Enter the number of the burger you would like to add to your order: ")
        # while burger not in ("1", "2", "3", "4", "5",):
        #     print(f'{burger} is an invalid selection, please try again')
            # print("1.cheeseburger($5.99), 2.hamburger($6.99), 3.double_double($7.99), 4.big mac($8.99), 5.baconator($9.99)")
            # burger = input("Enter the number of the burger you would like to add to your order: ")

        # else:
        #     selections.append(burger)
        # more = input("Would you like to add another burger to your order? (yes/no): ")
        # while more.lower() not in ("yes", "no", "y", "n"):
        #     print("Invalid selection, please try again.")
        #     more = input("Would you like to add another burger to your order? (yes/no): ")
        # return selections 

   
# Function changed to allow customers to add multiple items to their order
# and to confirm if they are finished and if not they can add more         
 


# time input 

def order_time():
    while True:
        time_input = input("Enter the time of the order between 11:00 and 22:00. (HH:MM, 24-hour format): ")

# checks for time format 

        if len(time_input) == 5 and time_input[2] == ":":

            hours = time_input[:2]
            minutes = time_input[3:]

            if hours.isdigit() and minutes.isdigit():
                hours, minutes = int(hours), int(minutes)
# checks if time is within 11 - 10 or 11 to 22

                if 11 <= hours <= 22 and 0 <= minutes < 60:
                    return time_input
        print("Invalid time or format. Please enter enter time in HH:MM format, between 11:00 and 22:00.")



# a list of the prices for the burgers 
# Calculates the total cost of the burgers selected by the clients


# burger_selections is a parameter which means it goes to the 
# buger_selection function to grab contents needed for this function to work properly
# 
def item_prices(burger_selections, bills):
    prices = {
        1: 5.99,
        2: 6.99,
        3: 7.99,
        4: 8.99,
        5: 9.99
    }

    total = round(sum(prices[int(burger)] for burger in burger_selections), 2) #added a round function to round to 2 decimal places
    bills.append(total)
    return total








# function to call for the 10th customer 
def tenth_customers(customers):
    if len(customers) >= 10:
        return customers[9].name
    else:
        return "There are less than 10 customers."
    

# Function to get the longest name 

def get_longest_name (theRosta):
    currentChamp = ""
    otherChamps = ""
    secondaryChamp = ""
    for fighter in theRosta:
        currentContender = fighter.name
        if len(currentContender) > len(currentChamp):
            currentChamp = currentContender
            if len(currentContender) > len(secondaryChamp):
                otherChamps = ""
        elif len(currentContender) == len(currentChamp):
            secondaryChamp = currentContender
            otherChamps = otherChamps + "" + currentContender 
    print ("\nThe longest customer name of the shift was",currentChamp,"\nWith names of the same lengh being: ",otherChamps)



# Function for the most popular burgers

def mostPopularBurgers(customers):

    burgerOne = [0, "cheeseburger"]
    burgerTwo = [0, "hamburger"]
    burgerThree = [0, "doubledouble"]
    burgerFour = [0, "big mac"]
    burgerFive = [0, "baconator"]
    
    for client in customers:
        selection = client.burger
        for purchase in selection:
            if purchase == "1":
                burgerOne[0] = burgerOne[0] + 1
            elif purchase == "2":
                burgerTwo[0] = burgerTwo[0] + 1
            elif purchase == "3":
                burgerThree[0] = burgerThree[0] + 1
            elif purchase == "4":
                burgerFour[0] = burgerFour[0] + 1
            elif purchase == "5":
                burgerFive[0] = burgerFive[0] + 1                
            
        
    burgerChoices = [burgerOne, burgerTwo, burgerThree, burgerFour, burgerFive]
    burgerChoices.sort()
    
    print ("\nThe three most popular burgers were",burgerChoices[-1],"",burgerChoices[-2],"",burgerChoices[-3])
    
    
def highestBills (customer):
    
    Bills = customer 
    
    sorted(Bills, key = lambda Client: Client.total)
    
    print ("\nThe customers with the three highest bills are ! ") 
    
    if len(customer) > 0:
        print ((Bills[-1].name))
    if len(customer) >= 2:
        print ((Bills[-2].name))
    if len(customer) >= 3:
        print ((Bills[-3].name))



# Function for busiest hour of the day 
# between 11:00 and 22:00 

def bestNumberOfClients(customers):
    
    
    # initializes variables to keep track of count of each hour 
    amElleven = 0
    pmTwelve = 0
    pmOne = 0
    pmTwo = 0
    pmThree = 0
    pmFour = 0
    pmFive = 0
    pmSix = 0
    pmSeven = 0
    pmEight = 0
    pmNine = 0
    pmTen = 0
    
    # for loop to itterate over each client 
    
    for client in customers:
        # sets a variable to the time recorded in each client 
        purchaseHour = client.time
       
       #Grabbing the first and second character from the string that time comes out two and adding them together  
       
        first = purchaseHour[0]
        second = purchaseHour[1]
        hour = first + second 
        hour = int(hour)
        
        # basically a long winded way of adding a point to each of the counters 
        
        if hour == 11:
            amElleven = amElleven + 1 
        elif hour == 12:
            pmTwelve = pmTwelve + 1 
        elif hour == 13:
            pmOne = pmOne + 1 
        elif hour == 14:
            pmTw0 = pmTwo+ 1 
        elif hour == 15:
            pmThree = pmThree+ 1 
        elif hour == 16:
            pmFour = pmFour + 1 
        elif hour == 17:
            pmFive = pmFive + 1 
        elif hour == 18:
            pmSix = pmSix + 1 
        elif hour == 19:
            pmSeven = pmSeven + 1 
        elif hour == 20:
            pmEight = pmEight + 1
        elif hour == 21:
            pmNine = pmNine + 1 
        elif hour == 22:
            pmTen = pmTen + 1      
            
            
    # adding all the variables to a list 
    HOURS = [ "Elleven","Twelve","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    hourCounts = [amElleven,pmTwelve,pmOne,pmTwo,pmThree,pmFour,pmFive,pmSix,pmSeven,pmEight,pmNine,pmTen]
    
    currentChamp = 0 
    hourList = ""
    otherChamps = ""
    secondaryChamp = 0
    positionCounter = 0 
    
    for time in HOURS:    
        currentContender = hourCounts[positionCounter]
        if currentContender > currentChamp:
            currentChamp = currentContender
            hourList = time 
            if currentContender > secondaryChamp:
                otherChamps = ""
        elif currentContender == currentChamp:
            secondaryChamp = currentContender
            otherChamps = otherChamps + time + " "
        positionCounter = positionCounter + 1 
            
    print ("\nThe busiest hour of the day was ",hourList,"\nWith other equally as busy hours being: ",otherChamps)
    
    
    
    

def mostProfitableHour(customers):
    
    
    # initializes variables to keep track of count of each hour 
    amElleven = 0
    pmTwelve = 0
    pmOne = 0
    pmTwo = 0
    pmThree = 0
    pmFour = 0
    pmFive = 0
    pmSix = 0
    pmSeven = 0
    pmEight = 0
    pmNine = 0
    pmTen = 0
    
    # for loop to itterate over each client 
    
    for client in customers:
        # sets a variable to the time recorded in each client 
        purchaseHour = client.time
        clientTotal = client.total
       
       #Grabbing the first and second character from the string that time comes out two and adding them together  
       
        first = purchaseHour[0]
        second = purchaseHour[1]
        hour = first + second 
        hour = int(hour)
        
        # basically a long winded way of adding a point to each of the counters 
        
        if hour == 11:
            amElleven = amElleven + clientTotal 
        elif hour == 12:
            pmTwelve = pmTwelve + clientTotal 
        elif hour == 13:
            pmOne = pmOne + clientTotal 
        elif hour == 14:
            pmTw0 = pmTwo + clientTotal 
        elif hour == 15:
            pmThree = pmThree+ clientTotal 
        elif hour == 16:
            pmFour = pmFour + clientTotal 
        elif hour == 17:
            pmFive = pmFive + clientTotal 
        elif hour == 18:
            pmSix = pmSix + clientTotal
        elif hour == 19:
            pmSeven = pmSeven + clientTotal
        elif hour == 20:
            pmEight = pmEight + clientTotal
        elif hour == 21:
            pmNine = pmNine + clientTotal 
        elif hour == 22:
            pmTen = pmTen + clientTotal      
            
            
    # adding all the variables to a list 
    HOURS = [ "Elleven","Twelve","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    hourCounts = [amElleven,pmTwelve,pmOne,pmTwo,pmThree,pmFour,pmFive,pmSix,pmSeven,pmEight,pmNine,pmTen]
    
    currentChamp = 0 
    hourList = ""
    otherChamps = ""
    secondaryChamp = 0
    positionCounter = 0 
    
    for time in HOURS:    
        currentContender = hourCounts[positionCounter]
        if currentContender > currentChamp:
            currentChamp = currentContender
            hourList = time 
            if currentContender > secondaryChamp:
                otherChamps = ""
        elif currentContender == currentChamp:
            secondaryChamp = currentContender
            otherChamps = otherChamps + time + " "
        positionCounter = positionCounter + 1 
            
    print ("\nThe most profitable hour of the day is ",hourList,"\nWith other equally as profitable hours being: ",otherChamps)
        





def main():
    customers = []
    bills = []
    for i in range(30): # eventually change this to 30 to add all customers
        name = input('Customer name: ')
        burger = Client.burger_selection()
        time = order_time()
        total = item_prices(burger, bills)
        print(f"{name}'s bill adds up to {total}")
    

        customer = Client(name, burger, time, total)
        customers.append(customer)

        if len(customers) <30:    
            continue_adding = input("Do you want to add another customer? (yes/no): ").lower()
            if continue_adding in ("no", "n"):
                break
            elif continue_adding in ("yes", "y"):
                print("Welcome\n")
        #     more = input("Would you like to add another customer to your order? (yes/no): ")
        #     if continue_adding not in ("yes","y"):
            
        
    tenth_customer_name = tenth_customers(customers)
    print(f"The name of the 10th customer is: {tenth_customer_name}")
        
    total_sales = sum(bills)
    print(f"Total sales of the day: ${total_sales:.2f}")

    sorted_bills = sorted(customer.total for customer in customers)
    # sorted() arranges the total from each customer from lowest to highest. 
    #customer.total # we are taking the total attribute from the class into the variable
    if len(sorted_bills) >= 2:
        #Checking the length of the list in the sorted_bills has atleast 2. 
        second_to_last_bill = sorted_bills[-2]
        # finds the second to last bill using -2 index. -2 -1 0 1 2 or [0 1 2 3 4] (3 = -2)
        for client in customers:
            if client.total == second_to_last_bill:
                print(f"Client with the second to last lowest bill: {client.name}")
                break
    else:
        print("Not enough customers to find second to last lowest bill")
        
    # Calling function for longest name 
    
    get_longest_name(customers)
    
    bestNumberOfClients(customers)
    
    mostProfitableHour(customers)
    
    mostPopularBurgers(customers)
    
    highestBills(customers)




  
main()
