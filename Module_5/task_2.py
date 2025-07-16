a=[1,2,3,4,5,6,7,8,9,10]
b=[]

i=0
for i in range(0,5):
    b.append(a[i])

print("Original List:",a)
print("Extracted first five elements:",b)

b.reverse()
print("Reversed Extracted elements:",b)