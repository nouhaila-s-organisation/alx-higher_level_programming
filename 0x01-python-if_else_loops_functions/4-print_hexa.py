#!/usr/bin/python3
# 4-print_hexa.py
# nouhaila<123@holbertonschool.com>

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
