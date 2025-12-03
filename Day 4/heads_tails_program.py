# Write a code that prints "Heads" or "Tails" randomly when run.

import random

toss = random.randint(0,1)
output = ""

if toss == 1:
    output = "Heads"
else:
    output = "Tails"

print(f"The Toss outcome is = {output}")