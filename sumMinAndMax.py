list=[1,2,3,4,5]
sl=list.sort()

print(list,type(list))
small=list[0]
print(small)
big=list[-1]
print(big)
print("========================")
value=0
for i in list:
    value=value+i
print(value)
print("========================")

print("max:",value-big, 'min:',value-small)
print("========================")