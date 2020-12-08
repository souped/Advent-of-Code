with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input8.txt") as f: a=[l.strip() for l in f.readlines()]

def read_instruction(instruction, acc, index):
    operation, value = instruction
    if operation == "acc":
        new_acc = acc+value
        index += 1
    if operation == "jmp":
        index += value
    if operation == "nop":
        index += 1
    return new_acc, index

def part1(a):
    acc = 0
    index = 0
    ins = set()
    while index < len(a):
        s = a[index]
        if index in ins: break
        ins.add(index)
        acc+=int(s[4:]) if "acc" in s else 0
        index += int(s[4:]) if "jmp" in s else 1
    return index, acc

def part2(a):
    completed = {}
    for index, value in {i:v for i,v in enumerate(a) if v[:3] in ["jmp","nop"]}.items():
        acopy = list(a)
        acopy[index] = acopy[index].replace("jmp", "nop") if "jmp" in acopy[index][:3] else acopy[index].replace("nop", "jmp")
        temp = part1(acopy)
        completed[index] = temp
    return {k:v for k,v in completed.items() if v[0] == len(a)}

def main():
    print(part1(a))
    print(part2(a))
    
        
    

main()