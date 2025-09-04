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

def f4(x, V, R):
    IR = 1e-12  # corrente de saturação (A)
    T = 300.0  # temperatura (K)
    k = 1.38064852e-23  # constante de Boltzmann (J/K)
    q = 1.60217662e-19  # carga do elétron (C)
    vt = k * T / q  # tensão térmica (V)
    return R * IR * (np.exp(x / vt) - 1) + x - V

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

    print("-- Atividade 4 --")
    VRs = [
        (30, 1e3, 0, 1),
        (3, 1e3, 0, 1),
        (3, 1e4, 0, 1),
        (0.3, 1e3, 0, 0.5),
        (-0.3, 1e3, -1, 0),
        (-30, 1e3, -40, 0),
        (-30, 1e4, -40, 0),
    ]
    for V, R, a, b in VRs:
        try:
            f4_vrs = lambda x: f4(x, V, R)
            r = newton_raphson(b, f4_vrs)
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> vd = {r:.3f} V")
        except ValueError as error:
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> {error}")

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
