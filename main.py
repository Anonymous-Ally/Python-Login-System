from user import User # Import the class User from ./user.py.
import os # Import os to be able to use a function to clear the screen.
import time # Import time to be able to use a function to wait.

# Here you can customize your list of users.
users = [User(hash('123456'), 'John'), User(hash('qwerty'), 'Jane')]

# Defining a function to check the password and return the User if the passwords match.
def check_password(y):
  for loop in users:
    if loop.password == y:
      return loop
  return None

def screen_clear():
  # Clear the screen depending on what os type is being used.
  if os_type == 'nt': # If the os is Windows use cls to clear the screen.
    os.system('cls')
  elif os_type == 'posix': # If the os is Unix-like (Linux, MacOS, etc.) use clear to clear the screen.)
    os.system('clear')

# Store which type of os the user is using (Useful later).
os_type = os.name

# Create a variable for the while loop.
looping = True

# Create a while loop to loop back to the input if the password is incorrect.
while looping: # Check if looping is equal to 'True'.
  # Store an input from the user as a string.
  x = input('Password: ')
  
  # Store the hash of the input we stored.
  y = hash(x)
  
  # Store the result of the function in a variable.
  Password = check_password(y)

  # Clear the screen.
  screen_clear()
    
  # Print the name of the user if the passwords match.
  if Password: # Checking whether the password is correct.
    print(Password.name)
    looping = False # Set looping to False to break the loop.
  else: # Printing incorrect password and returning to the password input if the password is incorrect.
    print('Incorrect password')
    time.sleep(1) # Wait 1 second.
    screen_clear() # Clear the screen.
