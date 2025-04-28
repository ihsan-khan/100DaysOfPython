# who will pay the bill
import random
persons = input('Enter the names of persons separated by commas: ').split(',')
print(persons[random.randint(0,len(persons)-1)] + ' will pay the bill')