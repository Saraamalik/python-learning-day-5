while True:
    try:
        age = int(input("Enter your age"))
        print("your age is:", age)
        break
    except ValueError:
        print("Please enter correct number")
