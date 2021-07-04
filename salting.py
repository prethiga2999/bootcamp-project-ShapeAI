import hashlib
import os

users = {} 

# Add a user
username = input("Enter the new username : ") # The users username
password = input("Enter the new password : ") # The users password

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('md5', password.encode('utf-8'), salt, 100000)
users[username] = { # Store the salt and key
    'salt': salt,
    'key': key
}

# Verification
username = input("Enter the new username : ")
password = input("Enter the new password :")

salt = users[username]['salt'] # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('md5', password.encode('utf-8'), salt, 100000)

if key != new_key:
    print("Password is not correct") 
else:
    print("Password is correct")
