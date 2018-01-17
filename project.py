from functools import partial


#=======================================================================================================================

def reduce(initial, l, f):
    return reduce(f(initial, l[0]), l[1:], f) if len(l) > 0 else initial

#-----------------------------------------------------------------------------------------------------------------------

def fMap(l, f):
    return reduce([], l, lambda x, y: x + [f(y)])

#-----------------------------------------------------------------------------------------------------------------------

def fFilter(p, l):
    return reduce([], l, lambda x, y: x + [y] if p(y) else x)

#-----------------------------------------------------------------------------------------------------------------------

def loop(p, f, x):
    return x if p(x) else loop(p, f, f(x))

#-----------------------------------------------------------------------------------------------------------------------

def exist(p, l):
    return reduce(False, l, lambda x, y: x or p(y))

#-----------------------------------------------------------------------------------------------------------------------

def find(p, l):
    return None if not exist(p, l) else fFilter(p, l)[0]

#-----------------------------------------------------------------------------------------------------------------------

def near(i):
    return fFilter(lambda x: x >= 0, [i-2, i-1, i, i+1, i+2])

#-----------------------------------------------------------------------------------------------------------------------

def flat_map(rel, l):
    return reduce([], l, lambda x, y : x + rel(y))

#-----------------------------------------------------------------------------------------------------------------------

def fIter(rel, n):
    return lambda x : rel(x) if n == 1 else flat_map(fIter(rel, n-1), x)

#=======================================================================================================================

print(loop(lambda x : x>5, lambda x : x + 1, 3))
print (exist(lambda x : x > 4, [2, 4, 5]))
print(find(lambda x : x>5, [3, 6, 2, 7]))
print(near(1))
print(flat_map(near, [2, 10, 20]))
print(fIter(near, 2)(2))