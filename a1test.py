"""
Test script for module a1.

When run as a script, this module invokes several procedures that
test the various functions in module a1.

Author: Jephthah Kwame Mensah( jkm255).
Date: September 16, 2022.
"""

import introcs
import a1


def testA():
    """
    Test procedure for Part A
    """

    #Testing for function before_space
    print('Testing for function before_space')

    #Test "4.502 Euros"
    input = "4.502 Euros"
    result = a1.before_space(input)
    introcs.assert_equals("4.502", result)
    
    #Test ' Euros'
    input = ' Euros'
    result = a1.before_space(input)
    introcs.assert_equals('', result)

    #Test '4.502 Euros '
    input = '4.502 Euros '
    result = a1.before_space(input)
    introcs.assert_equals('4.502', result)

    #Test 'Euros 4.502'
    input = 'Euros 4.502'
    result = a1.before_space(input)
    introcs.assert_equals('Euros', result)

    #Test '? 4.502'
    input = '? 4.502'
    result = a1.before_space(input)
    introcs.assert_equals('?', result)

    #Test '4.502  Euros'
    input = '4.502  Euros'
    result = a1.before_space(input)
    introcs.assert_equals('4.502', result)

    #Test '4.502   Euros  '
    input = '4.502   Euros  '
    result = a1.before_space(input)
    introcs.assert_equals('4.502', result)
    
    #Test ' '
    input = ' '
    result = a1.before_space(input)
    introcs.assert_equals('', result)
    
    #Test '  '
    input = '  '
    result = a1.before_space(input)
    introcs.assert_equals('', result)
    
    #Test '4.502 Euros US'
    input = '4.502 Euros US'
    result = a1.before_space(input)
    introcs.assert_equals('4.502', result)

    
    #Testing for function after_space
    print('Testing for function after_space')

    #Test "4.502 Euros"
    input = "4.502 Euros"
    result = a1.after_space(input)
    introcs.assert_equals("Euros", result)
    
    #Test ' Euros'
    input = ' Euros'
    result = a1.after_space(input)
    introcs.assert_equals('Euros', result)

    #Test '4.502 Euros '
    input = '4.502 Euros '
    result = a1.after_space(input)
    introcs.assert_equals('Euros ', result)
    
    #Test 'Euros 4.502'
    input = 'Euros 4.502'
    result = a1.after_space(input)
    introcs.assert_equals('4.502', result)

    #Test '? 4.502'
    input = '? 4.502'
    result = a1.after_space(input)
    introcs.assert_equals('4.502', result)

    #Test '4.502  Euros'
    input = '4.502  Euros'
    result = a1.after_space(input)
    introcs.assert_equals(' Euros', result)

    #Test '4.502   Euros  '
    input = '4.502   Euros  '
    result = a1.after_space(input)
    introcs.assert_equals('  Euros  ', result)
    
    #Test ' '
    input = ' '
    result = a1.after_space(input)
    introcs.assert_equals('', result)
    
    #Test '  '
    input = '  '
    result = a1.after_space(input)
    introcs.assert_equals(' ', result)
    
    #Test '4.502 Euros US'
    input = '4.502 Euros US'
    result = a1.after_space(input)
    introcs.assert_equals('Euros US', result)


def testB():
    """
    Test procedure for Part B
    """

    #Testing for function first_inside_quotes
    print('Testing for function first_inside_quotes')

    #Test '"ABCS D"'
    input = '"ABCS D"'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals("ABCS D", result)


    #Test 'A "B C" D'
    input = 'A "B C" D'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('B C', result)
    
    #Test 'A "B C" D "E F" G'
    input = 'A "B C" D "E F" G'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('B C', result)

    #Test '""'
    input = '""'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals('', result)

    #Test '" "C'
    input = '" "C'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals(' ', result)

    #Test ' $" "'
    input = ' $" "'
    result = a1.first_inside_quotes(input)
    introcs.assert_equals(' ', result)


    #Testing for function get_lhs
    print('Testing for function get_lhs')

    #Test '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    input = '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    result = a1.get_lhs(input)
    introcs.assert_equals( "1 Bitcoin", result)

    #Test '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    input = '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    result = a1.get_lhs(input)
    introcs.assert_equals( "", result)


    #Testing for function get_rhs
    print('Testing for function get_rhs')

    #Test '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    input = '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    result = a1.get_rhs(input)
    introcs.assert_equals( "19995.85429186 Euros", result)

    #Test '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    input = '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    result = a1.get_rhs(input)
    introcs.assert_equals( "", result)


    #Testing for function has_error
    print('Testing for function has_error')

    #Test '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    input = '{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    result = a1.has_error( input)
    introcs.assert_equals( True, result)

    #Test '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    input = '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    result = a1.has_error( input)
    introcs.assert_equals( False, result)


