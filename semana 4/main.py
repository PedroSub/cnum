import numpy as np
import matplotlib.pyplot as plt
import math

from algoritmos import bissecao

# Definição da função
def f1(x):
    return x**3 - x - 2
def f2(x):
    return x**(1/2) - np.cos(x)
def f3(x):
    sinxx=np.sin(x**2)
    return 5*sinxx-np.exp(x/10)
def f4(x, V, R):
    IR = 1e-12  # corrente de saturação (A)
    T = 300.0  # temperatura (K)
    k = 1.38064852e-23  # constante de Boltzmann (J/K)
    q = 1.60217662e-19  # carga do elétron (C)
    vt = k * T / q  # tensão térmica (V)
    return R * IR * (np.exp(x / vt) - 1) + x - V

# Função da Atividade5
def f5(x):
    d = 500
    fmax = 50
    return (x*(np.cosh(d/(2*x))-1)) - fmax

# Função da Atividade6
def f6(x):
    F = 1e3
    L = 100e-3
    R = 1e3
    T = 2 * np.pi * F * L / R
    A = np.atan(T)
    return np.sin(x - A) + np.sin(A) * np.exp(-x / T)


def plot(f,x1,x2,d=0.1, number=1):
    # Intervalo para plotar
    x_vals = np.arange(x1, x2, d)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)  # eixo x
    plt.axvline(0, color="black", linewidth=1)  # eixo y
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.title("Visualização da função f(x)")

    # Salvar gráfico como imagem
    plt.savefig(f"semana 4/bissecao_{number}.png", dpi=120, bbox_inches="tight")
    plt.close()

def main():
    print("-- Atividade 1 --")
    plot(f1,-2,3,1)
    r, i = bissecao(f1, 1, 2, 1e-15)
    print(f"raiz = {r} , i = {i}")
    print("-- Atividade 2 --")
    #plot(f2,0,8,2)
    r, i = bissecao(f2, 0, 1, 1e-15, 4)
    print(f"raiz = {r} , i = {i}")
    print("-- Atividade 3 --")
    #plot(f3,0,3,3)
    r, i = bissecao(f3, 0.4, 0.5, 1e-5)
    print(f"raiz 1 = {r} , i = {i}")
    r, i = bissecao(f3, 1.6, 1.8, 1e-5)
    print(f"raiz 2 = {r} , i = {i}")
    r, i = bissecao(f3, 2.5, 2.7, 1e-5)
    print(f"raiz 3 = {r} , i = {i}")
    print("-- Atividade 4 --")
    f4_vr = lambda x: f4(x, 30, 1e3)
    plot(f4_vr, 0, 1, number=4)
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
            r, i = bissecao(f4_vrs, a, b, 1e-8)
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> vd = {r:.3f} V")
        except ValueError as error:
            print(f"V={V} V, R={R/1e3:.0f}kΩ --> {error}")
    # Atividade 5
    print("-- Atividade 5 --")
    plot(f5, 550, 650, number=5)
    r, i = bissecao(f5, 550, 650, 1e-4, iter=1e2)
    print(f"raiz = {r:.4} , i = {i}")
    # Atividade 6
    print("-- Atividade 6 --")
    a = 212 * np.pi / 180
    b = 213 * np.pi / 180
    plot(f6, a, b, d=0.01,number=6)
    r, i = bissecao(f6, a, b, 1e-4, iter=1e2)
    r_deg = r * 180 / np.pi
    print(f"raiz = {r_deg:.4} , i = {i}")

if __name__ == "__main__":
    main()

