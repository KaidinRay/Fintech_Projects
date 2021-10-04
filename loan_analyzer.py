# coding: utf-8
import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

# Total number of loans that are in the list

loan_costs = [500, 600, 200, 1000, 450]
x = len(loan_costs)
print(x)

# Calculations of the total of all loans

loan_costs = [500, 600, 200, 1000, 450]
y = sum(loan_costs)
print(y)

# Calculations of the average loan amount from the list

average_loan_price = (y/x)
print(average_loan_price)

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable."""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
print(future_value)

remaining_months = loan.get("remaining_months")
print(remaining_months)
print(loan.pop("loan_price"))
print(loan)
"""@NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""
Annual_Discount_Rate = .20
present_value = future_value / (1+ Annual_Discount_Rate/12)

cost = 500
present_value = 374.99
if present_value >= cost:
    print ('The loan is at least worth the cost to buy it')

else: print('The loan is too expensive and not worth the price')

# Calculations of the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#  Extraction of the Future Value and Remaining Months on the loan.

future_value = loan.get('future_value')
print(future_value)
remaining_months = loan.get('remaining_months')
print(remaining_months)



present_value = future_value/(1 + .20/12) ** remaining_months
print(present_value)



if present_value >= 500:
    print (f'The loan is at least worth the cost to buy it')
else: print(f'The loan is too expensive and not worth buying')




def calculate_present_value(future_value,remaining_months,annual_discount_rate):
    return future_value/(1 + .20/12) ** remaining_months

# Calculations of the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
future_value = new_loan["future_value"]
remaining_months = new_loan["remaining_months"]
Annual_Discount_Rate = .20







# Calculations of  the present value of the new loan given below.

print(f"The present value of the loan is: {present_value}")




loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


inexpensive_loan = []

#Loop created searching through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

for loan_price in loans:
    cost = loan_price["loan_price"]
    if cost <= 500:
        inexpensive_loan.append(cost)


print(inexpensive_loan)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")


# Saving the copy of the data as a CSV for the company's business analysts.
inexpensive_loans = []
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
with open (Path('inexpensive_loans.csv'),"w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter .writerow(header) 
    for loan in inexpensive_loans:
        csvwriter .writerow(loan.values())