def testC():
    """
    Test procedure for Part C
    """

    #Testing for function query_website
    print("Testing for fuction query_website")

    #Test ['USD', 'CUP', 2.5]
    input = ['USD', 'CUP', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected =('{ "lhs" : "2.5 United States Dollars",' +
    ' "rhs" : "64.375 Cuban Pesos", "err" : "" }')

    introcs.assert_equals(expected, result)
    
    #Test ['US', 'CUP', 2.5]
    input =['US', 'CUP', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected =('{ "lhs" : "",' +
    ' "rhs" : "", "err" : "Source currency code is invalid." }')
    introcs.assert_equals(expected, result)

    #Test ['Usd', 'CUP', 2.5]
    input = ['Usd', 'CUP', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected = ('{ "lhs" : "",' +
    ' "rhs" : "", "err" : "Source currency code is invalid." }')
    introcs.assert_equals(expected, result)

    #Test ['usd', 'CUP', 2.5]
    input = ['usd', 'CUP', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected = ('{ "lhs" : "",' +
    ' "rhs" : "", "err" : "Source currency code is invalid." }')
    introcs.assert_equals(expected, result)

    #Test ['USDOLLAR', 'CUP', 2.5]
    input = ['USDOLLAR', 'CUP', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected = ('{ "lhs" : "",' + 
    ' "rhs" : "", "err" : "Source currency code is invalid." }')
    introcs.assert_equals(expected, result)

    #Test ['USD', 'CU', 2.5]
    input = ['USD', 'CU', 2.5]
    old, new, amt = input 
    result = a1.query_website(old, new, amt)
    expected = ('{ "lhs" : "",' +
    ' "rhs" : "", "err" : "Exchange currency code is invalid." }')
    introcs.assert_equals(expected, result)


def testD():
    """
    Test procedure for Part D
    """

    #Testing for function is_currency
    print('Testing for function is_currency')

    #Testing 'abc'
    input = 'abc'
    result = a1.is_currency( input)
    introcs.assert_equals( False, result)

    #Testing 'GBP'
    input = 'GBP'
    result = a1.is_currency( input)
    introcs.assert_equals( True, result)

    #Testing 'USD'
    input = 'USD'
    result = a1.is_currency( input)
    introcs.assert_equals( True, result)

    #Testing 'usd'
    input = 'usd'
    result = a1.is_currency( input)
    introcs.assert_equals( False, result)

    #Testing 'Usd'
    input = 'Usd'
    result = a1.is_currency(input)
    introcs.assert_equals( False, result)


    #Testing for function exchange
    print('Testing for function exchange')

    #Test ['USD', 'GBP', 2.0]
    input = ['USD', 'GBP', 2.0]
    old , new, amt = input
    result = a1.exchange(old, new, amt)
    introcs.assert_floats_equal(1.736488, result)

    #Test ['USD', 'USD', 2.0]
    input = ['USD', 'USD', 2.0]
    old , new, amt = input
    result = a1.exchange(old, new, amt)
    introcs.assert_floats_equal(2.0, result)

    #Test ['USD', 'USD', 0.0]
    input = ['USD', 'USD', 0.0]
    old , new, amt = input
    result = a1.exchange(old, new, amt)
    introcs.assert_floats_equal(0.0, result)
    

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')