import csv

with file = open("phonebook.csv", "a") as file # it will automatically close the file at the end

name = input("Name: ")
number = input("Number: ")

writter = csv.DictWritter(file, filenames=["name", "number"])
writter.writerow({"name": name, "number": number})
