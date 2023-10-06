import numpy as np

# array bidimensional
array_bi = []

minha_array = np.genfromtxt('minha_array.csv', delimiter = ';', dtype = 'int8')
print(minha_array)

# obter dados estatísticos diferentes
# pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis

# valor mínimo para cada linha
minha_array.min(axis=1)

# valor máximo para cada coluna
minha_array.max(axis=0)

# valor médio da array
minha_array.mean()

# definindo uma matriz 
minha_matriz = np.array([[8,4,2,9],
                         [4,5,6,10],
                         [4,2,8,3],
                         [5,3,6,8]])
minha_matriz

# obter a transposta da matriz e realizar uma operação com ela
minha_matriz_t = np.array(minha_matriz).T
minha_matriz_t

c = 2
igualdade1 = np.array(2*minha_matriz).T
igualdade1

igualdade2 = 2*minha_matriz_t
igualdade2

# Logo, provamos que (cA)^t = cA^t.

# realizar um produto escalar entre duas matrizes ou de um array com uma matriz
prod_escalar = np.dot(minha_array,minha_matriz)
prod_escalar

# criar um filtro para a sua matriz
(minha_matriz%2==0)

# realizar alguma operação aritmética (número com matriz, array com matriz, etc.)
soma_matriz = minha_matriz+minha_matriz_t
soma_matriz