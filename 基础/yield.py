a = lambda x,y : [x,y]
b = (i for i in range(10))
c = (i for i in range(5))

d = map(a,b,c)

print(dir(d))