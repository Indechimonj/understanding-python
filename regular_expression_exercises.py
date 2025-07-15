#This is a python exercise to showcase the use of regular expressionsRegular expressions are a powerful tool for matching patterns in strings.
import re
# Exercise 1: Validate 10-digit phone numbers
def validate_phone_number(phone_number):# Function to validate a phone number
    pattern = r'^\d{3}-\d{3}-\d{4}$'# Define the pattern for a valid phone number
    # The pattern matches a string that starts with 3 digits, followed by a hyphen
    if re.match(pattern, phone_number):# Check if the phone number matches the pattern
        return True
    else:
        return False
print (validate_phone_number('123-456-7890'))  # Should return True

# Exercise 2: Extract email addresses from a text
def extract_email_addresses(text):# Function to extract email addresses from a text
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'# Define the pattern for a valid email address
    # The pattern matches a string that contains an email address
    return re.findall(pattern, text)# Return a list of all email addresses found in the text
print(extract_email_addresses('Goodmorning, my email is imonjesamue@gmail.com and my backup is indechewagwan89@gmail.com'))  # Should return ['
 