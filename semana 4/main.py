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
def f4(r,v,vd):
    return  vd+r*id-v

def plot(f,x1,x2, number=1):
    # Intervalo para plotar
    x_vals = np.arange(x1, x2, 0.1)
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
    #plot(f1,-2,3,1)
    r, i = bissecao(f1, 1, 2, 1e-15)
    print(f"raiz = {r} , i = {i}")
    print("-- Atividade 2 --")
    #plot(f2,0,8,2)
    r, i = bissecao(f2, 0, 1, 1e-15, 4)
    print(f"raiz = {r} , i = {i}")
    print("-- Atividade 3 --")
    plot(f3,0,3,3)
    r, i = bissecao(f3, 0.4, 0.5, 1e-5)
    print(f"raiz 1 = {r} , i = {i}")
    r, i = bissecao(f3, 1.6, 1.8, 1e-5)
    print(f"raiz 2 = {r} , i = {i}")
    r, i = bissecao(f3, 2.5, 2.7, 1e-5)
    print(f"raiz 3 = {r} , i = {i}")

if __name__ == "__main__":
    main()

