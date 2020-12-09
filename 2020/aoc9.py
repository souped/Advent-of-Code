def check_sum(a, n, index):
    sub = [val for i, val in enumerate(a) if i < index and i >= index - n]
    sub2 = set()
    for i in sub:
        for j in sub:
            if j != i:
                sub2.add(i+j)
    
    if len(a) > index and a[index] not in sub2:
        return a[index]
    return check_sum(a,n,index+1)
    
def weaknes(a, w):
    for i in range(len(a)-2):
        r = list()
        while sum(r) < w:
            if i < len(a):
                r.append(a[i])
                i+=1
            else: break
        if sum(r) == w: return min(r) + max(r)
    return -1

def main():
    with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input9.txt") as f: a = [int(v) for v in f.readlines()]
    # b = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
    c = check_sum(a,25,25)
    # d = check_sum(b,5,5)
    print(c)
    print(weaknes(a,c))


main()