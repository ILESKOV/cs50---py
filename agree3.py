s = input("Do you agree? ")

if s.lower() in ["yes", "y"]:
    print("Agreed")
elif s.lower() in ["not", "n"]:
    print("Not agreed")