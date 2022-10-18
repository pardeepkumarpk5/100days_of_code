print('Welcome to the tip calculator.')

# asking for total bill
total_bill = float(input('What was the total bill? $'))

# asking for total no of people
no_of_people = float(input('How many people to spilt the bill? '))

# asking for percentage of tip
tip_percentage = float(
    input('What percentage of tip would like to give? 10, 12 or 15? '))


# calculating bill each person has to pay
bill_per_person = (total_bill/no_of_people)
tip = (total_bill*tip_percentage) / 100

final_pay = round(bill_per_person + tip/no_of_people, 2)
print(f'Each person should pay : {final_pay}$')
