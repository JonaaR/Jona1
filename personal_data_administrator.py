from validators import input_bounded_integer, input_postal_code, input_string
import csv

person = {}








prompt = "Please choose which aspect to edit: (d)ay of birth, (m)onth of birth, (y)ear of birth, (p)ostal code, (l)ength, (n)ame (or enter 'q' to quit): "


while True:

    aspect = input(prompt)



    match aspect.casefold()[:1]:

        case 'd':

            print(input_bounded_integer("Please enter day of birth (Enter 'q' to quit): ", "day of birth", 1, 31))

        case 'm':

            print(input_bounded_integer("Please enter month of birth (Enter 'q' to quit): ", "month of birth", 1, 12))

        case 'y':

            print(input_bounded_integer("Please enter year of birth (Enter 'q' to quit): ", "year of birth", -5000, 2021))

        case 'l':

            print(input_bounded_integer("Please enter length (Enter 'q' to quit): ", "length", 0, 60))

        case 'n':

            print(input_string("Please enter your Name (Enter 'q' to quit): "))

        case 'p':

            list_of_postal_codes = [1000 + 10 * i for i in range(1, 24)]

            print(input_postal_code("Please enter postal code (Enter 'q' to quit): ", *list_of_postal_codes))

        case 'q':
            with open('people.csv', 'w', newline='', encoding="UTF-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(["Vorname", "Nachname", "Alter", "Adresse", "PLZ", "Ort"])

            break
