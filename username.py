import json

filename = 'username.json'
name = ''

# Check for a history file
try:
    with open(filename, 'r') as r:
        try:
            data = json.load(r)
            name = data.get('name', '')
        except json.decoder.JSONDecodeError:
            print("Error loading JSON data")

except FileNotFoundError:
    print("First-time login")
    # Create the file if it doesn't exist
    with open(filename, 'w') as f:
        json.dump({'name': name}, f)

# If the user is in the history file, welcome them by name
if name != '':
    print('Welcome back, ' + name + '!')

# If the user is not on the list, ask their name
else:
    name = input("Hi! What's your name?")
    print('Welcome, ' + name + '!')
    # Save the user into the history file
    with open(filename, 'w') as f:
        json.dump({'name': name}, f)