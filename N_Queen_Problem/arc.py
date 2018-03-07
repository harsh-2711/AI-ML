import sys
import time

BOARD_SIZE = input('Please enter Board Size: ')
start_time = time.time()
count = 0
queue = []
dom = {}

def queen(A, a, B, b):
    return A == B or (a != b and A + a != B + b and A - a != B - b)


def neighbors(xi):
    return set(range(BOARD_SIZE)) - {xi}


def arcons(queens, queue):
    if len(queue) == 0:
        queue = [(Xi, Xk) for Xi in range(BOARD_SIZE) for Xk in neighbors(Xi)]
        while queue:
            (x1, x2) = queue.pop()
            if unconsist(queens, x1, x2):
                if not dom[x1]:
                    return False
                for xk in neighbors(x1):
                    queue.append((xk, x1))
        return True


def unconsist(queens, x1, x2):
    removed = False
    for x in dom[x1]:
        if all(not queen(x1, x, x2, y) for y in dom[x2]):
            dom[x1].remove(x)
            removed = True
    return removed


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


ans = arcons([0] + [1], queue)
end_time = time.time()
print_board(ans)
print("\nTime taken to complete: %s s" % (((end_time - start_time)) * 1))
print("No. of assignments: %s" % count)