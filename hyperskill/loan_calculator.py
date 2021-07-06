#loan calculator program
import argparse
from math import log
from math import pow
from math import ceil
from math import floor

###  functions  ###

def differentiated_payments(loan_principal, num_periods, loan_interest):
    over_payment = 0
    loan_interest = loan_interest / 100
    i = loan_interest / 12
    
    for m in range(1, num_periods + 1):
        diff_monthly_payment = loan_principal / num_periods + i * (loan_principal - (loan_principal * (m - 1) / num_periods))
        over_payment += ceil(diff_monthly_payment)
        print(f"Month {m}: payment is {ceil(diff_monthly_payment)}")
    
    print(f"\nOverpayment = {over_payment - loan_principal}")
    
def annuity_monthly_payment(loan_principal, num_periods, loan_interest):
    loan_interest = loan_interest / 100   
    i = loan_interest / 12
    
    ordinary_annuity = loan_principal * (i * pow(1 + i, num_periods)) / (pow(1 + i, num_periods) - 1)
    
    print(f"Your annuity payment = {ceil(ordinary_annuity)}!")
    print(f"Overpayment = {ceil(ordinary_annuity) * num_periods - loan_principal}")
    
def loan_principal_func(annuity_payment, num_periods, loan_interest):
    loan_interest = loan_interest / 100
    i = loan_interest / 12
    
    denominator = (i * pow(1 + i, num_periods)) / (pow(1 + i, num_periods) - 1)
    loan_principal = annuity_payment / denominator
    
    print(f"Your loan principal {floor(loan_principal)}!")
    print(f"Overpayment = {annuity_payment * num_periods - floor(loan_principal)}")    

def num_monthly_payments(loan_principal, monthly_payment, loan_interest):
    loan_interest = loan_interest / 100
    i = loan_interest / 12
    
    n = ceil(log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
    
    if n % 12 == 0:
        print("It will take {} years to repay this loan!".format(int(n / 12)))
    else:
        print("It will take {} years and {} months to repay this loan!".format(int(n / 12), n % 12))
    
    print(f"Overpayment = {ceil(n * monthly_payment - loan_principal)}")
    
##########

parser = argparse.ArgumentParser(description="This is a loan calculator program.")

parser.add_argument("-typ", "--type")
parser.add_argument("-pri", "--principal")
parser.add_argument("-per", "--periods")
parser.add_argument("-int", "--interest")
parser.add_argument("-pay", "--payment")

args = parser.parse_args()

if not(args.type == "annuity" or args.type == "diff"):  # can only accept annuity or differential payments
    print("Incorrect parameters")
elif args.interest is None:  # interest value always needed
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:  # differential payment does not include payment parameter
    print("Incorrect parameters")
elif args.type == "diff" and (args.principal is None or args.periods is None or args.interest is None):
    print("Incorrect parameters")
elif args.type == "diff":
    differentiated_payments(int(args.principal), int(args.periods), float(args.interest))
elif args.type == "annuity" and args.payment is None:
    annuity_monthly_payment(int(args.principal), int(args.periods), float(args.interest))
elif args.type == "annuity" and args.principal is None:
    loan_principal_func(int(args.payment), int(args.periods), float(args.interest))
elif args.type == "annuity" and args.periods is None:
    num_monthly_payments(int(args.principal), int(args.payment), float(args.interest))
    
    