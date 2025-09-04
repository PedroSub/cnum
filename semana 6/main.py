import numpy as np

from algoritmos import (
    lu,
    jacobi,
    seidel,
)


def main():
    # Atividade 1
    print("-- Atividade 1 --")
    A = np.array([[1, 1, 1], [4, 4, 2], [2, 1, -1]], dtype=float)
    B = np.array([1, 2, 0], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    A = np.array([[2, 1, -1], [4, 4, 2], [1, 1, 1]], dtype=float)
    B = np.array([0, 2, 1], dtype=float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-8)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)

    # Atividade 2
    print("-- Atividade 2 --")
    A = np.array([[5, 1, 1], [-1, 3, -1], [1, 2, 10]], dtype=float)
    B = np.array([50, 10, -30], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-3)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-3)
    print(X)

    # Atividade 3
    print("-- Atividade 3 --")
    A = np.array([[1, 10, 3], [4, 0, 1], [2, 1, 4]], dtype=float)
    B = np.array([27, 6, 12], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    A = np.array([[4, 0, 1],[1, 10, 3], [2, 1, 4]], dtype=float)
    B = np.array([6,27,12], dtype=float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-8)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)

    # Atividade 4
    print("-- Atividade 4 --")
    r1=2 
    r2=2
    r3=2
    r4=2
    r5= 100  
    r6= 100   
    r7= 100  
    r8= 50  
    A = np.array([[1, 0, 0, 0, 0], [1/r1, -(r2*r5+r1*r5+r1*r2)/(r1*r2*r5), 0, 0, 1/r2], [0, 1/r2, -(r3*r6+r2*r6+r2*r3)/(r2*r3*r6), 0, 1/r3],[0, 0, 1/r3, -(r4*r7+r3*r7+r3*r4)/(r3*r4*r7), 1/r4],[0, 0, 0, 1/r4, -(r8+r4)/(r8*r4)]], dtype=float)
    B = np.array([127, 0, 0, 0, 0], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    A = np.array([[1, 0, 0, 0, 0],[0, 1/r2, -(r3*r6+r2*r6+r2*r3)/(r2*r3*r6), 0, 1/r3],[0, 0, 1/r3, -(r4*r7+r3*r7+r3*r4)/(r3*r4*r7), 1/r4],[0, 0, 0, 1/r4, -(r8+r4)/(r8*r4)], [1/r1, -(r2*r5+r1*r5+r1*r2)/(r1*r2*r5), 0, 0, 1/r2]], dtype=float)
    B = np.array([127, 0, 0, 0, 0], dtype=float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-8)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)


if __name__ == "__main__":
    main()
