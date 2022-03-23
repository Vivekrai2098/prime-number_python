value=int(input("enter your number i will check is prime or not"))
l=[]
for i in range(1,value+1):
    if value % i == 0:
        l.append(i)

print("the factor is:=",l)
if len(l)>2:
    print("this is not a prime number")
else:
    print("this is the prime number")



