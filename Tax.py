#  This program computes income taxes, using a simplified tax schedule
# for single or married people
# @author Ahmad Barakat

# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25
RATE1_SINGLE_MID = 8000.0
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_MID = 16000.0
RATE1_MARRIED_LIMIT = 64000.0     

# Read income and marital status     
income = float(input("Please enter your income: $"))
maritalStatus = input("Please enter s for single, m for married: ")

# Compute taxes due.
tax1 = 0
tax2 = 0
tax3 = 0

# for single
if maritalStatus.lower() == "s" :
   if income <= RATE1_SINGLE_MID :
      tax1 = RATE1 * income
   elif RATE1_SINGLE_MID < income < RATE1_SINGLE_LIMIT:
      tax1 = (RATE1 * RATE1_SINGLE_MID)
      tax2 = (RATE2 * (income - RATE1_SINGLE_MID))
   else :
        tax1 = RATE1 * RATE1_SINGLE_MID
        tax2 = RATE2 * (RATE1_SINGLE_LIMIT - RATE1_SINGLE_MID)
        tax3 = RATE3 * (income - RATE1_SINGLE_LIMIT)
# for married
elif maritalStatus.lower() == "m":
    if income <= RATE1_MARRIED_MID:
        tax1 = RATE1 * income
    elif income <= RATE1_MARRIED_LIMIT:
        tax1 = (RATE1 * RATE1_MARRIED_MID)
        tax2 = (RATE2 * (income - RATE1_MARRIED_MID))
    else:
        tax1 = RATE1 * RATE1_MARRIED_MID
        tax2 = RATE2 * (RATE1_MARRIED_LIMIT - RATE1_MARRIED_MID)
        tax3 = RATE3 * (income - RATE1_MARRIED_LIMIT)
#unrecognized
else:
   print("Unrecognized marital status")
          
totalTax = tax1 + tax2 + tax3

# print(tax1)
# print(tax2)
# print(tax3)

# Print the results.
print(f"The tax is ${totalTax:,.2f}")