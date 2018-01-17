from functools import partial

#=======================================================================================================================

def selection_sort(l, f):
    length = len(l)
    for current_index in range(0, length):
        index_min = current_index
        for j in range(current_index + 1, length):
            if f(l[index_min], l[j]):
                index_min = j
        if index_min != current_index:
            temp = l[current_index]
            l[current_index] = l[index_min]
            l[index_min] = temp
    return l

#***********************************************************************************************************************

def reduce(initial, l, f):
    return reduce(f(initial, l[0]), l[1:], f) if len(l) > 0 else initial

#***********************************************************************************************************************

def fMap(l, f):
    return reduce([], l, lambda x, y: x + [f(y)])

#***********************************************************************************************************************

def fFilter(l, f):
    return reduce([], l, lambda x, y: x + [y] if f(y) else x)

#***********************************************************************************************************************

def fProperty(l, f):
    return reduce(False, l, lambda x, y: x or f(y))

#**********************************************************************************************************************

def fSommeSquaresEven (l):
    return reduce(0, fMap(fFilter(l, lambda x : x%2 == 0), lambda x : x*x), lambda x, y : x+y)

#**********************************************************************************************************************

def fMapPartial (integers):
    return fMap(integers, lambda x : partial(lambda y : y+x))

#=======================================================================================================================

print(selection_sort([3, 7, 1], lambda x, y: x > y))
print(reduce(1, [2, 2, 3], lambda x, y: x + y))
print(fMap([2, 2, 4], lambda x: x + 1))
print(fFilter([2, 3, 4, 5, 2], lambda x : x > 3))
print (fSommeSquaresEven([1, 3, 2]))