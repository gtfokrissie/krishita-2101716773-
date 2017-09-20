n = 10

arr=[]

a=b= 0
c = 1
i= 0
while i< n:
    a = b + c
    c = b
    b = a
    arr.append(str (a))
    i= i + 1
print(",".join(arr))
