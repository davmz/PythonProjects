"""
Name: David Montanez
Reason: Hello World
Created: July 9, 2021
Updated: July 9, 2021
"""
## Program
# Get user's email address
emailAddress = input("Enter email address: ").strip()

# Slice username
username = emailAddress[:emailAddress.index("@")]

# Slice domain name
domain = emailAddress[emailAddress.index("@") + 1:]

# Print email
print(f"\nUsername: {username}\nDomain: {domain}")
