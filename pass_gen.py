import random
import  string

# setting a min length for the password to be
min_length = 5

#for loop adding random characters depending on user length
def password_generator(length):
                # list of characters to be used. string import allows for use of upper and lower case letters.
    char = string.ascii_lowercase + string.ascii_uppercase +"!$%^&*()*/+-"

    # empty variable for storing user password and the condition to add user input to it
    password = "".join(random.choice(char) for x in range(length_choice))
    print(f"Your password is: {password}")

#loop to make sure the app keeps running
while  True:
    try:
        #user input for number choice
        length_choice = int(input("Please select a number you wish to represent the length of your password: "))

        # this ensures the user must enter a minimum length value
        while length_choice < min_length:
            length_choice = int(input("Please select a greater length: "))

        password_generator(length_choice)#calls the functions with modified parameter

        restart = input("would you like to create another? [Y/N]").strip().lower()

        #checking if user would like to restart the app or quit.
        if restart != "y":
            print("Goodbye")
            break

    except ValueError:
        print("Invalid entry! Please enter a number. ")












