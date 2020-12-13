directions = dict(zip("NESW", (1j, 1, -1j, -1)))
rotations = dict(zip("LR", (1j, -1j)))

def part1(a):
    location = complex(0,0)
    facing = complex(1,0)
    for di, v in a:
        if di in directions:
            location += directions[di] * v
            continue
        elif di in rotations:
            facing *= rotations[di] ** (v // 90)
            continue
        elif di == "F":
            location += facing * v
            continue
    return round(abs(location.real) + abs(location.imag))

def part2(a):
    wp = complex(10, 1)
    ship = complex(0,0)
    for di, v in a:
        if di in directions:
            wp += directions[di] * v
            
        elif di in rotations:
            wp *= rotations[di] ** (v // 90) # if di == "R" else rotations[di] ** (-v // 90)
            
        elif di == "F":
            ship += wp * v
            
        print(f"{wp}")
    return round(abs(ship.real) + abs(ship.imag))

def main():
    with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input12.txt") as f: a = [(v[0],int(v[1:])) for v in f.readlines()]
    print(part1(a))
    print(part2(a))
main()

