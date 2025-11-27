import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.differentiate import derivative

from interpolacaoc import (
    newton,
    lagrange,
    polinomial,
)
from regressaoc import regressao
from derivacaoc import dp, dr, dc


def ploti(x, y, num_img=1):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    p = newton(x, y)
    yn = np.polyval(p, x_vals)
    p = lagrange(x, y)
    yl = np.polyval(p, x_vals)
    p = polinomial(x, y)
    yp = np.polyval(p, x_vals)
    spline = CubicSpline(x, y, bc_type="natural")
    ys = spline(x_vals)
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, yn, label="Newton")
    plt.plot(x_vals, yl, label="Lagrange", linestyle="--")
    plt.plot(x_vals, yp, label="Polinomial", linestyle=":")
    plt.plot(x_vals, ys, label="Spline cúbica", linewidth=2)
    plt.scatter(x, y, label="Pontos", zorder=5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolação: Newton, Lagrange, Polinomial e Spline Cúbica")
    plt.legend()
    plt.grid(True, which="both", linestyle=":")
    plt.tight_layout()
    plt.savefig(f"semana 13/grafico_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()

def plotr(x, y, v, num_img=1):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    y_vals = np.zeros_like(x_vals, dtype=float)
    A = regressao(x, y, v)
    for p, ap in enumerate(A):
        y_vals += ap * (x_vals**p)
    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label="Ajuste linear f(x)")
    plt.title("Ajuste linear por mínimos quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"semana 13/grafico_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    x = np.array(
        [1.5, 2.0, 2.2, 3.0],
        dtype=float,
    )
    y = np.array(
        [4.9, 3.3, 3.0, 2.0],
        dtype=float,
    )

    xr = np.array(
        [1.75, 2.5, 2.75, 3.2],
        dtype=float,
    )

    p = newton(x, y)
    yn = np.polyval(p, xr)

    p = lagrange(x, y)
    yl = np.polyval(p, xr)

    p = polinomial(x, y)
    yp = np.polyval(p, xr)

    spline = CubicSpline(x, y, bc_type="natural")
    ys = spline(xr)

    for xi, n, l, p, s in zip(xr, yn, yl, yp, ys):
        print(f"x = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")

    ploti(x, y, 1)

    # Atividade 2
    print("-- Atividade 2 --")

    x = np.array(
        [0.2, 0.5, 0.7, 1.0],
        dtype=float,
    )
    y = np.array(
        [0.8187, 1.5815, 1.9354, 2.2905],
        dtype=float,
    )

    xr = np.array(
        [0.3, 0.9],
        dtype=float,
    )

    p = newton(x, y)
    yn = np.polyval(p, xr)

    p = lagrange(x, y)
    yl = np.polyval(p, xr)

    p = polinomial(x, y)
    yp = np.polyval(p, xr)

    spline = CubicSpline(x, y, bc_type="natural")
    ys = spline(xr)

    for xi, n, l, p, s in zip(xr, yn, yl, yp, ys):
        print(f"x = {xi:>4}:  N={n: .6f} | L={l: .6f} | P={p: .6f} | S={s: .6f}")

    ploti(x, y, 2)

    # Atividade 3
    print("-- Atividade 3 --")

    x = np.array([1, 1.25, 1.5, 1.75, 2], dtype=float)
    y = np.array([38.0, 40.0, 42.0, 44.0, 46.0], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plotr(x, y, v, 3.1)

    x = np.array([1.0, 1.5, 2, 2.5, 3.0], dtype=float)
    y = np.array([40, 44, 48, 52, 56], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plotr(x, y, v, 3.2)

    x = np.array([1, 1.15, 1.3, 1.45, 1.6], dtype=float)
    y = np.array([36, 39, 42, 45, 48], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plotr(x, y, v, 3.3)

    # Atividade 4
    print("-- Atividade 4 --")

    x = np.array([0.5, 1.1, 1.5, 2.2, 2.5, 3.1], dtype=float)
    y = np.array([5.1, 10.3, 15.2, 20.1, 24.7,30.5], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)
    print(A)
    plotr(x, y, v, 4)

    # Atividade 5
    print("-- Atividade 5 --")    
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4], dtype=float)
    y = np.array([0.00, 0.82, 1.36, 1.60, 1.73], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)
    
    print("f(x) = LdI/dt + RI")
    f=lambda x: A[0]+ x*A[1]
    Vl=0.1*dp(f,0.5,1e-12)+5*f(0.5) 
    print("V(0.5)=", Vl)

    # Atividade 6
    print("-- Atividade 6 --")    
    v = lambda x: np.column_stack((np.ones(len(x)), x,x**2))

    A = regressao(x, y, v)
    
    print("f(x) = LdI/dt + RI")
    f=lambda x: A[0]+ x*A[1]+x**2*A[2]
    Vl=0.1*dr(f,0.5,1e-12)+5*f(0.5) 
    print("V(0.5)=", Vl)

    # Atividade 7
    print("-- Atividade 7 --")    
    v = lambda x: np.column_stack((np.ones(len(x)), x,x**2,x**3))

    A = regressao(x, y, v)
    
    print("f(x) = LdI/dt + RI")
    f=lambda x: A[0]+ x*A[1]+x**2*A[2]+x**3*A[3]
    Vl=0.1*dr(f,0.5,1e-12)+5*f(0.5) 
    print("V(0.5)=", Vl)


if __name__ == "__main__":
    main()

