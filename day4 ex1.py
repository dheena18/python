a=['apple','banana','pear','papaya']
a.append('mango')
print(a)
a.remove('pear')
print(a)
a=[12,13,23,25,32,11,10]
a.sort()
print("Largest item of the list is",a[-1])
print("Largest item of the list is",a[0])
a=[10,15,16,17,25,23]
b=reversed(a)
print(tuple(b))
a=['apple','pear','banana','papaya']
b=list(a)
print(b)