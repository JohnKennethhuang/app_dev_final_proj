# Toms Crazy Scattered thoughts

# What did I do -

# Left notes for myself explaining whats going on 
# tabbed up the append in main due to it only adding the last customer to the list





# client’s name, burger’s name, time of the day, and the total bill

# Name of the client number 10
# The client with the longest name
# Top three most selling burgers (based on the number of burgers)
# Top three best clients (highest bills)
# Name of the client with the second-to-last lowest bill
# Busiest hour of the day (number of clients)
# Best hour of the day (sales)
# Total sales on the day

# No more than 30 clients per day 
# 5 types of borgers 
# 11:00 am to 10:00 pm 

# To Do List - 
# make sure to imput verify the yes/no of if you want another burger
# Create a question asking if there is another order 


class Client:
    def __init__(self, name, burger, time, total):
        
        # Note to self classes are cool ->
        self.name = name
        self.burger = burger
        self.time = time
        self.total = total

# Function changed to allow customers to add multiple items to their order
# and to confirm if they are finished and if not they can add more         
 
def burger_selection():
    print("1.cheeseburger, 2.hamburger, 3.double_double, 4.big mac, 5.baconator")
    selections = [] 

    while True:
        burger = input("Enter the number of the burger you would like to add to your order\nONE NUMBER AT A TIME: ")

        if burger in ("1", "2", "3", "4", "5",):
            selections.append(burger)
        else:
            print("Invalid selection, please try again.\n")
        
        more = input("Would you like to add another burger ot your order? (yes/no): ")
        if more.lower() != "yes":
            break 

    return selections 

def order_time():
    while True:
        time_input = input("Enter the time of the order (HH:MM, 24-hour format): ")

# checks for time format 

        if len(time_input) == 5 and time_input[2] == ":":
            if len(time_input) == 5 and time_input[2] == ":":
                hours = time_input[:2]
                minutes = time_input[3:]

                if hours.isdigit() and minutes.isdigit():
                    hours, minutes = int(hours), int(minutes)
# checks if time is within 11 - 10 or 11 to 22

                    if 11 <= hours <= 22 and 0 <= minutes < 60:
                        return time_input
        print("Invalid time or format. Please enter enter time in HH:MM format, between 11:00 and 22:00.")

def item_prices(burger_selections):
    prices = {
        1: 5.99,
        2: 6.99,
        3: 7.99,
        4: 8.99,
        5: 9.99
    }

    total = sum(prices[int(burger)] for burger in burger_selections)
    return total 



def main():
    customers = []
  
    
    
    
    for i in range(3): # eventually change this to 30 to add all customers
        name = input('Customer name: ')
        burger = burger_selection()
        time = order_time()
        total = item_prices(burger)
        print(f"{name}'s bill adds up to {total}")
        # Brought these two up one indentation because what would happen is that because it fell out of the loop
        # only the last customer would be appended 
        customer = Client(name, burger, time, total)
        # Because each item in the list falls into the class Client, it "stores" states / attributes. tbh the variable names did not need to be the same yadayadayada
        # because by setting the variable customer to the class client we save the states / attributes (name,burger,time,total) to it. 
        customers.append(customer)

    # loop to check if shit is working 
    #for customer in customers:
        #print(f"Name: {customer.name}, Burger: {customer.burger}, Time: {customer.time}, Total: {customer.total}") 
        
    # I want to return the list so we can leave this as a function because it is complex as it is, so that we can do the other half with other functions 
    return customers

# ------------------------------------------------------------------------------------------------------------------
# visualy seperating the two parts of the project ( Im stupid ) 
# From this point on I set the list created by returning customers from main to finalList

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
    print ("The longest customer name of the shift is",currentChamp,"\nWith names of the same lengh being: ",otherChamps)
    
            
        

# Callign main and setting final List to what main returns which is the list of all the customers. Each entry in the list is an object in the class Client



final_list = main()

get_longest_name(final_list)


