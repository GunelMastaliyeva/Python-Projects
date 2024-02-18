
#Program introduction
print("Welcome to my program!")

#Ask user for input.
name= input("Please enter your full name: ")
print("Hello,",name)
print("This Program will ask you to enter the base and height of a triangle.The program will calculate and print the area of triangle")

#Ask user to enter base and height of triangle
base=eval(input("Enter base of a triangle: "))
height=eval(input("Enter height of a triangle: "))

# Zero and negative numbers are not accepted.
if base > 0 and height > 0:
    
    #calculate the are of triangle
    area= 0.5 * base * height
    print("The area is: ", format(area, '.2f'))
    print('Thank you and have a nice day.\nGood bye!')

else:
    print("Error. Negative number and zero are not accepted.") #Error message





    
