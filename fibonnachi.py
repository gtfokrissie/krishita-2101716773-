n = 10

arr=[]

a=b= 0
c = 1
for i  in range(n):
    a = b + c
    c = b
    b = a
    arr.append(str (a))
print(",".join(arr))
