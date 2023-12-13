# python code to switch the value of two numbers
a = input("enter a number: ")
b = input("enter second number: ")

a, b = b, a

print(a)
print(b)

# switching the common way, like in C
c = a
a = b
b = c

print(a)
print(b)

# band name generator (concatenates two strings)
print("welcome to the band name generator, welcome!")
city = input("what is the name of the city you grew up in ? \n")
pet = input("what is the name of your pet ?\n")
band_name = city + " " + pet

print(f"the possible name of your band is: {band_name}")

# tip bill generator/calculator
bill = input("what is your total bill? ")
split = input("how many people do you want to split the bill? ")
tip_perc = input("what percentage tip would like to give? ")

tip = ((int(tip_perc) * int(bill)) / 100)
n_bill = int(bill) - tip
each =round(n_bill / int(split), 2)
print(f"each person to pay: {each}")

# adds the digits in a 2-digit number
num = input("enter a two digit number: ")
sum = int(num[0]) + int(num[1])
print(sum)


# calculate your BMI (body mass index)
# BMI is the result of weight(kg)/height(m2)
# If bmi == 18.5 - 25, obese bmi > 30, underweight < 18.5
height = input("what is your height in m? ")
weight = input("how much do you weight in kg? ")
bmi = int(weight) // (float(height) ** 2)

if( bmi > 30):
    print(f"your bmi is {bmi}kgm2 indicating obese")
elif(bmi < 18.5):
    print(f"your bmi is {bmi}kgm2 indicating underweight")
else:
    print(f"your bmi is {bmi}kgm2 indicating normal weight")
# this program calculates the time you have left assuming you live until 90yrs
# the result is the amount of days, weeks, and months
print("welcome to the amount of lives you have left to reach 90")
age = input("what is your current age: ")
rem = 90 - int(age)
days = 365 * rem
months = 12 * rem
weeks = months * 4

print(f"you have {rem} yrs to live, which is: {months} months, {weeks} weeks, and {days} days")
# determine if number is odd or even
num = input("enter a number: ")
if(int(num) // 2 > 0):
    print("it's a odd number")
else:
    print("its not an odd number")
print("welcome to the treasure hunt Island")
print("Your mission is to locate the treasure and return it to the mainland")
dir = input("you are at a crossroad where do you want to go")
if(dir == 'left'):
    action= input("you come to a lake. There is an Island in the middle. Type 'swim' or 'wait'")
    if(action == 'swim'):
        print("game over you were bit by a shark")
    elif(action == 'wait'):
        door = input("you arrive unarmed. There is a house with three door: 'red', 'yellow', and green', choose one")
        if(door == 'red'):
            print("a room filled with fire, game over!")
        elif(door == 'yellow'):
            print("a room filled water, game over")
        elif(door == 'green'):
            print("game over you found the treasure")

