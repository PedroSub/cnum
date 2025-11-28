import numpy as np
from scipy.integrate import quad

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)
def integral_composta_n(metodo, f, a, b, N):
    
    if metodo == medio:

        M = N
        h = (b - a) / M
        
        s = 0.0
        for i in range(M):
            x_i = a + i * h
            s += h * f(x_i + h / 2)
        return s
    

    M = N - 1
    h = (b - a) / M
    
    if metodo == trapezio:

        s = f(a) + f(b)
        for i in range(1, M):
            x_i = a + i * h
            s += 2 * f(x_i)
        return s * h / 2
    
    elif metodo == simpson:

        if M % 2 != 0:
            print(f"Aviso: A regra de Simpson composta requer um número par de subintervalos. N={N} (M={M})")
            return 0.0
            
        s = f(a) + f(b)
        for i in range(1, M):
            x_i = a + i * h
            if i % 2 == 0:
                s += 2 * f(x_i)
            else:
                s += 4 * f(x_i)
        return s * h / 3
    
    else:
        return 0.0



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
    f = lambda x: np.exp(4-(x**2))
    n = np.array([3, 5 ,7 ,9])
    for inter in n:
        r = integral_composta_n(medio,f, a, b, inter)
        print(f"Ponto medio = {r:.8}")
        r = integral_composta_n(trapezio,f, a, b, inter)
        print(f"Trapezio = {r:.8}")
        r= integral_composta_n(simpson,f, a, b, inter)
        print(f"Simpson = {r:.8}")
    
    
    
    
    


if __name__ == "__main__":
    main()
