from math import cos, sin, pi

directions = dict(zip("NESW", (1j, 1, -1, -1j)))
rotations = dict(zip("LR", (1j, -1j)))

def part1(a):
    location = complex(0,0)
    facing = complex(1,0)
    for di, v in a:
        if di in directions:
            location += directions[di] * v
        elif di in rotations:
            facing *= rotations[di] ** (v // 90)
        elif di == "F":
            location += facing * v
    print(location)
    return round(abs(location.real) + abs(location.imag))


def main():
    with open("O:\\Coding\\Python\\Advent-of-Code\\inputsaoc\\input12.txt") as f: a = [(v[0],int(v[1:])) for v in f.readlines()]
    print(part1(a))
main()

