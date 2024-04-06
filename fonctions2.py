import random
from re import A, T
from tkinter  import Button, Entry, Frame, Label, messagebox
import numpy as np
import tkinter as tk


def resolution_systeme_triangulaire_inferieur(matrice, vecteur):
    n = len(matrice)
    x = [0] * n  # Initialisation du vecteur solution

    for i in range(n):
        x[i] = vecteur[i]
        for j in range(i):
            x[i] -= matrice[i][j] * x[j]
        x[i] /= matrice[i][i]

    return x
def resolution_systeme_triangulaire_superieur(matrice, vecteur_b):
    n = len(matrice)
    x = [0] * n

    # Boucle à partir de la dernière ligne jusqu'à la première
    for i in range(n - 1, -1, -1):
        x[i]=vecteur_b[i]
        for j in range(i + 1, n):
            x[i]-= matrice[i][j] * x[j]
        x[i] /= matrice[i][i]
    np.round(x,2)
    return x

def is_symmetric(matrix):
    num_rows = len(matrix[0])
    num_columns = len(matrix[0]) 
    # Check for symmetry
    return all(matrix[i][j] == matrix[j][i] for i in range(num_rows) for j in range(num_columns))

def is_positive_definite(matrix):
    # Check if the matrix is symmetric
    if not is_symmetric(matrix):
        return False

    # Check if all leading principal minors have positive determinants
    for i in range(1, len(matrix) + 1):
        submatrix = [row[:i] for row in matrix[:i]]
        determinant = calculate_determinant(submatrix)
        if determinant <= 0:
            return False

    return True

def calculate_determinant(matrix):
    n = len(matrix[0])
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            sign = (-1) ** j
            determinant += sign * matrix[0][j] * calculate_determinant(submatrix)
        return determinant

def Resolution_systeme_triangulaire_sup(matrice, b):
     n=len(b)
     x=[0]*n
     for i in range(n-1,-1,-1):
        x[i]=b[i]
        for j in range(i+1,n):
            x[i]=x[i]-matrice[i][j]*x[j]
        x[i]=x[i]/matrice[i][i]
     return x  

def Resolution_triangulaire_inf(matrice,b):
    n=len(b)
    x=[0]*n
    for i in range(n):
        x[i]=b[i]
        for j in range(i):
            x[i]=x[i]-matrice[i][j]*x[j]
        x[i]=x[i]/matrice[i][i]
    return x 

def Resolution_systeme_triangulaire_inf_bande(L, b, m):
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i]
        for k in range(max(0, i-m), i):
            y[i] -= L[i, k] * y[k]

    return y
def Resolution_systeme_triangulaire_sup_bande(U, b, m):
    n = len(b)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for k in range(i+1, min(i+m+1, n)):
            x[i] -= U[i, k] * x[k]
        x[i] /= U[i, i]

    return x

def Gauss_partial_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
         # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=550, y=170) 

    vector_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=1150, y=170)

    result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1350, y=170)
    result_frame2 =Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=850, y=1050)
        #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []
        
        

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)

        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label =Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)
        

        button2 = Button(nouvelle_fenetre, text="Resoudre", command=partial_pivot_gauss_elimination_dense, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=40)

    def partial_pivot_gauss_elimination_dense():
         global matrix_values,matrix_entries,vector_entries
        # Initialiser la matrice résultante avec des zéros
         matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
         n = len(matrix_values)
         vector_values = []
         for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
    
         
         Atilde = np.column_stack((matrix_values, vector_values))

         for k in range(n - 1):
    
          pivot_row = k
          max_val = abs(Atilde[k, k])
          for i in range(k + 1, n):
            if abs(Atilde[i, k]) > max_val:
                max_val = abs(Atilde[i, k])
                pivot_row = i

            if pivot_row != k:
             for j in range(n + 1):
                
                Atilde[k, j], Atilde[pivot_row, j] = Atilde[pivot_row, j], Atilde[k, j]

     
            for i in range(k + 1, n):
             Atilde[i, k] = Atilde[i, k] / Atilde[k, k]
             for j in range(k + 1, n + 1):
                Atilde[i, j] -= Atilde[i, k] * Atilde[k, j]

           
         X = np.zeros(n)
         for i in range(n - 1, -1, -1):
          sum_term = 0
          for j in range(i + 1, n):
            sum_term += Atilde[i, j] * X[j]
          X[i] = (Atilde[i, -1] - sum_term) / Atilde[i, i]
          X[i] = np.round(X[i], 2)
         frame_VecteurR = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
         frame_VecteurR.pack()
         frame_VecteurR.place(x=850, y=400)
         for i in range(n):
            label_text = f"x{i+1} = {X[i]}"
            label_VecteurR = tk.Label(frame_VecteurR, text=label_text, relief="solid", borderwidth=1, width=8,
                                          height=2, bg='#eebfbc', font=("Arial", 10))
            label_VecteurR.grid(row=i)

