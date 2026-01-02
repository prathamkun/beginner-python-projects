def main():
    print("This program converts US dollars to Pounds Sterking")
    print()


    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")

convert_to_pounds = lambda dollars: dollars * 0.74 #on 1st january it was 0.74 pound sterling 

main()
