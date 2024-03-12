from typing import Any

class Nodo:
    def __init__(self, info: Any = None):
        self.info = info
        self.sig = None

aux = Nodo()
aux.info = "Primer nodo"
palabra = input('Ingrese una palabra: ')
naux = aux
while palabra != "":
    nodo = Nodo(palabra)
    naux.sig = nodo
    naux = nodo
    palabra = input('Ingrese una palabra: ')
while aux is not None:
    print(aux.info)
    aux = aux.sig


class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def sumar(self, otro):
        return Polinomio([a + b for a, b in zip(self.coeficientes, otro.coeficientes)])

    def restar(self, otro):
        return Polinomio([a - b for a, b in zip(self.coeficientes, otro.coeficientes)])

    def multiplicar(self, otro):
        resultado = [0] * (len(self.coeficientes) + len(otro.coeficientes) - 1)
        for i, a in enumerate(self.coeficientes):
            for j, b in enumerate(otro.coeficientes):
                resultado[i + j] += a * b
        return Polinomio(resultado)

    def dividir(self, otro):
        if otro.coeficientes[0] == 0:
            raise ValueError("División por cero")
        return Polinomio([a / otro.coeficientes[0] for a in self.coeficientes])

def pedir_polinomio():
    coeficientes = list(map(float, input("Introduce los coeficientes del polinomio, separados por espacios: ").split()))
    return Polinomio(coeficientes)

polinomio1 = pedir_polinomio()
polinomio2 = pedir_polinomio()

print("Suma: ", polinomio1.sumar(polinomio2).coeficientes)
print("Resta: ", polinomio1.restar(polinomio2).coeficientes)
print("Multiplicación: ", polinomio1.multiplicar(polinomio2).coeficientes)
print("División: ", polinomio1.dividir(polinomio2).coeficientes)