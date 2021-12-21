
# Swap first and last element of a list.
def swapFandL(l):
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    print('list :', l)

l1 = [1, 7, 9, 10]
swapFandL(l1)