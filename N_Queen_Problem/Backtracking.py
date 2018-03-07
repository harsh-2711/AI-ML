import sys
import time

BOARD_SIZE = input('Please enter Board Size: ')
start_time = time.time()
count = 0


def under_attack(col, queens):

    return col in queens or \
           any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))


def rsolve(queens, n):
    global count
    count = count + 1
    if n == len(queens):
        return queens
    else:
        for i in range(n):
            if not under_attack(i, queens):
                newqueens = rsolve(queens + [i], n)
                if newqueens != []:
                    return newqueens
        return []  # FAIL


def print_board(queens):

    row = 0
    n = len(queens)
    for pos in queens:
        for i in range(pos):
            sys.stdout.write(". ")
        sys.stdout.write("Q ")
        for i in range((n - pos) - 1):
            sys.stdout.write(". ")
        print


ans = rsolve([], BOARD_SIZE)
end_time = time.time()
print_board(ans)
print("\nTime taken to complete: %s s" % (((end_time - start_time)) * 1))
print("No. of assignments: %s" % count)