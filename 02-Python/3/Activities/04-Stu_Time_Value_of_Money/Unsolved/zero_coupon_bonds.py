# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def calculate_present_value(FV, i, n, t):
    """
        calculates the net present value
        args:
            FV - future value
            i - the interest rate
            n - the compounding period
            t - the number of years
        return:
            the computed present value
    """
    
    PV = FV/(1+i/n)**(n*t)
    
    return round(PV,2)

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
present_value = calculate_present_value(future_value, discount_rate, compounding_periods, years)

# @TODO: Determine if the bond is worth it
if price > present_value:
    print(f"It's a premium of ${round(price-present_value,2)} so maybe not worth purchasing the bond")
elif price < present_value:
    print(f"It's a discount of ${round(price-present_value,2)} so worth purchasing the bond")
else:
    print("It's selling at par")

print(calculate_present_value.__doc__)