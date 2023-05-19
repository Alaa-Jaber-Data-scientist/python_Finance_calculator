# Import the math module to perform mathematical operations
import math

# Display menu options to the user
print("\tFinancil calculator")
print("\nDo you want to calculate the interest on an investment or the repayments on a bond?")
print("Please choose which calculation you want to do:" ) # Provide information on program's functionality.
print("\tinvestment - to calculate the amount of interest you'll earn on your investment")
print("\tbond\t   - to calculate the amount you'll have to pay on a home loan")

# Prompt the user to choose the type of financial calculation to perform
# Loop until a valid financial_type is chosen
while True:
    financial_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    # The investment calculation
    if financial_type == 'investment':
        print("\nThank you! You have chose to calculate:",financial_type.capitalize())
        # Do investment calculation
        # prompt user for investment details with input validation       
        while True:
            try:
                deposit_amount=float(input("\tEnter the amount of money that you are depositing: "))
                if deposit_amount <= 0:  # Handle negative input by the user
                    raise ValueError
                break
            except ValueError:  # Handle non-numeric input by the user
                print("Please enter a valid positive number. Only numerical input is allowed.")

        while True:
            try:
                interest_rate=float(input("\tPlease enter the interest rate as a percentage (without the percentage symbol): "))/100
                if interest_rate<= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number. Only numerical input is allowed.")

        while True:
            try:
                years_number=float(input("\tWhat is the number of years you plan on investing: "))
                if years_number<= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number. Only numerical input is allowed.")

            
        interest_type=input("\tPlease indicate whether you would like \"simple\" or \"compound\" interest: ")
        
        # Calculate the total amount based on interest type
        while interest_type:                  
            if interest_type.lower()=="simple":
                total_amount = deposit_amount*(1 + interest_rate*years_number) 
            elif interest_type.lower()=="compound":
                total_amount= deposit_amount* math.pow((1+interest_rate),years_number)
            else: 
                # Display error message on invalid input.
                print("You have entered an invalid value. Please try again")
                interest_type=input("\tPlease indicate whether you would like \"simple\" or \"compound\" interest: ")
            
            # Print the total amount with two decimal places
            print("The total amount is: {:.2f}".format(total_amount))
            break
    
        break
    
    # The Bond calculation
    elif financial_type == 'bond':
        print("\nThank you! You have chose to calculate:",financial_type.capitalize())
        # Do bond calculation
        # Prompt the user for the necessary information
        while True:
                try:
                    house_value =float(input("\tEnter the present value of the house: "))
                    if house_value<= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid positive number. Only numerical input is allowed.")


        while True:
                try:
                    interest_rate=float(input("\tEnter the annual interest rate: "))/100/12
                    if interest_rate<= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid positive number. Only numerical input is allowed.")

        while True:
                try:
                    months_number=int(input("\tPlease enter the duration, in months, that you plan to take to repay the bond: "))
                    if months_number<= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid positive number. Only numerical input is allowed.")
        
        
        repayment = (interest_rate *house_value)/(1 - (1 +  interest_rate)**(-months_number))
    # Display the monthly repayment amount to the user
        print("You will have to repay: {:.2f} each month".format(repayment))
                
        break
        

    else:
        # Print error message and ask user to try again
        print("You have entered an invalid value. Please choose either \"investment\" or \"bond\"")



    


                
            
        
    


