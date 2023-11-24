# John's Code 


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


    customer = Client(name, burger, time, total)
    customers.append(customer)
    # loop to check if shit is working 
    # for customer in customers:
    #         print(f"Name: {customer.name}, Burger: {customer.burger}, Time: {customer.time}, Total: {customer.total}")
main()
