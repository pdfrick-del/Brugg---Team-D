#---Imports for the Code---
from datetime import date
from pathlib import Path
from modules import user_data

#---Variables for the Code---
CSV_PATH_FEES = Path(__file__).resolve().parent.parent / "data" / "Library_User_Fees_data.csv"
ANUAL_FEE = 50

#---Functions for the Code---
def update_membership_fees(fees):
    today = date.today()
    registration_date = date.fromisoformat(fees["Account_Creation_Date"])
    last_update = date.fromisoformat(fees["Last_Update"])
    
    anual_date = date(today.year, registration_date.month, 1)

    return last_update < anual_date <= today

def calculate_discount(registration_date):
    today = date.today()
    years = today.year - registration_date.year
    
    if (today.month, today.day) < (registration_date.month, registration_date.day):
        years -= 1

    if years >= 10:
        return 10
    
    elif years >= 5:
        return 5

    return 0

def calculating_anual_fee(registration_date):
    anual_fee = ANUAL_FEE - calculate_discount(registration_date)
    return anual_fee

def adding_current_anual_fee(outstanding_amount, anual_fee):
    outstanding_amount = outstanding_amount + anual_fee
    return outstanding_amount

def late_fee(outstanding_amount, anual_fee):
    late_fee = (outstanding_amount - anual_fee) * 0.1
    return late_fee

def adding_current_late_fee(outstanding_amount, late_fee):
    outstanding_amount = outstanding_amount + late_fee
    return outstanding_amount