total_bill = input('enter total bill amount: $')
tip = input('enter tip percentage: ')
people = input('enter number of people: ')
total_bill = float(total_bill)
tip_percent = float(tip) / 100
final_bill = total_bill + (total_bill * tip_percent)
final_bill = round(final_bill, 2)  
each_person_bill = final_bill / int(people) 
each_person_bill = "${:.2f}".format(each_person_bill)  # Format to 2 decimal places
print(f'Each person should pay : ${each_person_bill}')
