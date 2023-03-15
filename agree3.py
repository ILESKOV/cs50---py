s = input("Do you agree? ")

s = s.lower()
if s in ["yes", "y"]:
    print("Agreed")
elif s in ["not", "n"]:
    print("Not agreed")