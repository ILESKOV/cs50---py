import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Persy", "Ron"]

name = input("Name: ")

                  # for n in names:
if name in names: #     if name == n:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)