import numpy as np

arr = np.array([1,2,3,4,5])

#opreaciones matematicas

print("array", arr)
print("suma", arr.sum())
print("promedio", arr.mean())
print("maximos", arr.max())
print("minimos", arr.min())

#dos array
a = np.array([1,2,3])
b = np.array([4,5,6])
print("suma", a+b)
print("producto", a*b)
print("Raiz cuadrada", np.sqrt(a))

#matriz 2x2
matriz= np.array([[1,2],[3,4]])
print("Matriz")
print( matriz)
print("Matriz transpuesta")
print( matriz.T)
 
print(np.__version__)