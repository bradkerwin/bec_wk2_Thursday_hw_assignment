service_tickets = {
    1: {"Customer": "Mark", "Issue": "Cannot connect to wi-fi", "Status": "open"},
    2: {"Customer": "Tom", "Issue": "Login not registering", "Status": "closed"},
    3: {"Customer": "Scott", "Issue": "App will not open", "Status": "open"}
} # Our main dictionary and the subdictionaries contained within.


def next_id(): # Creating a function that returns an id in order to make a new service ticket
    last_id = 0 # Our last_id starts at zero so that we can add 1 to it each time we create a new id for each new service ticket.
    for id in service_tickets.keys(): # Iterates over the keys in our dictionary service_tickets. 1 and 2 are the keys in this dictionary. 
        if id > last_id: # Checks if the id is greater than our last_id which starts with a value of 0. 
            last_id = id # Setting last_id equal to id.
    return last_id + 1 # This will add 1 to last_id every time so that each new ticket will be 1 higher than the previous.

def new_ticket(): # Creating a function that actually makes the new service tickets
    new_id = next_id() # Calling our next_id() function
    while True: # Creating a while loop so our code will run as long as our condition is met.
        customer = input("Please enter the customer name: \n") # Asks user for customer name to add to the key 'Customer'.
        issue = input("Please state the issue: \n") # Asks user for the customer's issue to add to the key 'Issue'.
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct? ") # Confirming the info that has been entered is correct.
        if correct == 'yes':
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'} # Accessing our new_id variable and adding our new subdicitionary with the ticket info to the dictionary service_tickets.
            break # Breaks out of the while loop.
        else: # In case the if statement's condition is not met. 
            continue # Goes back to the start of the loop.

def update_ticket(): # Creating a function to update the status of an existing ticket.
    while True: # Creating a while loop so our code will run as long as our condition is met.
        try: # try statement added to make sure the code runs without causing errors.
            key_to_update = int(input("Please enter the key for the ticket status you wish to update: ")) # Input converted to an integer as it would only except a string without the int() statement. This will prevent errors. 
            if key_to_update in service_tickets: # Iterating through the dictionary service_tickets to confirm the key entered by the user is found in the dictionary.
                service_tickets[key_to_update]['Status'] = 'closed' # Accessing the key 'Status' within the subdicitonary selected by the user and changing the value from 'open' to 'closed'. The subdictionary inputed by the user is contained within the main dictionary service_tickets.
                print(service_tickets[key_to_update])
                confirm_info = input("Is this correct? ") # Confirming user input.
                if confirm_info == 'yes':
                    break # Breaks out of the loop if user inputs 'yes'.
                else:
                    continue # Returns the user to the top if they do not input 'yes'.
            else: # Added if the user input is not found within the dictionary service_tickets.
                print("Invalid entry. Please try again. ")
                continue # Returns the user to the beginning of the loop.
        except: # except statement added so that errors are not caused if the user enters an invalid input.
            print("Please enter a valid number. ")
            continue # Returns the user to the beginning of the loop.

def main(): # Defining our main function that will call all of our existing functions and will run based on user input.
    while True: # Creating a while loop so our code will run as long as our condition is met.
        ans = input('''
Service Ticket Manager
Please select an option:                   
1- Open a new service ticket.
2- Update the status of an existing ticket to "closed".
3- Display all tickets.
4- Quit
''') # Multi-line string asking for user input.
        if ans == '1':
            new_ticket() # function to add a new ticket
        elif ans == '2':
            update_ticket() # function to add update an existing ticket
        elif ans == '3':
            print(service_tickets) # simply prints all existing tickets
        elif ans == '4':
            print("Thank you, have a good day!")
            break # Breaks out of the while loop.
        else: # Added if the user enters an invalid input.
            print("Please enter a valid entry.")
main() # Calling our main function.