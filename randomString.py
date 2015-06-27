__author__ = 'jeffs'

import random

def randomString(n):
    res = ''
    letters = 'abcdefghijklmnopqrstvxyz'
    for i in range(n):
        res += random.choice(letters)
    return res

catString = ''
count = 0
while catString != 'cat':
    count += 1
    catString = randomString(3)

print (count, catString)
