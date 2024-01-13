#--------------imports
import sys
import csv
import requests
import datetime
import pandas as pd

#--------------main
def main():
    #check for correct command line arguments
    check_correct_args()

    #retrive data from an API
    data = get_api()

    #process the data by calculating the age of the characters
    for row in data:
        row["birthyear"] = char_age(row["birthyear"])

    #write the processed data to a CSV file
    with open(sys.argv[1] , "w") as file:
        writer = csv.DictWriter(file,fieldnames=["firstname","lastname","house","age"])
        writer.writerow({"firstname" : "firstname", "lastname" : "lastname" , "house" : "house" , "age" : "age"})
        for row in data:
            firstname,lastname = row["name"].split()
            writer.writerow({"firstname" : firstname, "lastname" : lastname , "house" : row["house"] , "age" : row["birthyear"]})

    #read the data from the CSV file using pandas and print it
    show= pd.read_csv(sys.argv[1])
    print(show)

    #enter a loop to search for a character's name untill user exits
    while True:
        x = input("Search the name of a character(or e to exit): ")
        print(search_name(x))

#--------------functions
def get_api():
    # Function to fetch data from the API
    output = []
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)

    if response.status_code == 200:
        characters = response.json()

        for character in characters:
            name = character['name']
            house = character['house']
            year_of_birth = character['yearOfBirth']

            # Filtering and processing the fetched data(drop the null data fields)
            if "" not in house or "None" not in str(year_of_birth):
                output.append({"name" : name , "house" : house , "birthyear" : year_of_birth})

    else:
        sys.exit(f"An error occurred: {response.status_code}")

    return output

def char_age(birthyear):
    # Function to calculate age based on birth year
    today = datetime.date.today()
    year = today.year
    age = year - birthyear
    return age


def check_correct_args():
    # Function to check if the correct command-line arguments are provided
    if len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    if len(sys.argv) <2 :
        sys.exit("Too few command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not CSV files")

def search_name(fname):
    # Function to search for a character's name
    fname = fname.lower()
    try:
        reader = csv.DictReader(open(sys.argv[1]))
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} CSV file Not Found")

    if fname == "e":
        sys.exit("mischief managed! 😁🐍")

    for row in reader:
        if fname == row["firstname"].lower():
            return row["firstname"] + " " + row["lastname"] + " house is " + row["house"]

    return "no character found"


# Checking if the script is being run as the main program
if __name__ == "__main__":
    main()
