while True:
    try:
        x=input("Type a number here: ")
        x=int(x)
        if x > 0:
            print(x)
        else:
            print(-x)
    except ValueError:
        if x == "":
            print("Please enter a number.")
        else:
            try:
                x=float(x)
                if x > 0:
                    print(x)
                else:
                    print(-x)
            except ValueError:
                print("A number like 11350.6, -12, 5.1476, or -241.7. ")
