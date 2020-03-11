# Lucky Unicorn Decomposition Step 3
# Generate a random token

# To do
# Set up starting amount
# Choose 100 tokens (ie: play 100 rounds and...
#   count # of unicorns and multiple by 5
#   count # of horse / zebra and multiple by 0.5
#   count # of donkeys
#   work out total won / lost

import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

unicorn_count = 0
zebra_horse_count = 0
donkey_count = 0

for item in range(0, HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebra_horse_count += 1

        print(chosen)

print("**** Win / Loss Calculations*****")
print("# Unicorns: {}".format(unicorn_count))
print("# Zebra / Horses: {}".format(zebra_horse_count))
print("# Donkeys: {}".format(donkey_count))
