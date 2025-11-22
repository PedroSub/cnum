import numpy as np
from scipy.integrate import quad

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)


def main():
    # Atividade 1
    print("-- Atividade 1 a) --")

    a = 0
    b = 1

    print("f(x) = e^(-x)")
    f = lambda x: np.exp(-x)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")
    
    print("-- Atividade 1 b)--")
    print("f(x) = x^2")
    f = lambda x: x**2
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("-- Atividade 1 c)--")
    print("f(x) = x^3")
    f = lambda x: x**3
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("-- Atividade 1 d)--")
    print("f(x) = x*e^(-x^2)")
    f = lambda x: x*np.exp(-x**2)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("-- Atividade 1 e)--")
    print("f(x) = 1/(x^2 + 1)")
    f = lambda x: 1/(x**2 + 1)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("-- Atividade 1 f)--")
    print("f(x) = x/(x^2 + 1)")
    f = lambda x: x/(x**2 + 1)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    # Atividade 2
    print("-- Atividade 2 --")

    a = 2
    b = 5
    print("f(x) = e^(4-x^2)")
    n = np.array([3.0, 5.0 ,7.0 ,9.0])
    for inter in n:
        h=((b-a)/inter)
        s=h-1
        f = lambda x: np.exp(4-(x**2))
        r = integral(medio, f, a, b,h)
        print(f"Ponto medio = {r:.8}")
        r = integral(trapezio, f, a, b,h)
        print(f"Trapezio = {r:.8}")
        r= integral(simpson, f,  a, b,h)
        print(f"Simpson = {r:.8}")
    
    
    
    
    


if __name__ == "__main__":
    main()
