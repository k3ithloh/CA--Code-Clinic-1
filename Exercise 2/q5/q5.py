##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def reformat_string(input_string):
    # YOUR CODE GOES HERE
    output_string = ""
    for char in input_string:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            output_string += char.upper()
        else:
            output_string += char.lower()
    return output_string

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = reformat_string('HuiQing')
print("Expected: hUIqIng" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = reformat_string('MaRrenTilLOno')
print("Expected: mArrEntIllOnO" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = reformat_string('GeKItouTAISEn')
print("Expected: gEkItOUtAIsEn" )
print("Actual:   " + str(result))
print()