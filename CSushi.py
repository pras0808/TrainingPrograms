n=int(input("Enter the number of rice:"))
m=int(input("Enter the number of toppings:"))
a=[]
b=[]
count=0
used=set()
for i in range(n):
    a1=int(input("Enter weight of rice :"))
    a.append(a1)
for i in range(m):
    b1=int(input("Enter weight of toppings :"))
    b.append(b1)
for i in range(n):
    for j in range(m):
        if b[j] not in used and b[j]<=(a[i]*2):
            count+=1
            used.add(b[j])
            print(used)
            break
print(count)
