"""This module counts the number of lines in a standard input
Input: string from the system standard input
"""

import sys

count = 0
for line in sys.stdin:
    count += 1

print(count,  'line in standard input')
