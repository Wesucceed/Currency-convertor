"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Author: Jephthah Kwame Mensah( jkm255).
Date:   September 16, 2022.
"""


def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space
    
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s[ : s.index(' ')]


def after_space(s):
    """
    Returns a copy of s after the first space
    
    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return s[ (s.index(' ')+1): ]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that 
    delimits it.  We typically use single quotes (') to delimit a 
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C', 
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """

    return s[ (s.index('"')+1): s.index('"', (s.index('"')+1))]


def get_lhs(json):
    """
    Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    
    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #index_quote1= json.index('"')
    #index_quote2= json.index('"', (index_quote1+ 1))
    #index_quote3= json.index('"', (index_quote2+ 1))
    #index_quote4= json.index('"', (index_quote3+ 1))
   
    #lhs= json[(index_quote3+ 1): index_quote4]

    #return lhs
    
    index_colon1 = json.index(':')
    index_colon2 = json.index(':', (index_colon1 + 1))
    s = json[index_colon1 : index_colon2]

    return first_inside_quotes(s)


def get_rhs(json):
    """
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '19995.85429186 Euros' (not 
    '"38781.518240835 Euros"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #index_quote1= json.index('"')
    #index_quote2= json.index('"', (index_quote1+ 1))
    #index_quote3= json.index('"', (index_quote2+ 1))
    #index_quote4= json.index('"', (index_quote3+ 1))
    #index_quote5= json.index('"', (index_quote4+ 1))
    #index_quote6= json.index('"', (index_quote5+ 1))
    #index_quote7= json.index('"', (index_quote6+ 1))
    #index_quote8= json.index('"', (index_quote7+ 1))

    #rhs= json[(index_quote7+ 1): index_quote8]
    
    #return rhs

    index_last_colon = json.rindex(':')
    index_last_but1_colon = json.rindex(':', 0, index_last_colon)
    s = json[index_last_but1_colon: index_last_colon]
    return first_inside_quotes(s)

def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns True if there
    is an error message. For example, if the JSON is 

    '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It 
    does NOT return the message 'Currency amount is invalid.').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query

    """
    index_quote1= json.index('"')
    index_quote2= json.index('"', (index_quote1+ 1))
    index_quote3= json.index('"', (index_quote2+ 1))
    index_quote4= json.index('"', (index_quote3+ 1))
    index_quote5= json.index('"', (index_quote4+ 1))
    index_quote6= json.index('"', (index_quote5+ 1))
    index_quote7= json.index('"', (index_quote6+ 1))
    index_quote8= json.index('"', (index_quote7+ 1))
    index_quote9= json.index('"', (index_quote8+ 1))
    index_quote10= json.index('"', (index_quote9+ 1))
    index_quote11= json.index('"', (index_quote10+ 1))
    index_quote12= json.index('"', (index_quote11+ 1))

    error_message= json[(index_quote11+1): index_quote12]
    error_present=(len(error_message)>0)

    return error_present


def query_website(old, new, amt):
    """
    Returns a JSON string that is a response to a currency query.
    
    A currency query converts amt money in currency old to the 
    currency new. The response should be a string of the form    
    
    '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
    
    where the values old-amount and new-amount contain the value 
    and name for the old and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "err" will have an error message.
    
    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters
    
    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    import webScrapToJson

    
    json= webScrapToJson.get_rate_json(old, new, amt)
    return json


def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.
    
    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    json_response = query_website(code, code, 0)
    error_present = has_error(json_response)
    return (not error_present)


def exchange(old, new, amt):
    """
    Returns the amount of currency received in the given exchange.
    
    In this exchange, the user is changing amt money in currency 
    old to the currency new. The value returned represents the 
    amount in currency new.
    
    The value returned has type float.
    
    Parameter old: the currency on hand
    Precondition: old is a string for a valid currency code
    
    Parameter new: the currency to convert to
    Precondition: new is a string for a valid currency code
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json_response = query_website(old, new, amt)
    rhs = get_rhs(json_response)
    rhs_amt = float(before_space( rhs))
    return rhs_amt


