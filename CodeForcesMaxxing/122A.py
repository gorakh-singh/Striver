i=input()
flag=0
s=set(i)
if len(s)==2 and "7" in s and "4" in s:
    print("YES")
elif int(i)%4==0 or int(i)%7==0 or int(i)%47==0 or int(i)%74==0 or int(i)%477==0 or int(i)%447==0 or int(i)%474==0 or int(i)%444==0 or int(i)%44==0 or int(i)%77==0:
    print("YES")
else:
    print("NO")
