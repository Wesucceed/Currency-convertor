"""
Module to extract currency exchange rate from Open Exchange Rate.

This module scrap the currency rates of several currencies from
Open Exchange Rate, get the currency rates of two currencies,
converts one currency to the other, and express the conversion rate
in the form '{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'.

Author: Jephthah Kwame Mensah( jkm255).
Date:   September 17, 2022.
"""

#import requests
#url = "https://openexchangerates.org/api/latest.json?app_id=f1043d48efdb4c30a6e9e0a362a4978a"
#response = requests.get(url)

#Function that gets the total currency rates from Open Exchange Rate with respect to USD
def get_rates( app_id):
    """
    Returns json string which has the currency rates relative to USD of all the currencies
    provided by Open Exchange Rate 

    Parameter app_id: App_id of the user of Open Exchange Rate account
    Precondition: App_id is a string 
    """
    import requests

    url = "https://openexchangerates.org/api/latest.json?app_id="+app_id
    all_rates = requests.get(url)

    return all_rates.text


#Function that gets the exchange rates of the two query currencies with respect to USD
def USD_currency_rate( all_rates, currency):
    """
    Returns json string which has the currency exchange rates relative to USD 
    of a currency

    Parameter all_rates: the returned value of the function "get_rates" 
    Precondition: a json string
    
    Parameter currency: the currency on hand
    Precondition: currency is a string for a valid currency code
    """
    import json
    all_rates_dict = json.loads(all_rates)
    currency_rate_USD = all_rates_dict["rates"][currency]

    return {currency: currency_rate_USD}
    



#Function that get the exchange rate with the two query curriences
def old_new_rate(old_rate, new_rate):
    """
    Returns the exchange rate between two currencies

    Parameter old_rate: exchange rate of currency on hand with respect to USD
    Precondition: old_rate is a dictionary

    Parameter new_rate: exchange rate of current to convert to with respect to USD
    Precondition: new_rate is a dictionary
    """
    for i in old_rate.values():
        old_rate_value = float(i)

    for i in new_rate.values():
        new_rate_value = float(i)

    rate_ratio = new_rate_value / old_rate_value

    return rate_ratio

#Function that converts one currency amount to the other
def old_to_new( currencies_ratio, amount):
    """
    Returns the amount of currency received in a given exchange
    The amount of currency received is the product of currencies_ratio
    and amount

    Parameter currencies_ratio: value of the ratio two currencies
    Precondition: currencies ratio is a float

    Parameter amount: amount of currency on hand
    Precondition: amount is a float
    """
    return currencies_ratio * amount

#Function that expresses the conversion as '{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'
def to_json_string( old, new, old_amount, new_amount):
    """
    Returns a json string that has the old currency, new_currency, old_amount,
    and new_amount

    The json string should be in the form :
    '{ "lhs" : "old_amount old_currency", "rhs" : "new_amount new_currency", "err" : "" }'

    Parameter old: the currency on hand
    Precondition: old is a valid currency code string

    Parameter new: the currency to convert to
    Precondition: new is a valid currency code string

    Parameter old_amount: the amount of the currency on hand
    Precondition: old_amount is an integer

    Parameter new_amount: the amount of the currency to convert to
    Precondition: new_amount is an integer
    """
    format = f'"lhs" : "{old_amount} {old}", "rhs" : "{new_amount} {new}", "err" : ""'
    json = '{ '+ format + ' }'
    return json

def get_rate_json(old, new, amt):
    """
    Returns a json string that has the old currency , new currency,
    old amount, and new amount in the form
    '"lhs" : "old amount old currency", "rhs: "new amount new currency", "err" : ""'

    Parameter old: the currency on hand
    Precondition: old is a valid currency code string

    Parameter new: the currency to convert to
    Precondition: new is a valid currency code string

    Parameter amt: the amount to be converted or on hand
    Precondition: amt is an integer
    """

    rates = get_rates('f1043d48efdb4c30a6e9e0a362a4978a')
    old_rate = USD_currency_rate(rates, old)
    new_rate = USD_currency_rate(rates, new)
    rate_ratio = old_new_rate(old_rate, new_rate)
    desired_amount = old_to_new(rate_ratio, amt)
    json = to_json_string(old, new, amt, desired_amount)
    
    return json


