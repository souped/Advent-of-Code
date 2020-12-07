import re

with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input7.txt") as f:
    a = f.readlines()

s = "shiny gold"
regoutbag = re.compile(r"^([a-z]+ [a-z]+)")
regsubbags = re.compile(r"(\d+) ([a-z]+ [a-z]+)")

bags = {re.match(regoutbag, line).group(0): re.findall(regsubbags, line) for line in a}

def check_bag(bag_color):
    for bag, subbags in bags.items():
        if any(sub_bag_color == bag_color for temp, sub_bag_color in subbags):
            yield bag
            yield from check_bag(bag)

print(len(set(check_bag(s))))

def bag_contains(bag_color):
    return 1 + sum(int(c) * bag_contains(col) for c, col in bags[bag_color])

print(bag_contains(s)-1)