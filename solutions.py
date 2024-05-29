"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
# My changes 
try:
    total_profit1 = float(input("Enter profit value for total sale:\n"))
    total_profit2 = float(input("Now increase it by 0.23%:\n"))
    profit = total_profit1 * 0.23
    sum = total_profit1 + total_profit2+ profit 
    print("Your sum:", sum, end='\n\n')
    #DONE!!!
except:
    print("Sorry on numeric values are allowed", end='\n\n')

def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
try:
    n1 = int(input("Enter a number\n"))
    n2 = int(input("Enter a your second number\n")) 
    quotient = n1//n2
    remainder =n1%n2
    print("The Remainder is:\n", quotient, end='\n')
    print("The quotient is:\n", remainder, end='\n\n')
except:
    print("Sorry on numeric values are allowed",end='\n')

def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
try:
    Miles_Driven = float(input("Enter number of miles driven so far:\n"))
    Gas_used = float(input("Enter how much gas was used:\n"))
    mpg = Miles_Driven / Gas_used
    print('Miles per gallon =', mpg, end='\n\n')
except:
    print("Sorry on numeric values are allowed", end='\n\n')


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
try:
    Your_number1 = float(input("Please include your first number here!:\n"))
    Your_number2 = float(input("Now your second:\n"))
    Your_number3 = float(input("Lastly, your third:\n"))
    output_message = "Here are your prices!"
    print(output_message,end='\n\n')
    print("{:.2f}".format(Your_number1,end='\n'))
    print("{:.2f}".format(Your_number2,end='\n'))
    print("{:.2f}".format(Your_number3,end='\n\n'))
except:
    print("Sorry on numeric values are allowed",end='\n\n')