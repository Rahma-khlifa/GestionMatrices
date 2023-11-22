import numpy as np

def multiplication_matrice_vecteur(matrice, vecteur):
    if len(matrice) != len(matrice[0]) or len(matrice) != len(vecteur):
        raise ValueError("Les dimensions de la matrice et du vecteur ne sont pas compatibles.")

    resultat = np.zeros(len(vecteur))

    for i in range(len(matrice)):
        for j in range(i + 1):
            resultat[i] += matrice[i][j] * vecteur[j]

    return resultat

def Resolution_systeme_triangulaire_inf(matrice,b):
    n=len(b)
    x=[0]*n
    for i in range(n):
        x[i]=b[i]
        for j in range(i):
            x[i]=x[i]-matrice[i][j]*x[j]
        x[i]=x[i]/matrice[i][i]
    return x 

matrice = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]
b = [1, 8, 21]

solution = Resolution_systeme_triangulaire_inf(matrice, b)
print("Solution:", solution)




def multiply_banded_lower_semi_banded(A, B, m):
    n = A.shape[0]

    C = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            sum_val = 0
            for k in range(max(0, i - m), min(n, i + 1)):
                sum_val += A[i, k] * B[k, j]
            C[i, j] = sum_val

    return C


# Example usage with user-provided values
m = 1  # Example value for m
n = 4  # Example size for the matrices
A = np.array([[1, 2, 0, 0],
              [3, 4, 5, 0],
              [0, 6, 7, 8],
              [0, 0, 9, 10]])

B = np.array([[1, 0, 0, 0],
              [2, 3, 0, 0],
              [0, 5, 6, 0],
              [0, 0, 9, 10]])

result = multiply_banded_lower_semi_banded(A, B, m)

print("Result:")
print(result)
