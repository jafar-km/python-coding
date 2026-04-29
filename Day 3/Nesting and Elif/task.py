print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age?"))
    if age <= 12:
        print("Pay $5")
    elif age <=18:
        print("pay $7")
    else:
        print("Pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
