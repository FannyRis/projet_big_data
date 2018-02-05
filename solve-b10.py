# Project big data : Functional programming
#
# Date : 05/01/2018
# Authors : Amédée ROY and Fanny RISBOURG

import sys

#=======================================================================================================================

sys.setrecursionlimit(50000)

# The state we want to reach at Jigsaw
final_state = ((1, 2, 3),
               (4, 5, 6),
               (7, 8, None))

# Our initial state at Jigsaw. Cannot be too far from the final state on my computer or the program ends wth a segfault
initial_state = ((2, None, 6),
                 (1, 3, 4),
                 (7, 5, 8))

#=======================================================================================================================

def reduce(initial, l, f):
    return reduce(f(initial, l[0]), l[1:], f) if len(l) > 0 else initial

#-----------------------------------------------------------------------------------------------------------------------

# Question 1
def loop(p, f, x):
    return x if p(x) else loop(p, f, f(x))

#-----------------------------------------------------------------------------------------------------------------------

# Question 2
def exist(p, l):
    return False if not l else p(l[0]) or exist(p, l[1:])

#-----------------------------------------------------------------------------------------------------------------------

#  Question 3
def find(p, l):
    return None if not l else l[0] if p(l[0]) else find(p, l[1:])

#-----------------------------------------------------------------------------------------------------------------------

# Question 4
def near(i):
    return [i - 2, i - 1, i, i + 1, i + 2]

#-----------------------------------------------------------------------------------------------------------------------

# Question 5
def flat_map(rel, l):
    return reduce([], l, lambda x, y : x + rel(y))

#-----------------------------------------------------------------------------------------------------------------------

# Question 6
def fIter(rel, n):
    return lambda x : [x] if n == 0 else flat_map( rel, fIter(rel, n-1)(x) )

#-----------------------------------------------------------------------------------------------------------------------

# Question 7
def solve(rel, p, x):
    return find(p, loop(lambda y : exist(p, y), lambda l: flat_map(rel, l), [x]))

#-----------------------------------------------------------------------------------------------------------------------

# Question 8
def solve_path(rel, p, i):
    return solve(lambda x : [ x + (y,) for y in rel(x[-1])], lambda x : p(x[-1]), (i,))

#-----------------------------------------------------------------------------------------------------------------------

# Bonus : application with Jigsaw

# Relation between states in Jigsaw
def reach(s) :
    states = []
    next_state = [list(x) for x in s]
    for i in range(3):
        for j in range(3):
            if not s[i][j] :
                if i > 0:
                    next_state[i][j] = s[i - 1][j]
                    next_state[i-1][j] = None
                    states.append(tuple([tuple(x) for x in next_state]))
                    next_state = [list(x) for x in s]
                if i < 2:
                    next_state[i][j] = s[i + 1][j]
                    next_state[i+1][j] = None
                    states.append(tuple([tuple(x) for x in next_state]))
                    next_state = [list(x) for x in s]
                if j > 0:
                    next_state[i][j] = s[i][j - 1]
                    next_state[i][j-1] = None
                    states.append(tuple([tuple(x) for x in next_state]))
                    next_state = [list(x) for x in s]
                if j < 2:
                    next_state[i][j] = s[i][j + 1]
                    next_state[i][j+1] = None
                    states.append(tuple([tuple(x) for x in next_state]))
                    next_state = [list(x) for x in s]
    return states

#-----------------------------------------------------------------------------------------------------------------------

# Function to pretty print a tuple of 3*3 with None values
def pretty_print(tup):
    for row in range(3) :
        s = ''
        for column in range(3) :
            if not tup[row][column] :
                s += '  '
            else :
                s += str(tup[row][column]) + ' '
        print(s)

#-----------------------------------------------------------------------------------------------------------------------

# functions partially working with sets in order to limit redundancies

def flat_map_set(rel, l):
    return set(reduce([], l, lambda x, y : x + rel(y)))

#-----------------------------------------------------------------------------------------------------------------------

def solve_set(rel, p, x):
    return find(p, loop(lambda y : exist(p, y), lambda l: list(flat_map_set(rel, l)), [x]))

#-----------------------------------------------------------------------------------------------------------------------

def solve_path_set(rel, p, i):
    return solve_set(lambda x : [ x + (y,) for y in rel(x[-1])], lambda x : p(x[-1]), (i,))

#=======================================================================================================================

result = solve_path_set(reach, lambda x : x == final_state, initial_state)

for index, state in enumerate(result) :
    print("\n")
    if index == 0 :
        print("Initial state : ")
    elif state == final_state :
        print("Final state : ")
    else:
        print("Step %d :" % index)
    pretty_print(state)