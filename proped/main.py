from Matrix import Matrix

import numpy as np 

A=np.array([[1,2],[3,4]])
B=np.array([[0,0],[3,4]])

D=2*np.eye(2)
Ma1=Matrix(D,D)

pp=Ma1.potencia(2,D,D)

print(pp)

print(Ma1._Matrix__jaja)
Ma1._Matrix__encap()

print(" encapsula")
Ma1.__jaja=121
print(Ma.__jaja)
Ma1.__encap()