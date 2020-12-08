with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input6.txt") as f:
    a = [line.replace("\n", " ") for line in f.read().split("\n\n")]

a1 = 0
a2 = 0
for l in [set(line.replace(" ", "")) for line in a]:
    a1+=len(l)

for l in [l.strip() for l in a]:
    d = dict((el,0) for el in set(l.replace(" ", "")))
    for c in l.replace(" ", ""):
        d[c]+=1
    f = len(l.split(" ")) # aantal personen
    e = [v for c,v in d.items() if v == f]
    if len(e) != 0 and f == max(e): a2+= len(e)


print(a1,a2)
