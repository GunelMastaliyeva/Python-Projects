
#Program introduction for the user
print("Welcome! This program will calculate the output voltage average of your generators.")


#Ask the input from user
generator_num= eval(input("Enter the number of generators to test: "))

#Variable initialization
total_average_voltage = 0
generator_count = 1

#Loop through generator

while generator_count <= generator_num:
    print("Generator {}".format(generator_count))
    
    #Ask user to enter test voltage
    print("Please enter 3 test voltages")
    
    voltage_1=eval(input("Voltage reading 1: "))
    voltage_2=eval(input("Voltage reading 2: "))
    voltage_3=eval(input("Voltage reading 3: "))

   #Calculate average voltage
    average_output_voltage = (voltage_1 + voltage_2 + voltage_3)/3

   #Result for average output voltage
    print(f"The average output voltage for generator {generator_count} is: ", format(average_output_voltage, ".2f" ))
    
    total_average_voltage= total_average_voltage + average_output_voltage
    generator_count = generator_count +1
   
#Calculate overall average voltage for all generators
total_average_voltage = total_average_voltage / generator_num
print("Total average of all generators is:", format(total_average_voltage, ".2f"))
