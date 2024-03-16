while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number")

if age < 18:
    print("You are not eligible to vote.")
elif age == 18 or age > 18:
    print("You are eligible to vote.")
