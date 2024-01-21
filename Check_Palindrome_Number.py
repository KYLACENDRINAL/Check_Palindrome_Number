# Write a program to check if the given number is a palindrome number

# pseudocode

# Define the function of palindrome
def palindrome(number):
    original_number=number
    reversed_number=int(str(number)[::1])

    if original_number==reversed_number:
        return f"Original number{original_number}\nYes. Given number is palindrome number"
    else:
        return f"Original number{original_number}\nNo. GIven number is not a palindrome number"
    
    
# Give values
value1=palindrome(121)
value2=palindrome(125)

