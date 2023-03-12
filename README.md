# Dec_to_Bin
This function allows you to convert any decimal number to a binary number system with adjustable precision.
binary(num: decimal.Decimal, accuracy, req_int_part=True, req_frac_part=True) receives a decimal.Decimal object (exact floating point number) and the required number of decimal places (integer) as input
Returns the result as a string(!)
req_int_part=False means that the integer part is not required.
req_frac_part=False means that the fractional part is not required.
With both options set to False, the settings will reset to True for both flags.
