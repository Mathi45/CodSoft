def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2

print("Please select any of the options: \n" "1. ADD\n" "2. SUBTRACT\n" "3.MULTIPLY\n" "4.DIVIDE\n")

select = int(input("Select from operations 1,2,3,4:"))

num_1 = int(input("Enter the 1st number:"))
num_2 = int(input("Enter the 2nd number:"))

if select ==1:
    print(num_1, "+" , num_2, "=", add(num_1,num2))
elif select==2:
    print(num_1, "-", num_2, "=", subtract(num_1,num_2))
elif select==3:
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))
elif select==4:
    print(num_1, "/", num_2, "=", divide(num_1,num_2))
else:
    print("Invalid Input")
    
