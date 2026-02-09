import numpy as np
import scipy as sp

def pseudo_inv(A):
    U, S, VT = np.linalg.svd(A, full_matrices=True)
    Sigma = np.zeros_like(A, dtype=float)  
    for i in range(len(S)):
        if S[i] > 1e-10:  
            Sigma[i, i] = 1 / S[i]
    pseudo_inv_A = VT.T @ Sigma.T @ U.T
    return pseudo_inv_A
def Q16():
    A = np.array([[1,3],
                 [2,2],
                 [3,1]])
    U, S, VT = np.linalg.svd(A, full_matrices=True)
    print(f"Singular values of A = {S}\n")
    print(f"U matrix of A = {U}\n")
    print(f"V^T matrix of A = {VT}\n")

    pseudo_inv_A = pseudo_inv(A)
    print(f'pseudoinverse of A = {pseudo_inv_A}\n')

    print(f'A^+A = {pseudo_inv_A@A}\n')

    print(f'AA^+ = {A@pseudo_inv_A}\n')

    M = A@pseudo_inv_A - np.identity(3)
    U, S, VT = np.linalg.svd(M, full_matrices=True)

    null_space = VT[1:,:].T
    print(f'Null(M) = {null_space}\n')
    print(f'b = c_1{null_space[:,0]} + c_2{null_space[:,1]} for any real c_1 and c_2')

def Q17():
    A = np.array([[0,3,0],
                  [2,0,0]])
    U, S, VT = np.linalg.svd(A, full_matrices=True)
    print(f"Singular values of A = {S}\n")
    print(f"U matrix of A = {U}\n")
    print(f"V^T matrix of A = {VT}\n")

    pseudo_inv_A = pseudo_inv(A)
    print(f'pseudoinverse of A = {pseudo_inv_A}\n')

    M = pseudo_inv_A @ A - np.identity(3)
    print(f'A^+A-I = {M}')

def Q18():
    A = np.array([[1,0,0],
                 [1,0,0],
                 [1,1,1]])
    b = np.array([[0],[2],[2]])
    
    x = pseudo_inv(A) @ b
    print(f'least-square solution = {x}')


if __name__ == "__main__":
    #Q16()
    #Q17()
    Q18()