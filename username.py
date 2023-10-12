import json

filename = 'username.json'
name = {'name': ''}

# Check for a history file
try:
    with open(filename, 'r') as r:
        file_contents = r.read()
        if file_contents:
            # Load the user's name
            data = json.loads(file_contents)
            name = data.get('name', '')
        else:
            # When the file exists but is empty
            print("First-time login")

except FileNotFoundError:
    print("First-time login")
    # Create the file if it doesn't exist
    with open(filename, 'w') as f:
        json.dump({'name': name['name']}, f)

# If the user is in the history file, welcome them by name
if name != '':
    print('Welcome back, ' + name + '!')

# If the user is not on the list, ask their name
else:
    name['name'] = input("Hi! What's your name?")
    print('Welcome, ' + name['name'] + '!')
    # Save the user into the history file
    with open(filename, 'w') as f:
        json.dump({'name': name['name']}, f)