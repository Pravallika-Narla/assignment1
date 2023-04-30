str=input("enter a string: ")
lwr_str=str.lower()
unique_letters=set(lwr_str)
len=len(unique_letters)
print("unique_letters = ",end=" ")
for k in unique_letters:
    print(k,end="")
    if len-1>0:
        print(",",end="")
        len=len-1