import sys
import random
number = int(sys.stdin.readline().strip())

file = open('_strings.txt', 'a')
for num in range(0, number):
    num = random.randrange(97,123)
    result = chr(num)
    file.write(result+'\n')
file.close()