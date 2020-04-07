# Mortgage Calculator

# define loan function
def loan(prop_value, percent_down):

    deci_percent = float(percent_down)/100 # convert percent down to a decimal
    loan_diff = int(prop_value) * deci_percent
    loan_ = int(prop_value) - loan_diff
    print("The loan your taking out is ${}".format(loan_))
    return loan_

# convert annual interest rate to monthly rate

def month_int_rate(rate):
    deci_rate = float(rate)
    month_rate = deci_rate/12
    round_mr = round(month_rate)
    print("Your monthly interest rate is {}%".format(round_mr))
    return round_mr


# determine how much borrower will spend per month

def monthly_payments(loan, month_rate, term):
    months = int(term)*12
    mp_noint = loan/months # monthly payments without interest
    overall_int_amnt = loan * month_rate # overall interest amount
    month_int_amnt = overall_int_amnt/months
    mp_int = month_int_amnt + mp_noint
    round_mp = round(mp_int)
    print("You will be paying ${} per month for this mortage over a {} month span".format(round_mp, months)) # overall monthly payments
    return

# input variables

prop_value = input("How much is the property? ")
percent_down = input("How much percent are you putting down? ")
rate = input("What is your annual interest rate? ")
term = input("How long is the mortgage term for? ")

# call functions

loan_func = loan(prop_value, percent_down)
month_func = month_int_rate(rate)
monthly_payments(loan_func, month_func, term)
