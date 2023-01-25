def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

list1 = []

list2 = []

for i in range(499, 1001):
	list1.append(i)

for i in range(1, 501):
	list2.append(i) 

# print(list1)
print('List 1 : ', list1)
print('List 2 : ', list2)

num = multiplyList(list1)

den = multiplyList(list2)

print('Multiplication : ', num)

ans = num / den

print('Check : ', ans)

print('Ans : ', ans * (0.5**10))
