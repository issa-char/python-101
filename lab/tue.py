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

print("the possible name of your band is\n", band_name)

# tip bill generator/calculator
bill = input("what is your total bill? ")
split = input("how many people do you want to split the bill? ")
tip_perc = input("what percentage tip would like to give? ")

tip = ((int(tip_perc) * int(bill)) / 100)
n_bill = int(bill) - tip
each = n_bill // int(split)
print("each person to pay:", each)

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
    print("your bmi is " + str(bmi) + "kgm2 indicating obese")
elif(bmi < 18.5):
    print("your bmi is " + str(bmi) + "kgm2 indicating underweight")
else:
    print("your bmi is " + str(bmi) + "kgm2 indicating normal weight")
