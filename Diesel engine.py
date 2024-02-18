'''
This program demonstrates computer aided troubleshooting of diesel engine.

Name: Gunel Mastaliyeva
Date: 02/04/2024
Course: CIS-2531

'''

import sys

#Tester ID 
tester_ID= 123456

#Ask the user to enter the tester ID.
user_input= int(input("Enter tester ID: "))

# Validate the ID
if user_input == tester_ID:
    print ("Thank you for providing tester ID")
    print ("Check status light") #Ask the user to chechk the light

#Ask user to enter the color and also validate the inputs of the user
    while True:
        light_color=input("Enter the color that you see: ").upper()
        if light_color in ["RED","AMBER","GREEN"]:
            break
        else:
            print("Invalid color. Please enter 'RED', 'GREEN' or 'AMBER'")
        
    #Provide user with directions if the light color is red, green or amber
    if light_color == "GREEN":
        print("Do restart procedure")
    elif light_color == "AMBER":
        print("Check fuel line service routine")
    elif light_color == "RED":
        print ("Shut off all input lines check meter")
       

        #Ask user to provide test pressure if the light color is red
        pressure=int(input("Enter test pressure: ")) #input from user

        if pressure < 50:
            print ("Check main line for test pressure")
        else:
            print("Measure flow velocity at inlet 2-B")

            #Ask user to provide velosite if the pressure is greater than or equal to 50
            velocity=input("Is the velocity normal?: yes/no: ")
            
            if velocity == "yes":
                print(" Refer to inlet service manual.")
                sys.exit()
            else:
                print("Refer unit for factory service.")
                sys.exit()
                
        #Ask user to provide input regarding if the pressure is normal or not.          
        pressure=input("Is the pressure normal?: yes/no ")

        #Describe two different directions for user if the pressure is normal or vice versa.
        if pressure == "yes":
            print ("Refer to motor service manual")
            sys.exit() 
        else:
            print("Refer to main line manual.")
            sys.exit()
            
else:
    print("It is not a valid ID. Check the ID.") #Statement to show the user if the tester Id is not valid.


           
 
