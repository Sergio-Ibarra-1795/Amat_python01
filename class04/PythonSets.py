c = {'a', 'b' , 'c', 'd'}
print(c)
print(type(c))

c = {"a","b","c","d"}
print(type(c))

# Conjuntos
a = set('abcde')
b = {'b','d','x','y','z'}
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print(a > b)

# Agregar elementos
b.add("a")
print(b)

# Actualiza el conjunto
b.update(set('1234'))
print(b)

# Remover elemento
b.remove('a')
print(b)

b.discard('b')
print(b)

# Eliminar todos lo elementos
#b.clear()
#print(b)

# Eliminar el último elemento
value = b.pop()
print(value)

# Copia de un conjunto
A = b.copy()
print(A)

# Remueve del primer conjunto los elementos que estén en ambos conjuntos
b.difference_update(A)
print(b)

# Remueve del primer conjunto los elementos que no estén en ambos conjuntos
d = {1,2,3}
e = {1,2,3,4,5,6}
f = {7}
#e.intersection_update(d)
#print(e)

# Prueba de no intersección
print(e.isdisjoint(f))

# Regresa todo menos lo que haga intersección
print(e.symmetric_difference(d))
e.symmetric_difference_update(d)
print(e)
