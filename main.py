# Everyone's Code

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

    total = sum(prices[int(burger)] for burger in burger_selections)
    bills.append(total)
    return total








# function to call for the 10th customer 
def tenth_customers(customers):
    if len(customers) >= 10:
        return customers[9].name
    else:
        return "There are less than 10 customers."


def main():
    customers = []
    for i in range(30): # eventually change this to 30 to add all customers
        name = input('Customer name: ')
        burger = burger_selection()
        time = order_time()
        total = item_prices(burger, bills)
        print(f"{name}'s bill adds up to {total}")
    

        customer = Client(name, burger, time, total)
        customers.append(customer)

        continue_adding = input("Do you want to add another customer? (yes/no): ").lower()
        if continue_adding != "yes":
            break
        
        
    tenth_customer_name = tenth_customers(customers)
    print(f"The name of the 10th customer is: {tenth_customer_name}")
        
            # loop to check if shit is working 
    # for customer in customers:
    #         print(f"Name: {customer.name}, Burger: {customer.burger}, Time: {customer.time}, Total: {customer.total}")











main()
