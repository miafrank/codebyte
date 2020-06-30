# Given an integer, , print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
from decimal import *

sample_input = 2

# todo figured out width with f string or .format


def print_formatted(number):
    width = len(bin(number)[2:])
    for n in range(1, number + 1):
        i_dec_formatted = "{0:d}".format(n)
        i_oct_formatted = "{0:o}".format(n)
        i_hex_formatted = "{0:X}".format(n).upper()
        i_bin_formatted = "{0:b}".format(n)
        print(i_dec_formatted.rjust((width)), i_oct_formatted.rjust((width)),
              i_hex_formatted.rjust((width)), i_bin_formatted.rjust((width)))


(print_formatted(sample_input))

# def print_formatted(number):
#     width=len(bin(number)[2:])
#     for i in range(1,number+1):
#         deci=str(i)
#         octa=oct(i)[2:]
#         hexa=(hex(i)[2:]).upper()
#         bina=bin(i)[2:]
#         print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

