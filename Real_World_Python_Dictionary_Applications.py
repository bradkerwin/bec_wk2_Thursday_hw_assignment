restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu.update({'Beverages': {'Water': 1.00, 'Coke': 2.50}}) # This adds the subdictionary 'Beverages' to the main dicitonary 'restaurant_menu'. The subdicitonary containes 2 key-value pairs, 'Water': 1.00 and 'Coke': 2.50.
print(restaurant_menu) # Prints our new dicitonary which consists of: {'Starters': {'Soup': 5.99, 'Bruschetta': 6.5}, 'Main Course': {'Steak': 15.99, 'Salmon': 13.99}, 'Desserts': {'Cake': 4.99, 'Ice Cream': 3.99}, 'Beverages': {'Water': 1.0, 'Coke': 2.5}}.

restaurant_menu.update({'Steak': 17.99}) # Updates the value associated with the key 'Steak' from 15.99 to 17.99.
print(restaurant_menu) # Prints our new dictionary with the updated value for the key 'Steak'.

del restaurant_menu['Starters']['Bruschetta'] # Using the del function to access the subdictionary 'Starters' and delete the key-value pair 'Bruschetta': 6.50.
print(restaurant_menu) # Prints out our new dictionary with the key-value pair 'Bruschetta': 6.50 removed.