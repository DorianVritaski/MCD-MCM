from src.logica.FaltanParametros import FaltanParametros

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCD(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        elif len(self.__numeros) > 1:
            return self.MCDMasDosNumeros()
        else:
            return 0

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCDMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los elementos deben ser enteros.")

        cantidadNumeros = len(self.__numeros)
        mcd = self.MCD(self.__numeros[0], self.__numeros[1])
        i = 0
        while i < (cantidadNumeros - 2):
            mcd = self.MCD(mcd, self.__numeros[i + 2])
            i = i + 1
        return mcd

    def calcularMCM(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError("Todos los elementos deben ser enteros.")

        if len(self.__numeros) < 2:
            raise FaltanParametros

        def MCM(a, b):
            return abs(a * b) // self.MCD(a, b)

        mcm = self.__numeros[0]
        for i in range(1, len(self.__numeros)):
            mcm = MCM(mcm, self.__numeros[i])

        return mcm
