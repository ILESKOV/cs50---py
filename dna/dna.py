import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:  # Check if there are exactly 3 arguments provided (script name, database file name, and sequence file name)
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    # Read database file into a variable
    with open(sys.argv[1], "r") as database_file:  # Open the first argument as a file in read mode
        database_reader = csv.reader(database_file)  # Create a CSV reader object
        database = [row for row in database_reader]  # Read each row from the CSV file and store it in a list

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:  # Open the second argument as a file in read mode
        sequence = sequence_file.read()  # Read the contents of the file and store it in a string

    # Get the STRs from the header of the database file
    headers = database[0]  # Get the first row (header) of the database
    str_names = headers[1:]  # Get all the headers except the first one, which is the person's name

    # Find longest match of each STR in DNA sequence
    # Use a dictionary comprehension to store the longest match of each STR in the DNA sequence
    str_counts = {header: longest_match(sequence, header) for header in str_names}

    # Check database for matching profiles
    for row in database[1:]:  # Loop through each row in the database (excluding the header row)
        name = row[0]  # Get the name of the person from the first column of the row
        # Use a dictionary comprehension to create a dictionary of the STR counts for this person from the database
        str_counts_in_database = {str_name: int(count) for str_name, count in zip(str_names, row[1:])}
        if str_counts_in_database == str_counts:  # If the STR counts in the database match the STR counts in the DNA sequence, print the person's name and exit the script
            print(name)
            return

    print("No match")  # If no match is found in the database, print "No match"


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    subsequence_length = len(subsequence)
    max_count = 0
    count = 0
    i = 0
    while i < len(sequence):  # Loop through each character in the sequence
        # Get the substring starting from the current position with the same length as the subsequence we are looking for
        subseq = sequence[i:i+subsequence_length]
        if subseq == subsequence:  # If the substring matches the subsequence, increment the count and move to the next potential match
            count += 1
            i += subsequence_length
        else:  # If the substring doesn't match the subsequence, update the maximum count and reset the count to zero
            max_count = max(max_count, count)
            count = 0
            i += 1
    return max(max_count, count)  # Return the maximum count of consecutive subsequence matches found in the sequence


if __name__ == '__main__':
    main()  # Call the main function if the script is run directly, but not if it is imported as a module
