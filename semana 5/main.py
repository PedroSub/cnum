import numpy as np

from algoritmos import (
    pontofixo,
    newton_raphson,
    secante,
)

f1 = lambda x: np.e**x - x - 2
g1 = lambda x: np.e**x - 2

f2 = lambda x: np.cos(x) -x**2 
g2 = lambda x:  np.sqrt(np.cos(x)) 

f3 = lambda x: np.e**(-x**2) - 2*x
g3 = lambda x:  (np.e**(-x**2))/2

f4 = lambda x: 

f5 = lambda x: (x*(np.cosh(500/(2*x))-1)) - 50
g5 = lambda x:  x*(np.cosh(500/(2*x))) - 50

F6 = 1e3
L6 = 100e-3
R6 = 1e3
T6 = 2 * np.pi * F6 * L6 / R6
A6 = np.atan(T6)

f6 = lambda x: np.sin(x - A6) + np.sin(A6) * np.exp(-x / T6)
g6 = lambda x:  T6*np.log(np.sin(x - A6) + np.sin(A6))


def main():
    # Atividade 1
    print("-- Atividade 1 --")
    r = pontofixo(-1.8, g1)
    print(f"raiz ponto fixo = {r}")
    r = newton_raphson(-1.8, f1, df=lambda x: np.e**x - 1)
    print(f"raiz newton-raphson df = {r}")
    r = newton_raphson(-1.8, f1)
    print(f"raiz newton-raphson = {r}")
    r = secante(-1.8, -1.7, f1)
    print(f"raiz secante = {r}")

    print("-- Atividade 2 --")
    r = pontofixo(1, g2)
    print(f"raiz ponto fixo = {r}")
    r = newton_raphson(1, f2, df=lambda x: -np.sin(x)-2*x)
    print(f"raiz newton-raphson df = {r}")
    r = newton_raphson(1, f2)
    print(f"raiz newton-raphson = {r}")
    r = secante(1, 0.5, f2)
    print(f"raiz secante = {r}")
    
    print("-- Atividade 3 --")
    r = pontofixo(0.5, g3)
    print(f"raiz ponto fixo = {r}")
    r = newton_raphson(0.5, f3, df=lambda x: -2*x*(-x**2)*(np.e**(-x**2)) - 2)
    print(f"raiz newton-raphson df = {r}")
    r = newton_raphson(0.5, f3)
    print(f"raiz newton-raphson = {r}")
    r = secante(0.5, 0.4, f3)
    print(f"raiz secante = {r}")

    print("-- Atividade 5 --")
    r = pontofixo(630, g5)
    print(f"raiz ponto fixo = {r}")
    r = newton_raphson(630, f5, df=lambda x: np.cosh(500/(2*x))+x*(-500/(2*x**2))*np.sinh(500/(2*x))-1)
    print(f"raiz newton-raphson df = {r}")
    r = newton_raphson(630, f5)
    print(f"raiz newton-raphson = {r}")
    r = secante(630, 640, f5)
    print(f"raiz secante = {r}")

    print("-- Atividade 6--")
    r = newton_raphson(210, f6, df=lambda x: np.cos(x - A6) - (np.sin(A6) * np.exp(-x / T6))/T6)
    print(f"raiz newton-raphson df = {r}")
    r = newton_raphson(210, f6)
    print(f"raiz newton-raphson = {r}")



if __name__ == "__main__":
    main()
