"""
User interface for module currency.

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting first currency to 
the second. 

Author: Jephthah Kwame Mensah (jkm255).
Date: September 16, 2022.
"""
import a1, webScrapToJson



currency_original = input('Enter original currency: ')
currency_desired = input('Enter desired currency: ')
amount_original = float(input('Enter original amount: '))
exchange_amount = a1.exchange(currency_original, currency_desired, amount_original)

print('You can exchange '+ str(amount_original)+' '+ currency_original +' '+ 'for'+' ' +str(exchange_amount)+' '+currency_desired+'.')