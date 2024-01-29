 # This is going to be a text-based simulation that displays different output based on the users input

# Project Requirments

# Need 2 Loops

# Need decision logic - If/else statements aim for 3 levels deep.

# Set up while loop here to allow the user to run the sim multiple times
while True:

    # Show the user descriptive text for why this sim is so cool and why they want to run through it several times.

    # Insert some print () statements here
    print("Welcome to my text-based sim. Play many times it will be fun!")
    print("You find your self at a crossroad. which path will you choose?")
    print("1. Follow the path through the dark forest")
    print("2. Cross the river by skipping on stones across the water! ")


    # Need to gather input from the user for what path they want to take.


    # Insert an input () statement here.
    # Need to store their choice in a variable
    choice1 =input("Enter your choice(1 or 2): ")
    

    #   THIS IS OUR FIRST DECISION LOGIC - 1/3
    #   Insert Decision logic to handle different options
    #   If they chose option 1, then write an if statement.
    
    if choice1 == '1': 
    #   print some information about going this direction.
        print("You enter the dark forest and you hear a load growl")
        print("1. You ignore the growl and keep walking!")
        print("2. You walk towards the growl! ")
    #   Insert an input () statement so they have more options on wat direction to go
        choice2 =input("Enter your choice(1 or 2): ")

     

    #   THIS IS OUR FIRST DECISION LOGIC - 2/3
    #    Insert Decision logic to handle different options
    #   If they chose option 1, then write an if statement.
    if choice2 == '1':
    #       print some information about going this direction.
            print("The noise is getting louder and its next to you")
            print("1. Ignore the growl and keep walking!")
            print("2. Shine your flashlight towards the direction the growl is coming from! ")       
    #       Insert an input () statement so they have more options on wat direction to go
            choice3 =input("Enter your choice(1 or 2): ")

    

    #   THIS IS OUR FIRST DECISION LOGIC - 3/3
    #   Insert Decision logic to handle different options
    #   If they chose option 1, then write an if statement.
            
    if  choice3 == '1':
        print("You reach a cliff you lose!")
    #   If they choose option 2, then write on elif statement (else if)
    elif choice3 == '2':
        print("You discover a baby kitten. You just got a new pet! You Win!")
    else:
        print("Invalid choice. Please enter 1 or 2")
    #   for any other input, then write an else statement.
    #   If they choose option 2, then write on elif statement (else if)
    #   for any other input, then write an else statement.

    #   If they choose option 2, then write on elif statement (else if)
    #   Insert Decision logic to handle different options
    #   If they chose option 1, then write an if statement.
    #   print some information about going this direction.
    #   Insert an input () statement so they have more options on wat direction to go
    #   Add another while loop here
    #   for any other input, then write an else statement.

    # Ask the user if they want to continue, if no, break out of the loop.
    
    replay = input("Do you want to play again? (yes/no): ")
    
    if replay.lower() != 'yes':
        print("Thank you for playing")
        break
    
            
