import hashlib

print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)

# SHA256
str = input("Enter the string for SHA256 : ")

result = hashlib.sha256(str.encode())
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")

# SHA384
str = input("Enter the string for SHA384 : ")

result = hashlib.sha384(str.encode())
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")


# SHA1
str = input("Enter the string for SHA1 : ")

result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
