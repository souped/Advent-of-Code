from math import factorial

def quicksortinplace(a, lo=0, hi=None):
    if hi is None: hi = len(a) - 1
    if lo < hi:
        piv = a[hi]
        i = lo
        j = lo
        while j < hi:
            if a[j] < piv:
                a[i], a[j] = a[j], a[i]
                if i < hi:
                    i+=1
            j+=1
        a[i],a[hi] = a[hi], a[i]
        quicksortinplace(a, lo, i-1)
        quicksortinplace(a, i+1, hi)

def part1(a):
    diffs1 = 0
    diffs3 = 0
    for i in range(len(a)-1):
        diff = abs(a[i+1] - a[i])
        if diff == 1: diffs1+=1
        if diff == 3: diffs3+=1
        if diff > 3: print(f"er is iets fout")
    return diffs1*diffs3

def part2(a, count=0, index = None):
    if index is None: index = len(a)-2
    if index < len(a) - 1 and index > 1:
        diff = abs(a[index]-a[index-1])
        diff2= abs(a[index]-a[index-2])
        if diff < 2 and diff2 < 3:
            del a[index-1]
            return part2(a,count+1,index-1)

    return count
            
def main():
    with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input10.txt") as f: a = [int(v) for v in f.readlines()]
    a.append(0)
    a.append(max(a)+3)
    quicksortinplace(a)
    b = [0,1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
    c = [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, 52]
    print(part1(a))
    print(part2(list(a)))

main()