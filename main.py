from random import randint
from math import sqrt

def make_arrive ():
    sides = []
    for i in range(1000000):
        sides += '0'
    for i in range(1000000):
        sides[i] = randint(1, 1000000)
        #print(sides[i])
    return sides

def check (a, b, c):
    if a+b <= c:
        return False
    if b+c <= a:
        return False
    if a+c <= b:
        return False
    return True

def choose_max(sides):
    if len(sides) >= 3:
        i = 0
        max = [0, 0, 0]
        for side in sides:
            if max[i] <= side:
                max[i] = side
                if i == 2:
                    i = 0
                else:
                    i += 1
        if check(max[0], max[1], max[2]) == True:
            return max
        else:
            if ((max[0]>max[1]) & (max[0]>max[2])):
                wrong_side = max[0]
            elif ((max[1]>max[0]) & (max[1]>max[2])):
                wrong_side = max[1]
            else:
                wrong_side = max[2]
            sides = delete_side(sides, wrong_side)
            max = choose_max(sides)
            return max
    else:
        return False

def delete_side(sides, wrong_side):
    #print(wrong_side, sides)
    new_sides = []
    side_deleted = 0
    for n in range(len(sides)-1):
        new_sides += '0'
        #print(new_sides)
    i = 0
    for side in sides:
        #print(side)
        if ((side == wrong_side) & (side_deleted == 0)):
            side_deleted = 1
        else:
            new_sides[i] = side
            #print(new_sides)
            i += 1
    return new_sides

if __name__ == '__main__':
    #max = choose_max([3, 4, 5, 50, 100])
    sides = make_arrive()
    max = choose_max(sides)
    if max != False:
        p = (max[0] + max[1] + max[2])/2
        print(f"Triangle sides: {max[0]}, {max [1]}, {max[2]}")
        s = sqrt(p * (p-max[0]) * (p-max[1]) * (p-max[2]))
        print(f"Maximum area of triangle:{s}")
    else:
        print("You can't make a triangle with this sides!")