def multiply_triangulaire_inferieure_Vecteur(nouvelle_fenetre):
    
 rows_var = tk.StringVar()

    # Créer un cadre pour les entrées utilisateur
 input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
 input_frame.pack()

    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
 label = tk.Label(nouvelle_fenetre, text="Choisir la taille nxn :", font=("Times New Roman", 15, "italic bold"),
                          background='#BCD2EE', foreground='#780000')
 label.pack()
 label.place(x=700, y=40)
 entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var, fg="#004E98", width=5, font=("Arial", 10),
                               highlightthickness=1, relief='raised', borderwidth=2)
 entry_rows.pack()
 entry_rows.place(x=890, y=40)
 band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
 band_frame.pack()
 band_frame.place(x=550, y=170) 

 

 result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
 result_frame.pack()
 result_frame.place(x=1300, y=170)
 result_frame2 =Frame(nouvelle_fenetre,padx=8,pady=8)
 result_frame2.pack()
 result_frame2.place(x=850, y=700)

 def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []
        
        

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                if j<=i:
                    
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        
        

        button2 = Button(nouvelle_fenetre, text="Multiplier", command=multiplication_triangulaire_inf, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
 button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
 button1.pack()
 button1.place(x=1300, y=40)

 def multiplication_triangulaire_inf():
         global matrix_values,matrix_entries,vector_entries
        # Initialiser la matrice résultante avec des zéros
         matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
         n = len(matrix_values)
         vector_values = []
         for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
         x = [0] * n

         for i in range(n):
          for j in range(i +1):
           x[i] = x[i] + matrix_values[i][j] * vector_values[j]



        
       
       # Affichage du vecteur
         frame_VecteurR = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
         frame_VecteurR.pack()
         frame_VecteurR.place(x=850, y=400)
         for i in range(n):
            label_VecteurR = tk.Label(frame_VecteurR, text=f"{x[i]}", relief="solid", borderwidth=1, width=5,
                                          height=2, bg='#eebfbc', font=("Arial", 10))
            label_VecteurR.grid(row=i)


    # Créer un bouton pour lancer la multiplication et afficher le résultat
   
def multiply_bande_demi_bande(nouvelle_fenetre):
    rows_var = tk.StringVar()
    band_size_r=tk.StringVar()
         # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
         
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
        #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande m :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_r,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
    band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=550, y=170) 
    demiband_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    demiband_frame.pack()
    demiband_frame.place(x=1000, y=170) 
    
    
        
    def create_matrix():
     global n,A,r,matrix_bande_entries,matrix_demi_entries
     try:
            rows = int(rows_var.get())
            r=int(band_size_r.get())
     except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
     if (r>rows):
            messagebox.showerror("Erreur", "la taille de la bande(2m+1) doit être inferieur à n ")
            return
     matrix_bande_entries = []
     matrix_demi_entries=[]
       

     for i in range(rows):
            matrix_bande_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if max(0, i - r) <= j <= min(rows - 1, i +r):
                    # Inside the band
                    matrix_bande_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_bande_entries[i].append(entry)
     
     for j in range(rows):
            matrix_demi_entries.append([])
            for i in range(rows):
                entry = Entry(demiband_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j <= i <= min(rows - 1, j +r):
                    # Inside the band
                    matrix_demi_entries[j].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_demi_entries[j].append(entry)
      
     button=Button(nouvelle_fenetre,text="multiplier",command=multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
     button.pack()
     button.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=40)
    def multiplication():
        global r,n,matrix_bande_entries,matrix_demi_entries,demi_matrix_values,matrix_values,demi_matrix_values
        # Initialiser la matrice résultante avec des zéro
        
        matrix_values = np.array([[float(entry.get()) for entry in row] for row in matrix_bande_entries])
        n = len(matrix_values)
        demi_matrix_values = np.array([[float(entry.get()) for entry in row] for row in matrix_demi_entries])
        
       
        m=len(matrix_demi_entries)
        c = np.zeros((n, n))

        for i in range(n):
         for j in range(n):
            if i >= j:
                for k in range(j, min(n, j + r)):
                    c[i][j] += matrix_values[i][k] * demi_matrix_values[k][j]
            else:
                for k in range(i, min(n, i + r)):
                    c[i][j] += matrix_values[i][k] * demi_matrix_values[k][j]
          
        
        #affichage de la matrice 2   
        Result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
        Result_frame.pack()
        Result_frame.place(x=800, y=500) 
        for i in range(n):
            for j in range(n):
                #print(f"i: {i}, j: {j}")
                label_matrice_R = Label(Result_frame, text=f"{c[i][j]}", relief="solid", borderwidth=1, width=5, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_matrice_R.grid(row=i , column=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
                 

def Resolution_systeme_triangulaire_inf(nouvelle_fenetre):
       # Créer des variables tk pour stocker les valeurs entrées par l'utilisateur
    
    
    rows_var = tk.StringVar()

    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()

    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label = tk.Label(nouvelle_fenetre, text="Choisir la taille nxn :", font=("Times New Roman", 15, "italic bold"),
                          background='#BCD2EE', foreground='#780000')
    label.pack()
    label.place(x=700, y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var, fg="#004E98", width=5, font=("Arial", 10),
                               highlightthickness=1, relief='raised', borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=890, y=40)
    band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=550, y=170) 

    vector_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=1150, y=170)

    result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1350, y=170)
    result_frame2 =Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=850, y=1050)

    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []
        
        

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                if j<=i:
                    
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label =Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)
        

        button2 = Button(nouvelle_fenetre, text="Resoudre", command=Resolution, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=40)

    def Resolution():
         global matrix_values,matrix_entries,vector_entries
        # Initialiser la matrice résultante avec des zéros
         matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
         n = len(matrix_values)
         L = np.zeros((n, n))
        
         
         vector_values = []
         for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
         n=len(vector_values)
         x=[0]*n
         for i in range(n):
          x[i]=vector_values[i]
          for j in range(i):
            x[i]=x[i]-matrix_values[i][j]*x[j]
          x[i]/=matrix_values[i][i] 
         x=np.round(x,2)
         result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
         result_frame2.pack()
         result_frame2.place(x=850, y=400)
         for i in range(n):
                #print(f"i: {i}, j: {j}")
                label_text = f"x{i+1} = {x[i]}"
                label_VecteurR = Label(result_frame2, text=label_text, relief="solid", borderwidth=1, width=13, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_VecteurR.grid(row=i )
    # Créer un bouton pour lancer la multiplication et afficher le résultat
  
def Resolution_cholesky_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
         # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=550, y=170) 

    vector_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=1150, y=170)

    result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1350, y=170)
    result_frame2 =Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=1360, y=1390)
        #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []
        
        

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)

        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label =Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)
        

        button2 = Button(nouvelle_fenetre, text="Resoudre", command=Resolution, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=40)

    

    def Resolution():
        global matrix_values,matrix_entries,vector_entries
        # Initialiser la matrice résultante avec des zéros
        matrix_values = np.array([[int(entry.get()) for entry in row] for row in matrix_entries])
        n = len(matrix_values)
        L = np.zeros((n, n))
        
        if not np.allclose(matrix_values, matrix_values.T) or not np.all(np.linalg.eigvals(matrix_values) > 0):
         raise messagebox.showerror("Erreur", "la matrice doit etre sysmetrique definie positive.")
        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        for j in range(n):
         L[j, j] = matrix_values[j, j]
         for k in range(j):
            L[j, j] -= L[j, k]**2
         L[j, j] = np.sqrt(L[j, j])
         L[j, j] = np.round(L[j, j], 2)

         for i in range(j + 1, n):
            L[i, j] = matrix_values[i, j]
            for k in range(j):
                L[i, j] -= L[i, k] * L[j, k]
            L[i, j] = L[i, j] / L[j, j]
            L[i, j] = np.round(L[i, j], 2)
        #affichage de la matrice 2 
        y = Resolution_triangulaire_inf(L, vector_values)
        x=Resolution_systeme_triangulaire_sup(L.T,y)
        x=np.round(x,2)
        frame_matrice_R = tk.Frame(nouvelle_fenetre)
        frame_matrice_R.pack()
        frame_matrice_R.place(x=1240, y=640) 
        label1=Label (nouvelle_fenetre,text="La matrice L de décomposition de Cholesky :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
        label1.pack()
        label1.place(x=1050,y=560)
        for i in range(n):
            for j in range(n):
                #print(f"i: {i}, j: {j}")
                label_matrice_R = Label(frame_matrice_R, text=f"{L[i][j]}", relief="solid", borderwidth=1, width=5, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_matrice_R.grid(row=i , column=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
        result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
        result_frame2.pack()
        result_frame2.place(x=850, y=400)
        for i in range(n):
                #print(f"i: {i}, j: {j}")
                label_text = f"x{i+1} = {x[i]}"
                label_VecteurR = Label(result_frame2, text=label_text, relief="solid", borderwidth=1, width=13, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_VecteurR.grid(row=i )

def Resolution_cholesky_Bande(nouvelle_fenetre):
   rows_var = tk.StringVar()
   band_size_r=tk.StringVar()
         # Créer un cadre pour les entrées utilisateur
   input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
   input_frame.pack()
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
   label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
   label.pack()
   label.place(x=800,y=40)
   entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
   entry_rows.pack()
   entry_rows.place(x=1000,y=40)
        #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
   label=Label (nouvelle_fenetre,text="Taille de la bande m :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
   label.pack()
   label.place(x=800,y=70)
   entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_r,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
   entry_band1.pack()
   entry_band1.place(x=1000,y=70)
   band_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
   band_frame.pack()
   band_frame.place(x=550, y=170) 

   vector_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
   vector_frame.pack()
   vector_frame.place(x=1150, y=170)

   result_frame = Frame(nouvelle_fenetre,padx=8,pady=8)
   result_frame.pack()
   result_frame.place(x=1350, y=170)
   result_frame2 =Frame(nouvelle_fenetre,padx=8,pady=8)
   result_frame2.pack()
   result_frame2.place(x=850, y=1050)
   def create_matrix_and_vector():
        global n,A,r,matrix_entries,vector_entries
        try:
            rows = int(rows_var.get())
            r=int(band_size_r.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        if (r>rows):
            messagebox.showerror("Erreur", "la taille de la bande(2m+1) doit être inferieur à n ")
            return
        matrix_entries = []

       

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if max(0, i - r) <= j <= min(rows - 1, i +r):
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label =Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)
        

        button2 = Button(nouvelle_fenetre, text="Resoudre", command=Resolution, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
   button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
   button1.pack()
   button1.place(x=1300, y=40)
   def Resolution():
        global r,n,matrix_entries,vector_entries,matrix_values,vector_values
        # Initialiser la matrice résultante avec des zéro
        
        matrix_values = np.array([[float(entry.get()) for entry in row] for row in matrix_entries])
        n = len(matrix_values)
        L = np.zeros((n, n))
        
        if not np.allclose(matrix_values, matrix_values.T) or not np.all(np.linalg.eigvals(matrix_values) > 0):
         raise messagebox.showerror("Erreur", "la matrice doit etre sysmetrique definie positive.")
        vector_values = []
        for i in range(n):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        print(matrix_values)
        for j in range(n):
          L[j,j] = matrix_values[j, j]
          for k in range(j):
            L[j, j] -= L[j, k] ** 2
          L[j, j] = np.sqrt(L[j, j])
          L[j, j] = np.round(L[j, j], 2)

          for i in range(j + 1, min(n, j + r + 1)):
           L[i, j] = matrix_values[i, j]
           for k in range(max(0, j - r), j):
             L[i, j] -= L[i, k] * L[j, k]
           L[i, j] /= L[j, j]
           L[i, j] = np.round(L[i, j], 2)

        
        y = Resolution_systeme_triangulaire_inf_bande(L, vector_values, r)
        x = Resolution_systeme_triangulaire_sup_bande(L.T, y, r) 
        x=np.round(x,2)
        frame_matrice_R = tk.Frame(nouvelle_fenetre)
        frame_matrice_R = tk.Frame(nouvelle_fenetre)
        frame_matrice_R.pack()
        frame_matrice_R.place(x=1240, y=640) 
        label1=Label (nouvelle_fenetre,text="La matrice L de décomposition de Cholesky :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
        label1.pack()
        label1.place(x=1050,y=560)
        for i in range(n):
            for j in range(n):
                #print(f"i: {i}, j: {j}")
                label_matrice_R = Label(frame_matrice_R, text=f"{L[i][j]}", relief="solid", borderwidth=1, width=6, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_matrice_R.grid(row=i , column=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
        result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
        result_frame2.pack()
        result_frame2.place(x=850, y=400)
        for i in range(n):
                #print(f"i: {i}, j: {j}")
                label_text = f"x{i+1} = {x[i]}"
                label_VecteurR = Label(result_frame2, text=label_text, relief="solid", borderwidth=1, width=15, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_VecteurR.grid(row=i )

def Gauss_matrice_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
    
    bold_font = ("Arial", 12, "bold")     
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows =tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    
    
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
    result_frame2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)

        vector_entries = []
        

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label =tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)
    def resolve_system():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        if not is_symmetric(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return
        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        gaussian_result = gaussian_elimination(matrix_values, vector_values)

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {gaussian_result[i]}"
            label =tk.Label(result_frame2, text=label_text, width=10, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def gaussian_elimination(matrix, vector):
        n = len(matrix)

        for k in range(n - 1):
            for i in range(k + 1, n):
                matrix[i][k] /= matrix[k][k]

                for j in range(k + 1, n):
                    matrix[i][j] -= matrix[i][k] * matrix[k][j] 

                vector[i] -= matrix[i][k] * vector[k]

        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = vector[i]
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j]
            x[i] /= matrix[i][i]
            x=[round(element, 2) for element in x]
        return x
    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=70)


def triangulaire_superieure_x_vecteur(nouvelle_fenetre):
    rows_var = tk.StringVar()
   
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    frame_matrice = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150) 
    frame_matrice.place() 
    frame_vecteur = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_vecteur.pack()
    frame_vecteur.place(x=1050, y=150) 


    def create_matrix():
        global rows,matrix_entries, vector_entries
        rows = int(rows_var.get())
        
 
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                if i <= j <= rows:
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
           
        
                    
        
        vector_entries = []

     
        for i in range(rows):
            entry = Entry(frame_vecteur, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)    
        
       
        
        button2=Button(nouvelle_fenetre, text="Multiplier",command=resole_system,width=10,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

    def resole_system():
        
        matrix = [[float(entry.get()) for entry in row] for row in matrix_entries]
        vector=[]
        for i in range(rows):
            vector.append(float(vector_entries[i].get()))

        multiplication_result=multiplication_vecteur(matrix,vector)
        frame_resultat = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
        frame_resultat.pack()
        frame_resultat.place(x=900, y=480) 
        for j in range(len(multiplication_result)):
            label_resultat= Label(frame_resultat, text=f"{multiplication_result[j]}", relief="solid", borderwidth=1, width=8, height=2,bg='#eebfbc',font=("Arial",10)) 
            label_resultat.grid(row=j, column=0)
    def multiplication_vecteur(matrice,vecteur):
        
         # Initialiser un tableau Yi rempli de zéros
        Y = [0] * rows
        # Implémenter l'algorithme
        for i in range(rows):
            for j in range(i, rows):
                Y[i] += matrice[i][j] * vecteur[j]
               
        return Y

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix,width=10,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)
     
 
def triangulaire_inferieure_demi_bande_x_triangulaire_superieure_demi_bande(nouvelle_fenetre):
     # Créer des variables tk pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    band_size_s=tk.StringVar()
    band_size_r=tk.StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande s :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_s,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
    label=Label (nouvelle_fenetre,text="Taille de la bande r :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=100)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_r,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=100)
    frame_matrice1 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice1.pack()
    frame_matrice1.place(x=600, y=150) 
   
    frame_matrice2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice2.pack()
    frame_matrice2.place(x=1050, y=150)
        
    
    def create_matrix_bande():
        global n,r,s,matrix1_entries,matrix2_entries
        #les exceptions sur les valeurs de la bande s et r
        try:
            n = int(rows_var.get())
            s=int(band_size_s.get())
            r=int(band_size_r.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        if s==r:
            messagebox.showerror("Erreur", "r doit être différente de s")
            return
        if (s>=n or r>=n):
            messagebox.showerror("Erreur", "la taille de la bande doit être inferieur de n ")
            return
        #remplissage des matrices

        matrix1_entries = []

        for i in range(n):
            matrix1_entries.append([])
            for j in range(n):
                entry = Entry(frame_matrice1, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                if max(0, i-s)<= j <=i:
                    # Inside the band
                    matrix1_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix1_entries[i].append(entry)
        

        matrix2_entries = []

        for i in range(n):
            matrix2_entries.append([])
            for j in range(n):
                entry = Entry(frame_matrice2, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                if i<= j <= min(i+r, n):
                    # Inside the band
                    matrix2_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix2_entries[i].append(entry)


         

         
        
           #Créer un bouton pour lancer la multiplication et afficher le résultat
        button2=Button(nouvelle_fenetre, text="Multiplier",command=resole_system,width=10,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1400, y=500)
    def resole_system():
        
        matrix1 = [[float(entry.get()) for entry in row] for row in matrix1_entries]
        matrix2 = [[float(entry.get()) for entry in row] for row in matrix2_entries]

        
        multiplication_result=multiplication(matrix1,matrix2)
        frame_resultat = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
        frame_resultat.pack()
        frame_resultat.place(x=900, y=480) 
        for i in range(len(multiplication_result)):
            for j in range(len(multiplication_result)):
                label_resultat= Label(frame_resultat, text=f"{multiplication_result[i][j]}", relief="solid", borderwidth=1, width=5, height=2,bg='#eebfbc',font=("Arial",10)) 
                label_resultat.grid(row=i, column=j)
    def multiplication(A,B):
        
        # Initialiser la matrice résultante avec des zéros
        C = [[0] * n for _ in range(n)]

        # Effectuer la multiplication matricielle
         # Parcourez les éléments de la matrice résultante
        for i in range(n):
        # Parcourez les éléments de la bande inférieure de la matrice inférieure
            for j in range(max(0, i-s), min(r+i+1,n)):
                C[i][j] = 0
                # Parcourez les éléments de la bande supérieure de la matrice supérieure
                for k in range(max(0, i-s), min(i, j)+1):
                    print(f"i: {i}, j: {j},k{k}")
                    C[i][j] += A[i][k] * B[k][j]
        
        return C
        
        
    #Créer un bouton pour lancer la multiplication et afficher le résultat
                 

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_bande,width=30,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)
 
def resolution_triangulaire_inf_demi_bande(nouvelle_fenetre):

    bold_font = ("Arial", 12, "bold") 
    rows_var = tk.StringVar()
    band_size_s=tk.StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande s :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_s,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)

    
    frame_matrice = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=170) 
    frame_matrice.place() 
   # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)
    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
   

    def create_matrix():
        global rows,s,matrix_entries, vector_entries
        rows = int(rows_var.get())
        s=int(band_size_s.get())
 
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                if max(0, i-s)<= j <= i:
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
           
        
                    
        
        vector_entries = []
        

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)

    def resolve_system():
        
        matrix = [[float(entry.get()) for entry in row] for row in matrix_entries]
        vector=[]
        for i in range(rows):
            vector.append(float(vector_entries[i].get()))

        resolution_result=resolution(matrix,vector,s)
        frame_resultat = tk.Frame(nouvelle_fenetre)
        frame_resultat.pack()
        frame_resultat.place(x=900, y=480) 
     # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {resolution_result[i]}"
            label = tk.Label(frame_resultat, text=label_text, width=15, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)
    def resolution(matrice,b,s):
        x = [0] * rows
        for i in range(rows):
            x[i]=b[i]
            for j in range(max(0, i-s), i):
                x[i] -= matrice[i][j] * x[j]
            x[i]=x[i]/matrice[i][i]
        return x    

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix,width=30,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)


def Gauss_jordon_matrice_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
    
    bold_font = ("Arial", 12, "bold")     
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    
    
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
    result_frame2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)

        vector_entries = []
        

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)
    def resolve_system():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        if not is_symmetric(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return
        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        gaussian_result = gauss_jordan_elimination(matrix_values, vector_values)

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {gaussian_result[i]}"
            label = tk.Label(result_frame2, text=label_text, width=15, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def gauss_jordan_elimination(matrix, vector):
        n = len(matrix)

        # Étape de l'élimination directe
        for k in range(n - 1):
            for i in range(k + 1, n):
                # Normalisation
                factor = matrix[i][k] / matrix[k][k]
            for i in range(n):
                if(i!=k):
                    for j in range(k+1, n):
                        matrix[i][j] -= factor * matrix[k][j]
                    vector[i] -= factor * vector[k]

        # Étape de la substitution arrière
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = vector[i]
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j]
            x[i] /= matrix[i][i]
            x=[round(element,3)for element in x]
        return x
        
        

    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=70)
 

def Gauss_jordon_matrice_bande(nouvelle_fenetre):
    rows_var = tk.StringVar()
    bande_var = tk.StringVar()

    bold_font = ("Arial", 12, "bold")     

    # Choisir la taille de la matrice
    label_taille = Label(nouvelle_fenetre, text="Choisir la taille nxn :", font=("Times New Roman", 15, "italic bold"), background='#BCD2EE', foreground='#780000')
    label_taille.pack()
    label_taille.place(x=800, y=40)

    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var, fg="#004E98", width=5, font=("Arial", 12), highlightthickness=1, relief='raised', borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000, y=40)

    # Choisir la taille de la bande
    label_bande = Label(nouvelle_fenetre, text="Choisir la taille de m: :", font=("Times New Roman", 15, "italic bold"), background='#BCD2EE', foreground='#780000')
    label_bande.pack()
    label_bande.place(x=800, y=70)

    entry_bande = tk.Entry(nouvelle_fenetre, textvariable=bande_var, fg="#004E98", width=5, font=("Arial", 12), highlightthickness=1, relief='raised', borderwidth=2)
    entry_bande.pack()
    entry_bande.place(x=1000, y=70)

    # Créer une Frame pour afficher la matrice bande
    band_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)

    result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_band_matrix_and_vector():
        global vector, rows, bande, resultat_vector, matrix_entries, vector_entries

        try:
            rows = int(rows_var.get())
            bande = int(bande_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        if (bande>rows):
            messagebox.showerror("Erreur", "la taille de la bande(2m+1) doit être inferieur à n ")
            return
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)
                if max(0, i - bande) <= j <= min(rows - 1, i + bande):
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

                

        vector_entries = []

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                              relief="solid",borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()

        button1.place(x=1300, y=500)

    def resolve_system():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        if not is_symmetric(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return

        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        gaussian_result = gauss_jordan_elimination_banded(matrix_values, vector_values,bande)

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {gaussian_result[i]}"
            label = tk.Label(result_frame2, text=label_text, width=15, height=2,
                             relief="solid", font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def gauss_jordan_elimination_banded(matrix, vector, bande):
        n = len(matrix)

        for k in range(n - 1):
            # Partie supérieure de la bande
            for i in range( k + 1,min(k+1+bande,n)):
                matrix[i][k] /= matrix[k][k]

            for i in range(k+1,n):
                for j in range(k + 1,min(k+1+bande, n)):
                    matrix[i][j] -= matrix[i][k] * matrix[k][j]

                vector[i] -= matrix[i][k] * vector[k]

        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = vector[i]
            # Partie inférieure de la bande
            for j in range(i + 1, min(n, i + bande + 1)):
                x[i] -= matrix[i][j] * x[j]   
            x[i] /= matrix[i][i]
            x=[round(element,3)for element in x]

        return x


    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_band_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=70)


def resolution_demi_band_sup(nouvelle_fenetre):
     # Créer des variables tk  pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    band_size_var=tk.StringVar()
    bold_font = ("Arial", 12, "bold")     
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    label=Label (nouvelle_fenetre,text="Taille de la bande m:",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
    result_frame2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)
    def create_matrix_and_vector():
        global matrix_entries, vector_entries,x,bande,rows,resultat_vector
        
        try:
            rows = int(rows_var.get())
            bande= int(band_size_var.get())
        except ValueError:
              messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
              return
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if bande > rows:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier inferieur à n.")
            return 
        matrix_entries = []
        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j < i or j > min(rows - 1, i + bande):
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)


        vector_entries = []

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        resultat_vector = [f"x{i+1}" for i in range(rows)]

        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5, height=2,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)# Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1=Button(nouvelle_fenetre,text="resoudre",command=resolution_systeme_lineaire_bande,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button1.pack()
        button1.place(x=1300,y=500)
    def resolution_systeme_lineaire_bande():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]

        try:
            vector_values = [float(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
       
        x = [0] * rows
        for i in range(rows-1, -1, -1):
            x[i] = vector_values[i]
            for j in range(i+1, min(i+1+bande, rows)):
                x[i] -=matrix_values[i][j] * x[j]
            x[i] /= matrix_values[i][i]
            x=[round(element, 2) for element in x]
        

        
        for i in range(rows):
                label_text = f"{resultat_vector[i]} = {x[i]}"
                label = tk.Label(result_frame2, text=label_text, width=10, height=2,
                             relief="solid", borderwidth=2, font=bold_font,bg='#eebfbc')
                label.grid(row=i, column=j)
                
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def Gauss_matrice_bande(nouvelle_fenetre):
    rows_var = tk.StringVar()
    bande_var = tk.StringVar()

    bold_font = ("Arial", 12, "bold")     

    # Choisir la taille de la matrice
    label_taille = Label(nouvelle_fenetre, text="Choisir la taille nxn :", font=("Times New Roman", 15, "italic bold"), background='#BCD2EE', foreground='#780000')
    label_taille.pack()
    label_taille.place(x=800, y=40)

    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var, fg="#004E98", width=5, font=("Arial", 12), highlightthickness=1, relief='raised', borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000, y=40)

    # Choisir la taille de la bande
    label_bande = Label(nouvelle_fenetre, text="Choisir la taille de m:", font=("Times New Roman", 15, "italic bold"), background='#BCD2EE', foreground='#780000')
    label_bande.pack()
    label_bande.place(x=800, y=70)

    entry_bande = tk.Entry(nouvelle_fenetre, textvariable=bande_var, fg="#004E98", width=5, font=("Arial", 12), highlightthickness=1, relief='raised', borderwidth=2)
    entry_bande.pack()
    entry_bande.place(x=1000, y=70)

    # Créer une Frame pour afficher la matrice bande
    band_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)

    result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_band_matrix_and_vector():
        global vector, rows, bande, resultat_vector, matrix_entries, vector_entries

        try:
            rows = int(rows_var.get())
            bande = int(bande_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if bande > rows:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier inferieur à n.")
            return
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if max(0, i - bande) <= j <= min(rows - 1, i + bande):
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

        vector_entries = []

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)

    def resolve_system():
    
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]

        try:
            vector_values = [float(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        

        if not is_symmetric(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(matrix_values):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return

        

        gaussian_result = gaussian_elimination_banded(matrix_values,vector_values)
        
        

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {gaussian_result[i]}"
            label = tk.Label(result_frame2, text=label_text, width=15, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def gaussian_elimination_banded(matrix,vector):
        for k in range(rows - 1):
            for i in range(k + 1,min(k+1+bande, rows)):
                matrix[i][k] /= matrix[k][k]
                for j in range(k + 1,min(k+1+bande, rows)):
                        matrix[i][j] -= matrix[i][k] * matrix[k][j]
                    

                vector[i] -= matrix[i][k] * vector[k]

    
       
        x = [0] * rows
        for i in range(rows-1, -1, -1):
            x[i] = vector[i]
            for j in range(i+1, min(i+1+bande, rows)):
                x[i] -= matrix[i][j] * x[j]
            x[i] /= matrix[i][i]
            x=[round(element, 2) for element in x]
        return x    
    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_band_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=300, y=70)
 

def Jaccobi_matrice_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
    
    bold_font = ("Arial", 12, "bold")     
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    
    
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
    result_frame2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries= []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)
     
        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)
    def resolve_system():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        jaccobi_result = jaccobi_method(matrix_values, vector_values)
        

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {jaccobi_result[i]}"
            label = tk.Label(result_frame2, text=label_text, width=10, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def jaccobi_method(A, b, epsilon=1e-6, max_iterations=1000):
        n = len(b)
        x = [0] * n
        iteration = 0

        while iteration < max_iterations:
            x_old = x.copy()

            for i in range(n):
                s = b[i]
                for j in range(n):
                    if i != j:
                        s -= A[i][j] * x_old[j]
                x[i] = s / A[i][i]
                
            max_difference = max(abs(xi - x_old[i]) for i, xi in enumerate(x))

            if max_difference < epsilon:
                x=[round(element, 2) for element in x]
                return x

            iteration += 1
        return x
    
        

    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=70)


def matrice_vector(nouvelle_fenetre):
     # Créer des variables tk pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    # Créer une Frame pour afficher la matrice
    matrix_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    matrix_frame.pack()
    matrix_frame.place(x=600, y=170)

    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=1050, y=170) 
    # Créer une Frame pour afficher le résultat de la multiplication
    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=800, y=500)
    def create_matrix_and_vector():
        global matrix_values,vector_values,rows,matrix_entries,vector_entries
        
        try:
            rows = int(rows_var.get())
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour la taille.")
                return
        matrix_entries= []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(matrix_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)
     
        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(vector_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
                
   
        button1=Button(nouvelle_fenetre,text="multiplier",command=perform_multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button1.pack()
        button1.place(x=1300,y=500)
    def perform_multiplication():

        try:
            rows = len(matrix_entries)
        except NameError:
            messagebox.showerror("Erreur", "Veuillez d'abord créer une matrice et un vecteur.")
            return
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]

        try:
            vector_values = [float(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        result = [0] * len(matrix_values)

        for i in range(len(matrix_values)):
            for j in range(len(matrix_values[0])):
                result[i] += matrix_values[i][j] * vector_values[j]
    # Afficher le résultat dans l'interface
        for i in range(len(result)):
            label = tk.Label(result_frame, text=result[i], relief="solid", borderwidth=1, width=5,bg='#eebfbc', height=2,font=("Arial",12))
            label.grid(row=i, column=0)
            
    # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)
def matrice_demi_band_sup_vector(nouvelle_fenetre):
    
    
     # Créer des variables tk pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    band_size_var=tk.StringVar()
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    label=Label (nouvelle_fenetre,text="Taille de la bande m:",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170)
    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=1050, y=170) 

    

    # Créer une Frame pour afficher le résultat de la multiplication
    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=800, y=500)
    def create_matrix_and_vector():
        global matrix_values,vector_values,rows,matrix_entries,vector_entries
        try:
            rows = int(rows_var.get())
            bande= int(band_size_var.get())
        except ValueError:
              messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
              return
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if bande > rows:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier inferieur à n.")
            return 
        matrix_entries = []
        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j < i or j > min(rows - 1, i + bande):
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)


        vector_entries = []

        
        for i in range(rows):
            entry = Entry(vector_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
    
      
        button1=Button(nouvelle_fenetre,text="multiplier",command=perform_multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button1.pack()
        button1.place(x=1300,y=500)
    
    def perform_multiplication():

        try:
            rows = len(matrix_entries)
        except NameError:
            messagebox.showerror("Erreur", "Veuillez d'abord créer une matrice et un vecteur.")
            return
        matrix_values = [[int(entry.get()) for entry in row] for row in matrix_entries]

        try:
            vector_values = [int(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        result_matrix = [0] * rows
        for i in range(rows):
            for j in range(i, min(i + len(matrix_values[0]), len(matrix_values))):
                result_matrix[i] += matrix_values[i][j] * vector_values[j]
        
    # Afficher le résultat dans l'interface
        for i in range(rows):
            label = tk.Label(result_frame, text=result_matrix[i], relief="solid", borderwidth=1, width=5,bg='#eebfbc', height=2,font=("Arial",12))
            label.grid(row=i, column=0)

   
        
        
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)


def matrice_demi_band_sup_transposé(nouvelle_fenetre):
    
    
     # Créer des variables tk pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    band_size_var=tk.StringVar()
        
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    label=Label (nouvelle_fenetre,text="Taille de la bande m:",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    transposé_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    transposé_frame.pack()
    transposé_frame.place(x=1050, y=170) 

    # Créer une Frame pour afficher le résultat de la multiplication
    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=800, y=500)
    def create_matrix_bande():
        global vector, rows, bande, resultat_vector, matrix_entries, vector_entries

        try:
            rows = int(rows_var.get())
            bande = int(band_size_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if bande > rows:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier inferieur à n.")
            return
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if max(0, i - bande) <= j <= min(rows - 1, i + bande):
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
        

    # Calculate the transpose if the matrix is full
        

        button1=Button(nouvelle_fenetre,text="multiplier",command=multiply_band_matrix_by_transpose,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button1.pack()
        button1.place(x=1300,y=500) 
    
    def multiply_band_matrix_by_transpose():
        matrix_values=[]
        matrix_values = [[int(entry.get()) for entry in row] for row in matrix_entries]
        is_matrix_full = all(all(entry.get() for entry in row) for row in matrix_entries)
        if is_matrix_full:
    # Calculate the transpose
            transpose_matrix = [[matrix_values[j][i] for j in range(len(matrix_entries))] for i in range(len(matrix_values[0]))]
            
            for i in range(len(transpose_matrix)):
                for j in range(len(transpose_matrix[0])):
                    label_matrice = Label(transposé_frame, text=transpose_matrix[i][j], relief="solid", borderwidth=1, width=5, height=1,bg='#eebfbc',font=("Arial",12)) 
                    label_matrice.grid(row=i,column=j)
        # Initialiser la matrice résultante avec des zéros
        result_matrix = [[0] * len(transpose_matrix[0]) for _ in range(len(matrix_values))]

        # Effectuer la multiplication matricielle
        for i in range(rows):
            for j in range(rows):
                for k in range(max(0, i - bande), min(rows, i + bande+ 1)):
                    result_matrix[i][j] +=matrix_values[i][k] * transpose_matrix[k][j]

        # Afficher la matrice résultante dans l'interface
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                label_matrice1 = Label(result_frame, text=result_matrix[i][j], relief="solid", borderwidth=1, width=5, height=1,bg='#eebfbc',font=("Arial",12)) 
                label_matrice1.grid(row=i , column=j )
    

    # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_bande,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def solve_banded_matrix_pivot_partial_gauss(nouvelle_fenetre):
    rows_var = tk.StringVar()
    band_size_r = tk.StringVar()

    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()

    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label = Label(nouvelle_fenetre, text="Choisir la taille nxn :", font=("Times New Roman", 15, "italic bold"),
                  background='#BCD2EE', foreground='#780000')
    label.pack()
    label.place(x=800, y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var, fg="#004E98", width=5, font=("Arial", 12),
                         highlightthickness=1, relief='raised', borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000, y=40)

    # creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label = Label(nouvelle_fenetre, text="Taille de la bande m :", font=("Times New Roman", 15, "italic bold"),
                  background='#BCD2EE', foreground='#780000')
    label.pack()
    label.place(x=800, y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=band_size_r, fg="#004E98", width=5, font=("Arial", 12),
                           highlightthickness=1, relief='raised', borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000, y=70)
    band_frame = Frame(nouvelle_fenetre, padx=8, pady=8)
    band_frame.pack()
    band_frame.place(x=550, y=170)
    vector_frame = Frame(nouvelle_fenetre, padx=8, pady=8)
    vector_frame.pack()
    vector_frame.place(x=1150, y=170)

    result_frame = Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame.pack()
    result_frame.place(x=1350, y=170)

    def create_matrix_and_vector():
        global n, A, r, matrix_entries, vector_entries
        try:
            rows = int(rows_var.get())
            r = int(band_size_r.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        if r > rows:
            messagebox.showerror("Erreur", "la taille de la bande(2m+1) doit être inferieur à n ")
            return
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if max(0, i - r) <= j <= min(rows - 1, i + r):
                    # Inside the band
                    matrix_entries[i].append(entry)
                else:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)

        vector_entries = []

        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label = Label(vector_frame, text=resultat_vector[i], width=5,
                          relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        button2 = Button(nouvelle_fenetre, text="Resoudre", command=Resolution, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)

    def Resolution():
        global matrix_values, matrix_entries, vector_entries, r, n
        # Initialiser la matrice résultante avec des zéros
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        n = len(matrix_values)
        vector_values = []
        for i in range(n):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        rows_matrix = len(matrix_values)
        vector_result = np.zeros(rows_matrix)
        bandwidth = 2 * r + 1

        # Concatenate the banded matrix with the vector
        used_matrix = [row + [vector_row] for row, vector_row in zip(matrix_values, vector_values)]

        # Changing the rows
        for i in range(rows_matrix):
            pivot_index = max(range(i, min(i + 1 + bandwidth, rows_matrix)),
                              key=lambda k: abs(used_matrix[k][i]))
            used_matrix[i], used_matrix[pivot_index] = used_matrix[pivot_index], used_matrix[i]

            # Application of the Gauss algorithm
            pivot_value = used_matrix[i][i]
            for j in range(i + 1, min(i + 1 + bandwidth, rows_matrix)):
                factor = used_matrix[j][i] / pivot_value
                used_matrix[j][i] = 0
                used_matrix[j][-1] -= factor * used_matrix[i][-1]

        # Solving the lower matrix
        for i in range(rows_matrix - 1, -1, -1):
            pivot_value = used_matrix[i][i]
            vector_result[i] = used_matrix[i][-1] / pivot_value
            for j in range(i - 1, max(-1, i - 1 - bandwidth), -1):
                used_matrix[j][-1] -= used_matrix[j][i] * vector_result[i]
            vector_result[i] = np.round(vector_result[i], 2)
        
        frame_VecteurR = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
        frame_VecteurR.pack()
        frame_VecteurR.place(x=850, y=400)
        for i in range(n):
            label_text = f"x{i+1} = {vector_result[i]}"
            label_VecteurR = tk.Label(frame_VecteurR, text=label_text, relief="solid", borderwidth=1, width=13,
                                      height=2, bg='#eebfbc', font=("Arial", 10))
            label_VecteurR.grid(row=i, column=0)

    # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
    button1 = Button(nouvelle_fenetre, text="afficher", command=create_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=40)

def matrice_bande_fois_matrice_inverse(nouvelle_fenetre):
    # Créer des variables tk  pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk .StringVar()
    band_size=tk .StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk .Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk .Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande m :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk .Entry(nouvelle_fenetre, textvariable=band_size,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
    frame_matrice = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150) 
    frame_matrice_inverse = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice_inverse.pack()
    frame_matrice_inverse.place(x=1050, y=150)
    frame_matrice_res = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice_res.pack()
    frame_matrice_res.place(x=800, y=480)
    def create_matrix_and_vector():
        global rows,bande,matrix_entries,bande
        try:
            rows= int(rows_var.get())
            bande=int(band_size.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if (bande>(rows+1)/2):
            messagebox.showerror("Erreur", "la taille de la bande(2m+1) doit être inferieur à n ")
            return
        #remplissage de matrice
        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice,borderwidth=0.5,  width=5, font=("Arial", 12), bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j> i+bande or j< i-bande:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)
        #creer un boutton pour calculer l'inverse        
        button3=Button(nouvelle_fenetre,text="inverser",command=calcul_mat_inverse,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button3.pack()
        button3.place(x=1300, y=110)
        
        
    def calcul_mat_inverse():
        global A_inverse,matrix_values
        #calcul de la mat inverse
        matrix_values = [[int(entry.get()) for entry in row] for row in matrix_entries]
        identite = np.identity(rows)  # Crée une matrice identité de taille nxn
        augmente = np.concatenate((matrix_values, identite), axis=1)  # Matrice augmentée [matrice | identité]

        for i in range(rows):
            pivot = augmente[i][i]
            augmente[i] = augmente[i] / pivot  

            for j in range(rows):
                if i != j:
                    coef = augmente[j][i]
                    augmente[j] = augmente[j] - coef * augmente[i]  
        inverse = augmente[:, rows:]
        A_inverse=np.round(inverse,2)
        
        #affichage de la matrice inverse 
         
        for i in range(rows):
            for j in range(rows):
                label_matrice = Label(frame_matrice_inverse, text=f"{A_inverse[i][j]}", relief="solid", borderwidth=0.5, width=5, font=("Arial", 12), bg='#eebfbc') 
                label_matrice.grid(row=i , column=j ) 

        #Créer un bouton pour lancer la multiplication et afficher le résultat
        button2=Button(nouvelle_fenetre, text="Multiplier",command=multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)
    def multiplication():
        
        # Initialiser la matrice résultante avec des zéros
        C = [[0] * rows for _ in range(rows)]
        # Effectuer la multiplication matricielle
        # Parcourez les éléments de la matrice résultante
        for i in range(rows):
            for j in range(rows):
                for k in range(max(0, i - bande), min(rows, i + bande + 1)):
                    C[i][j] += matrix_values[i][k] * A_inverse[k][j]  
        C_arr=np.round(C)   
        
        #affichage de la matrice res   
         
        for i in range(rows):
            for j in range(rows):
                label_matrice = Label(frame_matrice_res, text=f"{C_arr[i][j]}", relief="solid",borderwidth=0.5, width=5, font=("Arial", 12), bg='#eebfbc') 
                label_matrice.grid(row=i , column=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def matrice_demi_bande_inf_fois_vect(nouvelle_fenetre):
    # Créer des variables tk  pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk .StringVar()
    band_size=tk .StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk .Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk .Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande m :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk .Entry(nouvelle_fenetre, textvariable=band_size,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
    frame_matrice = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150)
    frame_Vecteur = tk .Frame(nouvelle_fenetre, padx=8, pady=8)
    frame_Vecteur.pack()
    frame_Vecteur.place(x=1050, y=150)
    
    def create_matrix_and_vector():
        global rows,bande,matrix_entries,vector_entries
        try:
            rows = int(rows_var.get())
            bande= int(band_size.get())
        except ValueError:
              messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
              return
        if bande <= 0:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier positif non nul.")
            return
        if bande > rows:
            messagebox.showerror("Erreur", "La valeur de m doit être un entier inferieur à n.")
            return 
        matrix_entries = []
        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j > i or j < i - bande:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)


        vector_entries = []
        
        for i in range(rows):
            entry = Entry(frame_Vecteur, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        #affichage de la matrice    
         
        #Créer un bouton pour lancer la multiplication et afficher le résultat
        button2=Button(nouvelle_fenetre, text="Multiplier",command=multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1300, y=500)
        
    def multiplication():
        
        try:
            rows = len(matrix_entries)
        except NameError:
            messagebox.showerror("Erreur", "Veuillez d'abord créer une matrice et un vecteur.")
            return
        A = [[int(entry.get()) for entry in row] for row in matrix_entries]

        try:
            V = [int(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        C = [0] * rows
        for i in range(rows):
            for j in range(max(0, i - bande), i + 1):
                C[i] += A[i][j] * V[j]

        #affichage de la vecteur resultat  
        frame_vecteur = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
        frame_vecteur.pack()
        frame_vecteur.place(x=800, y=480) 
        for j in range(rows):
            label_vecteur = Label(frame_vecteur, text=f"{C[j]}", relief="solid", borderwidth=1, width=5, height=2,bg='#eebfbc',font=("Arial",10)) 
            label_vecteur.grid(row=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
                 

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def resolution_lin_mat_sup_dense(nouvelle_fenetre):
    # Créer des variables tk  pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk .StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk .Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk .Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)   
    frame_matrice = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150)    
    frame_Vecteur = tk .Frame(nouvelle_fenetre, padx=8, pady=8)
    frame_Vecteur.pack()
    frame_Vecteur.place(x=1050, y=150) 
    vector_frame = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=150)
    def create_matrix_and_vector():
        global rows,matrix_entries,vector_entries,resultat_vector
        #les exceptions sur les valeurs de la bande s et r
        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes.")
            return
        
        #remplissage de matrice
        matrix_entries = []
        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)

                if j <i:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)
        #remplissage vecteur
        vector_entries = []

        
        for i in range(rows):
            entry = Entry(frame_Vecteur, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label = tk .Label(vector_frame, text=resultat_vector[i], width=5, height=2,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)# Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        #Créer un bouton pour lancer la multiplication et afficher le résultat
        button2=Button(nouvelle_fenetre, text="Résoudre",command=multiplication,width=10,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1400, y=500)
        
    def multiplication():
        A = [[float(entry.get()) for entry in row] for row in matrix_entries]

        try:
            V = [float(vector_entries[i].get()) for i in range(rows)]    
        except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        C = [0] * rows

        for i in range(rows - 1, -1, -1):
            C[i]=V[i]
            for j in range(i + 1, rows):
                C[i]-= A[i][j] * C[j]
            C[i] /= A[i][i]
        C=np.round(C,2)
        #affichage de la vecteur resultat  
        frame_vecteur = tk .Frame(nouvelle_fenetre)
        frame_vecteur.pack()
        frame_vecteur.place(x=800, y=480) 
        for j in range(rows):
            label_text = f"{resultat_vector[j]} = {C[j]}"
            label_vecteur = Label(frame_vecteur, text=label_text, relief="solid", borderwidth=1, width=10, height=2,bg='#eebfbc',font=("Arial",10)) 
            label_vecteur.grid(row=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
                 

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def decomposition_LU(nouvelle_fenetre):
    # Créer des variables tk  pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk .StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk .Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk .Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40) 
    frame_matrice = tk .Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150)      
    frame_Vecteur = tk .Frame(nouvelle_fenetre, padx=8, pady=8)
    frame_Vecteur.pack()
    frame_Vecteur.place(x=1050, y=150)
    frame_Vecteur1= tk .Frame(nouvelle_fenetre,padx=8,pady=8) 
    frame_Vecteur1.pack()
    frame_Vecteur1.place(x=900,y=150)
    frame_vecteur_2 = tk .Frame(nouvelle_fenetre)
    frame_vecteur_2.pack()
    frame_vecteur_2.place(x=800, y=480) 
    def create_matrix_and_vector():
        global rows,matrix_entries,vector_entries,resultat_vector
        #les exceptions sur les valeurs de la bande s et r
        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes.")
            return
        

        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)

        vector_entries = []
        

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(frame_Vecteur, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label = tk .Label(frame_Vecteur1, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        #Créer un bouton pour lancer la multiplication et afficher le résultat
        button2=Button(nouvelle_fenetre, text="Résoudre",command=multiplication,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
        button2.pack()
        button2.place(x=1400, y=500)
       
    def multiplication():
        A = [[float(entry.get()) for entry in n] for n in matrix_entries]        
        n = len(A)
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        V = []

        for i in range(n): 
            try:
                V.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return
        if not is_symmetric(A):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(A):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return         
        for i in range(n):
            for k in range(i, n):
                somme = sum(L[i][j] * U[j][k] for j in range(i))
                U[i][k] = A[i][k] - somme

            for k in range(i, n):
                if i == k:
                    L[i][i] = 1
                else:
                    somme = sum(L[k][j] * U[j][i] for j in range(i))
                    L[k][i] = (A[k][i] - somme) / U[i][i]
        y =resolution_systeme_triangulaire_inferieur(L, V)
        C =resolution_systeme_triangulaire_superieur(U,y)
        C=np.round(C,2)

        #affichage de la vecteur resultat  
        for j in range(n):
            label_text = f"x{j+1} = {C[j]}"
            label_vecteur = Label(frame_vecteur_2, text=label_text, relief="solid", borderwidth=1, width=8, height=2,bg='#eebfbc',font=("Arial",10)) 
            label_vecteur.grid(row=j )
    #Créer un bouton pour lancer la multiplication et afficher le résultat
                 

    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)

def decomposition_LU_bande(nouvelle_fenetre):
     # Créer des variables Tkinter pour stocker les valeurs entrées par l'utilisateur
    rows_var = tk.StringVar()
    bande_var=tk.StringVar()
    # Créer un cadre pour les entrées utilisateur
    input_frame = tk.Frame(nouvelle_fenetre, bg="#BCD2EE")
    input_frame.pack()
        
    # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    #creer des Entry widgets pour que l 'utilisateur puisse saisir la taille de la bande de la matrice demi_bande
    label=Label (nouvelle_fenetre,text="Taille de la bande m :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=70)
    entry_band1 = tk.Entry(nouvelle_fenetre, textvariable=bande_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_band1.pack()
    entry_band1.place(x=1000,y=70)
    frame_matrice = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    frame_matrice.pack()
    frame_matrice.place(x=600, y=150)      
    frame_Vecteur = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    frame_Vecteur.pack()
    frame_Vecteur.place(x=900, y=150)
    result_frame = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=150)   
    result_frame2 = tk.Frame(nouvelle_fenetre, padx=8, pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500) 
    
    def create_matrix_and_vector():
        global  rows, bande, resultat_vector, matrix_entries, vector_entries

        try:
            rows = int(rows_var.get())
            bande = int(bande_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        matrix_entries = []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(frame_matrice, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                if j> i+bande or j< i-bande:
                    # Outside the band, set the entry to zero
                    entry.insert(0, "0")
                    matrix_entries[i].append(entry)
                else:
                    # Inside the band
                    matrix_entries[i].append(entry)

        vector_entries = []

        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)

        for i in range(rows):
            label = tk.Label(frame_Vecteur, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=multiplication, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 12, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)

    def multiplication():
        A=[[float(entry.get()) for entry in row] for row in matrix_entries]
        V=[] 
        L = np.zeros((rows, rows))  
        U = np.zeros((rows, rows)) 
        
        if not is_symmetric(A):
            messagebox.showerror("Erreur", "La matrice n'est pas symétrique.")
            return

        if not is_positive_definite(A):
            messagebox.showerror("Erreur", "La matrice n'est pas définie positive.")
            return
        for i in range(rows):
            try:
                V.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return 
        #ce code ne fonctionne pas ilya un erreur de type: "IndexError: list index out of range"
        for i in range(rows):
            L[i][i] = 1 
            for j in range(i, min(i + bande+1 , rows)):
                U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(max(0, i - bande), i))
            
            for j in range(i +1, min(i + bande+1 , rows)):
                L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(max(0, j - bande), j))) / U[i][i]
        y = resolution_systeme_triangulaire_inferieur(L, V)
        C = resolution_systeme_triangulaire_superieur(U, y) 
        C=np.round(C,2)
        
        #affichage de la vecteur resultat  
        frame_vecteur = tk.Frame(nouvelle_fenetre)
        frame_vecteur.pack()
        frame_vecteur.place(x=800, y=480) 
        for i in range(rows):
            label_text = f"x{i+1} = {C[i]}"
            label = tk.Label(result_frame2, text=label_text, width=15, height=2,
                             relief="solid", borderwidth=2, font=("Arial",10), bg='#eebfbc')
            label.grid(row=i)
    #Créer un bouton pour lancer la multiplication et afficher le résultat
    button=Button(nouvelle_fenetre,text="afficher",command=create_matrix_and_vector,width=15,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=1300, y=70)


def gauss_seidel_matrice_dense(nouvelle_fenetre):
    rows_var = tk.StringVar()
    
    bold_font = ("Arial", 12, "bold")     
    
        
        # Créer des Entry widgets pour que l'utilisateur puisse saisir la taille de la matrice
    label=Label (nouvelle_fenetre,text="Choisir la taille nxn :",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#780000')
    label.pack()
    label.place(x=800,y=40)
    entry_rows = tk.Entry(nouvelle_fenetre, textvariable=rows_var,fg="#004E98",width=5, font=("Arial", 12),highlightthickness=1, relief='raised' , borderwidth=2)
    entry_rows.pack()
    entry_rows.place(x=1000,y=40)
    
    
        
    # Créer une Frame pour afficher la matrice
    band_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    band_frame.pack()
    band_frame.place(x=600, y=170) 

    # Créer une Frame pour afficher le vecteur
    vector_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    vector_frame.pack()
    vector_frame.place(x=900, y=170)

    result_frame = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame.pack()
    result_frame.place(x=1050, y=170)
    result_frame2 = tk.Frame(nouvelle_fenetre,padx=8,pady=8)
    result_frame2.pack()
    result_frame2.place(x=800, y=500)

    def create_matrix_and_vector():
        global  vector, rows, resultat_vector,matrix_entries,vector_entries

        try:
            rows = int(rows_var.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers pour les lignes et la taille de la bande.")
            return

        

        matrix_entries= []

        for i in range(rows):
            matrix_entries.append([])
            for j in range(rows):
                entry = Entry(band_frame, width=5, font=("Arial", 12), relief="solid", bg='#eebfbc')
                entry.grid(row=i, column=j)
                matrix_entries[i].append(entry)
     
        vector_entries = []
        

        
        for i in range(rows):
            entry = Entry(result_frame, width=5, font=("Arial", 12), bg='#eebfbc')
            entry.grid(row=i, column=0)
            vector_entries.append(entry)
        resultat_vector = [f"x{i+1}" for i in range(rows)]
        for i in range(rows):
            label = tk.Label(vector_frame, text=resultat_vector[i], width=5,
                             relief="solid", borderwidth=2, font=("Arial", 12))
            label.grid(row=i, column=0)

        # Créer un bouton pour l'utilisateur pour valider les dimensions de la matrice
        button1 = Button(nouvelle_fenetre, text="Resoudre", command=resolve_system, width=15, height=1,
                         relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
        button1.pack()
        button1.place(x=1300, y=500)
    def resolve_system():
        matrix_values = [[float(entry.get()) for entry in row] for row in matrix_entries]
        vector_values = []
        for i in range(rows):
            try:
                vector_values.append(float(vector_entries[i].get()))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir des nombres valides pour les éléments du vecteur.")
                return

        gauss_seidel_result = gauss_seidel_method(matrix_values, vector_values)
        

        # Affichage du résultat dans l'interface
        for i in range(rows):
            label_text = f"x{i+1} = {gauss_seidel_result[i]}"
            label = tk.Label(result_frame2, text=label_text, width=10, height=2,
                             relief="solid", borderwidth=2, font=bold_font, bg='#eebfbc')
            label.grid(row=i, column=0)

    def gauss_seidel_method(A, B,  tol=1e-6, max_iter=100):
        n=rows
        X = np.zeros(n)
        max_diff = float('inf')
        iter_count = 0
        
        while max_diff > tol and iter_count < max_iter:
            max_diff = 0
            for i in range(n):
                old_Xi = X[i]
                sigma = 0
                for j in range(n):
                    if j != i:
                        sigma += A[i][j] * X[j]
                X[i] = (B[i] - sigma) / A[i][i]
                max_diff = max(max_diff, abs(old_Xi - X[i]))
            
            iter_count += 1
        X=[round(element,3)for element in X]
        return X


    
        

    # Ajouter un bouton pour l'utilisateur pour commencer le processus
    button1 = Button(nouvelle_fenetre, text="Afficher", command=create_matrix_and_vector, width=15, height=1,
                     relief='raised', borderwidth=5, font=("Times New Roman", 10, "italic bold"), foreground='#004E98')
    button1.pack()
    button1.place(x=1300, y=70)