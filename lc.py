count=0
s=0
y=0
x=int(input("Enter a number"))
while x!=0:
    r=x%10
    y=y*10+r
    s=s+r
    x=x//10
    count+=1
print("Number of digits",count)
print("sum of digits",s)
print("Reverse of number",y)