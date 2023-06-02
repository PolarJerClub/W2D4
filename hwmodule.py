import math

def sqft():
        b = int(input("\nTell me the length of your house: "))
        d = int(input("Lemme get that width while you're at it: "))
        area = b * d
        print("The area of your house is: " + str(area) + " square feet.\n")

    

def circle():
    c = int(input("\nWhat would you like your circle radius to be?: "))
    circumference = 2 * math.pi * c
    print("The circumference of your circle is: " + str(circumference) + "\n")


while True:
    a=input("Welcome to your calculator of houses and circles! Where would you like to start? House or Circle: ")
    if a.lower()=='house':
        e=input("\nWhy couldn't the Italian get into his house?: ")
        if e.lower() == "He had gnocchi":
            print("WAHOOOOOO")
        else:
            print("He had gnocchi")
        sqft()
    elif a.lower() == 'circle':
        b=input("\nDo you know who invented the circle?: ")
        if b.lower == 'sircumference':
            print("You sure do know your history!")
        else:
            print("Why it's SirCumference, of course!")
        circle()
    elif a.lower()=='quit':
        print("OK. Be that way")
        break
    else:
        print("Type House or Circle dude.")