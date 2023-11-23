# John's code

# client’s name, burger’s name, time of the day, and the total bill

# Name of the client number 10
# The client with the longest name
# Top three most selling burgers (based on the number of burgers)
# Top three best clients (highest bills)
# Name of the client with the second-to-last lowest bill
# Busiest hour of the day (number of clients)
# Best hour of the day (sales)
# Total sales on the day

class Client:
    def __init__(self, name, burger, time, total):
        self.name = name
        self.burger = burger
        self.time = time
        self.total = total

def burger_selection():
    print("1.cheeseburger, 2.hamburger, 3.double_double, 4.big mac, 5.baconator")
    burger = input('What kind of burger would you like: ')
    while burger not in ('1','2','3','4','5'):
        burger = input("Invalid selection, please try again\n")
    return burger

def main():
    customers = []
    for i in range(3): # eventually change this to 30 to add all customers
        name = input('Customer name: ')
        burger = burger_selection()
        time = 12 #change this to input
        total = 13 #eventually figure out a way to get the total better


    customer = Client(name, burger, time, total)
    customers.append(customer)
    # loop to check if shit is working 
    # for customer in customers:
    #         print(f"Name: {customer.name}, Burger: {customer.burger}, Time: {customer.time}, Total: {customer.total}")
main()
