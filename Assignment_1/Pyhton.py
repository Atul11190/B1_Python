print("string operation")
#input a user  first name and last name
first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
#reverse order
print(last_name+" "+first_name)
print("-------------------------")
print("-------------------------")
print("numeric data type converstion")
#converted data type(integer,float,complex)
# Get user input as a string
num= input("Enter a number: ")
# Convert to different numeric types
int_value = int(num)
float_value = float(num)
complex_value = complex(num)
# Display the converted values
print(f"Original Value: {num}") #origial value for user input number
print(f"Integer: {int_value}") #integer data type
print(f"Float: {float_value}") #float data type
print(f"Complex: {complex_value}") #complex data type
print("-------------------------")
print("-------------------------")
print("calculated area")
#The area of rectangle
# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate the area of the rectangle
area = length * width
# Display the area
print(f"The area of the rectangle is: {area}")
print("-------------------------")
print("-------------------------")
print("format and print function")
#using the format method
# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate the area of the rectangle
area = length * width
# Display the area formatted to two decimal places
print("The area of the rectangle is: {:.2f}".format(area))
print("-------------------------")
print("-------------------------")
print("calculate average")
#Calculate average
# Get user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Calculate the average
average = (num1 + num2 + num3) / 3
# Display the average using the % method
print("The average of the three numbers is: %.2f" % average)
print("-------------------------")
print("-------------------------")
print("condition flow")
#if statement and loop
# Ask the user for a number
num = float(input("Enter a number: "))
# Determine if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    print("loop")
    # Loop through numbers from 1 to 10
    for i in range(1, 11):
        print(i)
print("-------------------------")
print("-------------------------")
print("relational and logical operator")
    #check num is odd ,even or one of each using relational and logical operator
    # Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
# Check if both numbers are odd
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
# Otherwise, one is even and the other is odd
else:
    print("first number is even, and the other is odd.")
print("-------------------------")
print("-------------------------")
#for loop and bitwise operator
# Input integer from the user
num = int(input("Enter an integer: "))
binary = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]
# Print the results
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")