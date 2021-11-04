# Child Support Guideline Calculator (Colorado)
# Version: 1.0
# Date: 11.02.21
# Author: Brian LeProwse

# TODO: OVERALL
#  Input mismatch, logic --- Test 
#  Determine how to calculate or parse 'Basic Child Support Obligation' table 
#  Format decimals 
#  GUI/web

# TODO Understand how these values are determined from table <------- *****************************
from_guideline_sched = 1919                   # Hardcode from table 
number_kids = 3                               # Kids number relates to guideline?
less_maintenance_spouse_this_marriage = 970   # Dont know what this means...Line 1(f) from worksheet 

# Line 1 from worksheet
parent1_income = int(input('\nEnter Parent1 Income: \n' ))   # 2050 from example
parent2_income = int(input('Enter Parent2 Income: \n'))      # 5500 from example

print('\n------------------------------------------------------------------------')
print('Monthly Gross Income: ')
print('Parent1 Gross: $', parent1_income, '\tParent2 Gross: $', parent2_income)

# Line 2 from worksheet
# Need to understand less_maintenance_spouse_this_marriage calculation ****
monthly_adjusted_gross_parent1 = parent1_income + less_maintenance_spouse_this_marriage
monthly_adjusted_gross_parent2 = parent2_income - less_maintenance_spouse_this_marriage
total_monthly_adjusted = monthly_adjusted_gross_parent1 + monthly_adjusted_gross_parent2
print('\nMonthly Adjusted Gross Income: ')
print('Parent1: $', monthly_adjusted_gross_parent1, 
        '\tParent2: $', monthly_adjusted_gross_parent2, 
        '\tTotal: $', total_monthly_adjusted, '\n')

# Line 2 column 3 
# monthly_adjusted_total = monthly_adjusted_gross_parent1 + monthly_adjusted_gross_parent2
# print('Total Monthly Adjusted Gross Income: ', '\n$', monthly_adjusted_total, '\n')

# Line 3 from worksheet
print('Parent Percentage Share of Income:')
percent_of_income_parent1 = monthly_adjusted_gross_parent1 / total_monthly_adjusted
percent_of_income_parent2 = monthly_adjusted_gross_parent2 / total_monthly_adjusted
print('Parent1: ', (percent_of_income_parent1)*100, '%', 
        '\tParent2: ', (percent_of_income_parent2)*100, '%', '\n')

# Line 4 from worksheet
print('Amount from Guideline Schedule: ', '$',from_guideline_sched, '\n')  # <----------------- DETERMINE

# Line 5 from worksheet 
basic_child_support_obligation = 1.5 * from_guideline_sched    # 1.5 x from_guideline_sched <------------
print('Basic Child Support Obligation: ', '$', basic_child_support_obligation, '\n')

# Line 6 from worksheet
parent1_share_basic_support = percent_of_income_parent1 * basic_child_support_obligation
parent2 = percent_of_income_parent2 * basic_child_support_obligation
print('Basic Support:')
print('Parent1: $', parent1_share_basic_support, '\tParent2: $', parent2, '\n')
print('------------------------------------------------------------------------')

# Line 7 from worksheet
overnights_first_parent = int((input('Enter Overnights for a single parent: \n')))
overnights_second_parent = 365 - overnights_first_parent
print('\nParent Overnights: ')
print('Parent1:', overnights_first_parent, '\tParent2:', overnights_second_parent)

# Line 8 from worksheet
parent1_percentage = overnights_first_parent/365
parent2_percentage = overnights_second_parent/365
print('\nPercentage Time Each Parent:')
print('Parent1:', (parent1_percentage)*100, '%', 
                    '\tParent2:', (parent2_percentage)*100, '%')

# Line 9 from worksheet
parent1_portion_owed = parent1_share_basic_support * parent2_percentage
parent2_portion_owed = parent2 * parent1_percentage
print('\nPortion of Own share Owed to Other Parent:')
print('Parent1: $', parent1_portion_owed, '\tParent2: $', parent2_portion_owed)

# Lines 10-13 from worksheet redundant in version 1.0 ***************

# Line 14 from worksheet
print('\n\t\tRecommended Support Order:')
if parent1_portion_owed > parent2_portion_owed:
    recommended_support_order = parent1_portion_owed - parent2_portion_owed
    print('\t\tParent1 pays Parent2: $', recommended_support_order)
else:
    recommended_support_order = parent2_portion_owed - parent1_portion_owed
    print('\t\tParent2 pays Parent1: $', recommended_support_order)

print('------------------------------------------------------------------------')
print('\n')
