import string
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input=input("Enter the number of characters:")

while True:
    try:
        characters_numbers = int(user_input)
        if characters_numbers < 8:
            print("your number should be atleast 8")
            user_input = input("please, enter your number again:")
        else:
            break
    except:
        print("please, Enter numbers only")
        user_input=input("enter the number of characters:")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(characters_numbers *(30/100))
part2=round(characters_numbers *(20/100))

result=[]

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)

password = "".join(result)
print("strong password:", password)
