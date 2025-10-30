import numpy as np
import matplotlib.pyplot as plt

from bissecaoc import bissecao
from gaussc import (
    lu,
    jacobi,
    seidel,
)

# Definição da função
def f1(x):
    return (5.67e-8)*x**4+0.4*(x-272.975)-500.125

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
    plt.savefig(f"semana 8/bissecao_{number}.png", dpi=120, bbox_inches="tight")
    plt.close()

from newtonraphsonc import (
    G,
    GN,
    fixed_point,
)

def main():
    # Atividade 1
    print("-- Atividade 1 --")
    #plot(f1,100,500,10)
    r, i = bissecao(f1, 300, 310, 1e-15)
    print(f"raiz = {r} , i = {i}")

    print("-- Atividade 2 --")
    A = np.array(
    [[17, -2, -3], 
    [-5, 21, -2], 
    [-5, -5, 22]], dtype=float)
    B = np.array([500, 200, 300], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-8)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)

    print("-- Atividade 3 --")
    A = np.array([[20, 10], [10, 20]], dtype=float)
    B = np.array([100, 100], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)
    I=np.sum(X)
    print(f"Ir3=I1+I2= {I:.4f}")

    print("-- Atividade 4 --")

    def F(x):
        x1, x2 = x
        return np.array(
            [
                x1**4 +0.06823*x1 - x2**4 -0.05848*x2 -0.01753,
                x1**4 +0.05848*x1 - 2*x2**4 -0.11696*x2 -0.00254,
            ],
            dtype=float,
        )

    def J(x):
        x1, x2 = x
        return np.array(
            [
                [4*(x1**3) +0.06823,- 4*(x2**3) -0.05848],
                [4*(x1**3) +0.05848, - 8*(x2**3) -0.11696],
            ],
            dtype=float,
        )

    x = np.array([1.0, 1.0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

if __name__ == "__main__":
    main()
