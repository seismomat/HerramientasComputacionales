from Data import Data
from Dataa import Dataa

class calculadora(Data,Dataa):
	
	def __init__(self):
		self.__datos=1256
		self.__jeje=1232
		Data.__init__(self) # heredando vars y metodos de la clase Data
		Dataa.__init__(self)

	def prueba(self):
		print(self.dato1)

	def imprimir(self):
		print(self.__datos)




if __name__ == "__main__":
	# crear el objeto 
	c=calculadora()

	su=c.sumar()
	print(su)

	su2=c.sumarr()
	print(su2)
