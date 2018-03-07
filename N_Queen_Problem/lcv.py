import sys
import time
import numpy as np
from collections import defaultdict

BOARD_SIZE = input('Please enter Board Size: ')
start_time = time.time()
count = 0

def under_attack(col, queens):
    if col in queens:
        return True
    else:
        return bool(any(abs(col - x) == len(queens) - i for i, x in enumerate(queens)))


def LCV(queens, size):
    current_row = len(queens)
    constrainList = np.full((size), size - 1, dtype=np.int)
    length = len(queens)
    if (length == 0):
        for row in range(size):
            if (row - 1 != -1 and row + 1 != size):
                constrainList[row] = size - 1
            else:
                constrainList[row] = size - 2

    else:
        indConstrain = 0
        constrains = buildconstr(queens,size)
        for cols in range(size):
            if (cols not in queens and constrains[length - 1][cols] != -1):
                if (cols - 1 != -1 and constrains[length][cols - 1] != -1):
                    indConstrain += 1
                if (cols + 1 != len(queens) and constrains[length][cols - 1] != -1):
                    indConstrain += 1
                if indConstrain > 1:
                    constrainList[cols] = indConstrain
            else:
                constrainList[cols] = size - 1

    return sorted(range(len(constrainList)), key=lambda k: constrainList[k])


def buildconstr(queens, size):
    track = np.zeros((size, size))
    for i, j in enumerate(queens):
        for x in range(size):
            for y in range(size):
                if (y == j):
                    track[x][y] = -1
                if (x - y == i - j):
                    track[x][y] = -1
                if (x + y == j - i):
                    track[x][y] = -1
    return track


def LCV_solve(queens, n):
    global count
    if n == len(queens):
        return queens
    else:
        constraints = LCV(queens, n)
        for i in constraints:
            if not under_attack(i, queens):
                count += 1
                newqueens = LCV_solve(queens + [i], n)
                if newqueens != []:
                    return newqueens
        return []


def print_board(queens):
    row = 0
    n = len(queens)
    for pos in queens:
        for i in range(pos):
            sys.stdout.write(" ~ ")
        sys.stdout.write(" Q ")
        for i in range((n - pos) - 1):
            sys.stdout.write(" ~ ")
        print

ans = LCV_solve([], BOARD_SIZE)
end_time = time.time()
print_board(ans)
print("\nTime taken to complete: %s s" % (((end_time - start_time)) * 1))
print("No. of assignments: %s" % count)