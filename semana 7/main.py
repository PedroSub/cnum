import numpy as np

from algoritmos import (
    G,
    GN,
    fixed_point,
)


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    def F(x):
        x1, x2, x3 = x
        return np.array(
            [
                2.0 * x1 - x2 - np.cos(x1),
                -x1 + 2.0 * x2 - x3 - np.cos(x2),
                -x2 + x3 - np.cos(x3),
            ],
            dtype=float,
        )

    def J(x):
        x1, x2, x3 = x
        return np.array(
            [
                [2.0 + np.sin(x1), -1.0, 0.0],
                [-1.0, 2.0 + np.sin(x2), -1.0],
                [0.0, -1.0, 1.0 + np.sin(x3)],
            ],
            dtype=float,
        )

    x = np.array([1.0, 1.0, 1.0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

    # Atividade 2
    print("-- Atividade 2 --")

    def F(x):
        x1, x2, x3 = x
        return np.array(
            [
                6.0 * x1 - 2.0 * x2 +np.exp(x3) - 2,
                np.sin(x1) - x2 + x3 ,
                np.sin(x1) + 2.0 * x2 + 3.0 * x3 - 1,
            ],
            dtype=float,
        )

    def J(x):
        x1, x2, x3 = x
        return np.array(
            [
                [6.0, -2.0, np.exp(x3)],
                [np.cos(x1), -1.0, 1.0],
                [np.cos(x1), 2.0, 3.0],
            ],
            dtype=float,
        )

    x = np.array([0, 0, 0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

    # Atividade 3
    print("-- Atividade 3.1 --")

    def F(x):
        x1, x2= x
        return np.array(
            [
                (x1**2)/8 + ((x2-1)**2)/5 - 1,
                np.arctan(x1) + x1 - x2 -x2**3 ,
            ],
            dtype=float,
        )

    def J(x):
        x1, x2 = x
        return np.array(
            [
                [2.0*x1/8.0, 2.0*(x2-1)/5.0],
                [1/(1+x1**2) + 1, -1.0-3*x2**2],
            ],
            dtype=float,
        )

    x = np.array([-1, -1], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)
    print("-- Atividade 3.2 --")

    def F(x):
        x1, x2= x
        return np.array(
            [
                (x1**2)/8 + ((x2-1)**2)/5 - 1,
                np.arctan(x1) + x1 - x2 -x2**3 ,
            ],
            dtype=float,
        )

    def J(x):
        x1, x2 = x
        return np.array(
            [
                [2.0*x1/8.0, 2.0*(x2-1)/5.0],
                [1/(1+x1**2) + 1, -1.0-3*x2**2],
            ],
            dtype=float,
        )

    x = np.array([2, 2], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

    # Atividade 4
    print("-- Atividade 4 --")

    def F(x):
        x1, x2,x3,k= x
        return np.array(
            [
                x1+x2+x3-1500,
                0.3 + (x1)*2e-4 +(x1**3)*4*3.4e-9-k,
                0.25+(x2)*4e-4+(x2**2)*3*4.3e-7-k,
                0.19+(x3)*10e-4+(x3**3)*4*1.1e-7-k,
            ],
            dtype=float,
        )

    def J(x):
        x1, x2,x3,k = x
        return np.array(
            [
                [1.0, 1.0, 1.0,0],
                [2e-4 +(x1**2)*12*3.4e-9, 0, 0,-1.0],
                [0, 4e-4+(x2)*6*4.3e-7, 0,-1.0],
                [0, 0, 10e-4+(x3**2)*12*1.1e-7,-1.0],
            ],
            dtype=float,
        )

    x = np.array([400, 400,400,0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

if __name__ == "__main__":
    main()
