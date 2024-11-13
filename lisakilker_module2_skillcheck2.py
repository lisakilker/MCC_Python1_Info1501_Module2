#Program checks if a user input is between 0-100
def main():
    #Prompt the user for input
    user_input = input("Please enter a number: ")

    try:
        #Convert the input to an integer
        test = int(user_input)

        #Check if the number is between 0 and 100
        if test > 100:
            print("The Entered Number Is Too Large.")
      
        elif test < 0:
            print("No Negative Numbers Allowed.")

        else:
            print("The Entered Number is Acceptable")

    #Prints the error if the user enters something other than a number
    except ValueError:
        print("That is not a valid number. Please enter a valid number.")
        main()

#Runs the program
main()
