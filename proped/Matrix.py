import numpy as np 
class Matrix:
  #
  def __init__(self,M,M1):
    # esta función suma matriz de arreglos 2D
    self.M=M # introducida por el usuario
    self.M1=M1 # introducida por el usuario
    self.F=np.zeros_like(self.M) # matriz final 
    self.F1=np.zeros_like(self.M)
    self.P=np.zeros_like(self.M)
    self.Pot=np.zeros_like(self.M)
    self.__i=0
    self.__jaja=125

  def sumaM(self):
    for i in range(self.M.shape[0]):
      #i=0,1 
      for j in range(self.M.shape[1]):
        #j=0,1
        self.F[i][j]= self.M[i][j]+self.M1[i][j]
    return self.F

  def __encap(self):
    print(self.__jaja)

  def transpuesta(self):
    for i in range(self.M.shape[0]):
      for j in range(self.M.shape[0]):
        self.F1[i][j]=self.M[j][i]

    return self.F1

  def producto(self,A,N):
    for i in range(self.M.shape[0]):
      for j in range(self.M.shape[1]):
        for k in range(self.M.shape[1]):
          self.P[i][j] +=  (self.M[i][k] * self.M1[k][j]) 

    return self.P

  def potencia(self,n,A,N):
    # n=2, 2-1
    # i= 0, 1
    for i in range(n):
      print(i)
      self.Pot=self.producto(A,N)
    return self.Pot