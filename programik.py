a = int(input())
b = a.split(',')

print(b, type(b))
for i in range (len(b)):
    b[i] = int(b[i])
lista = [int(i) for i in b]
print (b, type(b))
