import sys
import random as rand

args = sys.argv[1:]

if len(args) > 0:
    print(args[rand.randint(0, len(args) - 1)])
