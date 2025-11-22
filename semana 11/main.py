import numpy as np
from scipy.differentiate import derivative

from algoritmos import dp, dr, dc
from regressaoc import regressao


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    print("f(x) = sin(x)")

    f = lambda x: np.sin(x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 2, h1))
    print("h = 0.001 | f'(x)=", dp(f, 2, h2))
    print("h = eps | f'(x)=", dp(f, 2, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 2, h1))
    print("h = 0.001 | f'(x)=", dr(f, 2, h2))
    print("h = eps | f'(x)=", dr(f, 2, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 2, h1))
    print("h = 0.001 | f'(x)=", dc(f, 2, h2))
    print("h = eps | f'(x)=", dc(f, 2, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 2)
    print("f'(x)=", r.df)

    fd = lambda x: np.cos(x)
    print("Derivada analítica:")
    print("f'(x) = cos(x)")
    print("f'(x)=", fd(2))

    print("f(x) = e^(-x)")

    f = lambda x: np.exp(-x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 1, h1))
    print("h = 0.001 | f'(x)=", dp(f, 1, h2))
    print("h = eps | f'(x)=", dp(f, 1, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 1, h1))
    print("h = 0.001 | f'(x)=", dr(f, 1, h2))
    print("h = eps | f'(x)=", dr(f, 1, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 1, h1))
    print("h = 0.001 | f'(x)=", dc(f, 1, h2))
    print("h = eps | f'(x)=", dc(f, 1, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 1)
    print("f'(x)=", r.df)

    fd = lambda x: -np.exp(-x)
    print("Derivada analítica:")
    print("f'(x) = e^(-x)")
    print("f'(x)=", fd(1))

    # Atividade 2
    print("-- Atividade 2 --")

    def f1(x):
        if x == 1:
            return 1.83
        elif x==0.5:
            return 1.05
        elif x==1.5:
            return 2.69
        elif x==4:
            return 6.11
        elif x==4.5:
            return 7.06
        elif x==5:
            return 8.29
    h3=0.5
    print("a) Diferença progressiva para vi=1:")
    print("h = 0.5 | f'(x)=", dp(f1, 1, h3))
    print("Diferença progressiva para vi=4.5:")
    print("h = 0.5 | f'(x)=", dp(f1,4.5, h3))

    print("b) Diferença regressiva para vi=1:")
    print("h = 0.5 | f'(x)=", dr(f1, 1, h3))
    print("Diferença regressiva para vi=4.5:")
    print("h = 0.5 | f'(x)=", dr(f1,4.5, h3))

    print("c) Diferença central para vi=1:")
    print("h = 0.5 | f'(x)=", dc(f1, 1, h3))
    print("Diferença central para vi= 4.5:")
    print("h = 0.5 | f'(x)=", dc(f1,  4.5, h3))
    
    #x = np.array([0.0,0.5, 1.0, 1.5, 2.0,2.5,3.0,3.5,4.0,4.5,5.0], dtype=float)
    #y = np.array([0.0, 1.05, 1.83, 2.69,3.83,4.56,5.49,6.56,6.11,7.06,8.29], dtype=float)
    #v = lambda x: np.column_stack((x,x**3))
    #A = regressao(x, y, v)
    #print(A)
    #resultado da regressão:[ 1.89398693 -0.01247779]
    print("d) derivação analitica:")
    print("f(x) =  1.894*x-0.0125*x^3")
    print("f'(x) =  1.894-0.0375*x^2")
    df2 = lambda x:1.894-3*0.0125*x**2
    print("Derivada analítica:")
    print("f'(1)=", df2(1))
    print("f'(4.5)=", df2(4.5))



    








if __name__ == "__main__":
    main()
