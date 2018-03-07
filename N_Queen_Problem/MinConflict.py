import random
import time

count = 0
start_time = time.time()

def nqueens(nr):
    show(min_conflicts(list(range(nr)), nr), nr)


def show(soln, nr):
    for i in range(nr):
        row = [' ~ '] * nr
        for col in range(nr):
            if soln[col] == nr - 1 - i:
                row[col] = ' Q '
        print(''.join(row))
end_time = time.time()


def min_conflicts(soln, nr, iters=1000):

    def random_pos(li, filt):
        return random.choice([i for i in range(nr) if filt(li[i])])

    for k in range(iters):

        confs = find_conflicts(soln, nr)
        if sum(confs) == 0:
            return soln
        col = random_pos(confs, lambda elt: elt > 0)
        vconfs = [hits(soln, nr, col, row) for row in range(nr)]
        soln[col] = random_pos(vconfs, lambda elt: elt == min(vconfs))



def find_conflicts(soln, nr):
    global count
    count = count + 1
    return [hits(soln, nr, col, soln[col]) for col in range(nr)]


def hits(soln, nr, col, row):

    total = 0
    for i in range(nr):
        if i == col:
            continue
        if soln[i] == row or abs(i - col) == abs(soln[i] - row):
            total += 1
    return total


BOARD_SIZE = input('Please enter Board Size: ')
nqueens(BOARD_SIZE)
print("\nTime taken to complete: %s s" % (((end_time - start_time)) * 1))
print("No. of assignments: %s" % count)