from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk
import fonctions2

fenetre = Tk()

fenetre.title('Gestion des matrices')
fenetre['bg']='#F0EAD2'
#fenetre.iconbitmap('M.ico')
chemin=r"C:\Users\LENOVO\Gestion-des-matrices\cube.ico"
fenetre.iconbitmap(chemin)
image_path = r"C:\Users\LENOVO\Gestion-des-matrices\istockphoto-1457115338-612x612 (5) (1).jpg"  # Use a raw string
original_image = Image.open(image_path)
converted_image = ImageTk.PhotoImage(original_image)
# Get the width and height of the image
image_width = converted_image.width()
image_height = converted_image.height()

# Set the window size to match the image size
fenetre.geometry(f"{image_width}x{image_height}+0+0")
fenetre.resizable(False,False)
# Create a label to hold the image
background_label = Label(fenetre, image=converted_image)
background_label.place(relwidth=1, relheight=1)
label=Label (fenetre,text="Gestion des matrices \n  Bienvenue!On est ici pour t'aider à faire des divers  opérations sur les matrices \n  n'hésitez pas de choisir l'opréation que vous voulez faire",font=("Times New Roman",15,"italic bold"),relief="raised",highlightthickness=6 , borderwidth=5)
label.pack()
label.place(x=340,y=35)


def retour_a_menu_principal():
    
    # Fermer la fenêtre actuelle
    nouvelle_fenetre.destroy()
    # Réouvrir la fenêtre principale
    fenetre.deiconify()  # Affiche à nouveau la fenêtre principale

def destroy_and_reopen_res():
   
    # Destroy the current window
    nouvelle_fenetre.destroy()
    # Open the same window again
    passer_a_resolution()

def destroy_and_reopen_vect():
    
    # Destroy the current window
    nouvelle_fenetre.destroy()
    # Open the same window again
    passer_a_matrice_x_vecteur()

def destroy_and_reopen_mat():
    
    # Destroy the current window
    nouvelle_fenetre.destroy()
    # Open the same window again
    passer_a_matrice_x_matrice()
    

def passer_a_resolution():
    # Fermer la fenêtre actuelle
    fenetre.withdraw()
    global nouvelle_fenetre
   
    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = tk.Toplevel(fenetre)
    largeur_ecran = nouvelle_fenetre.winfo_screenwidth()
    hauteur_ecran = nouvelle_fenetre.winfo_screenheight()
    nouvelle_fenetre.attributes('-fullscreen', True)
    nouvelle_fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}+0+0")

    nouvelle_fenetre.geometry('1530x780')
    nouvelle_fenetre.title('Résolution')
    nouvelle_fenetre.resizable(False,False)
    nouvelle_fenetre['bg'] = '#BCD2EE'
    label=Label (nouvelle_fenetre,text="Menu",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#004E98')
    label.pack()
    label.place(x=150,y=80)
    button=Button(nouvelle_fenetre,text="Systéme triangulaire inféreieur dense ",command=lambda:fonctions2.Resolution_systeme_triangulaire_inf(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=40, y=120)
    button_demi=Button(nouvelle_fenetre,text=" Systéme triangulaire inféreieur demi bande ",command=lambda:fonctions2.Resolution_systeme_triangulaire_inf(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_demi.pack()
    button_demi.place(x=40, y=160)
    button_demi_sup=Button(nouvelle_fenetre,text=" Matrice supérieure demi-bande ",command=lambda:fonctions2.resolution_demi_band_sup(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_demi_sup.pack()
    button_demi_sup.place(x=40, y=200)
    button_sup=Button(nouvelle_fenetre,text=" Matrice supérieure dense ",command=lambda:fonctions2.resolution_lin_mat_sup_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_sup.pack()
    button_sup.place(x=40, y=240)
     #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    button_Gauss=Button(nouvelle_fenetre,text="Elimination de Gauss matrice Dense",command=lambda:fonctions2.Gauss_matrice_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Gauss.pack()
    button_Gauss.place(x=40, y=280)
    button_Gauss_Bande=Button(nouvelle_fenetre,text="Elimination de Gauss matrice Bande",command=lambda:fonctions2.Gauss_matrice_bande(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Gauss_Bande.pack()
    button_Gauss_Bande.place(x=40, y=320)
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    button_Gauss_partial=Button(nouvelle_fenetre,text="Elimination de Gauss partial matrice Dense",command=lambda:fonctions2.Gauss_partial_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Gauss_partial.pack()
    button_Gauss_partial.place(x=40, y=360)
    button_Gauss_partial_bande=Button(nouvelle_fenetre,text="Elimination de Gauss partial matrice Bande",command=lambda:fonctions2.solve_banded_matrix_pivot_partial_gauss(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Gauss_partial_bande.pack()
    button_Gauss_partial_bande.place(x=40, y=400)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    button_cholesky=Button(nouvelle_fenetre,text="Resolution Cholesky Matrice Dense",command=lambda:fonctions2.Resolution_cholesky_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_cholesky.pack()
    button_cholesky.place(x=40, y=440)
    button_cholesky_Bande=Button(nouvelle_fenetre,text="Resolution Cholesky Matrice Bande",command=lambda:fonctions2.Resolution_cholesky_Bande(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_cholesky_Bande.pack()
    button_cholesky_Bande.place(x=40, y=480)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Ajoutez les éléments de la nouvelle fenêtre ici
    button_Jordan=Button(nouvelle_fenetre,text="Resolution Jordan Matrice Dense",command=lambda:fonctions2.Gauss_jordon_matrice_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Jordan.pack()
    button_Jordan.place(x=40, y=520)
    button_Jordan_Bande=Button(nouvelle_fenetre,text="Resolution Jordan Matrice Bande",command=lambda:fonctions2.Gauss_jordon_matrice_bande(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Jordan_Bande.pack()
    button_Jordan_Bande.place(x=40, y=560)
   #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    button_LU=Button(nouvelle_fenetre,text="Resolution avec décomposition LU Matrice Dense",command=lambda:fonctions2.decomposition_LU(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_LU.pack()
    button_LU.place(x=40, y=600)
    button_LU=Button(nouvelle_fenetre,text="Resolution avec décomposition LU Matrice Bande",command=lambda:fonctions2.decomposition_LU_bande(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_LU.pack()
    button_LU.place(x=40, y=640)
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------
    button_Jacobi=Button(nouvelle_fenetre,text="Resolution Jaccobi Matrice dense",command=lambda:fonctions2.Jaccobi_matrice_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_Jacobi.pack()
    button_Jacobi.place(x=40, y=680)
    button_seidel=Button(nouvelle_fenetre,text="Resolution Gauss Seidel  Matrice dense",command=lambda:fonctions2.gauss_seidel_matrice_dense(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_seidel.pack()
    button_seidel.place(x=40, y=720)
    return_button = tk.Button(nouvelle_fenetre, text="Retour", command=retour_a_menu_principal,width=20,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    return_button.pack(side=BOTTOM)
    # Create a button to destroy and reopen the same window
    reopen_button = tk.Button(nouvelle_fenetre, text="Rafraichir", command=destroy_and_reopen_res, width=20, height=2, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    reopen_button.pack(side=BOTTOM)
    nouvelle_fenetre.mainloop()

def passer_a_matrice_x_vecteur():
    # Fermer la fenêtre actuelle
    fenetre.withdraw()
    global nouvelle_fenetre
    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = tk.Toplevel(fenetre)
    largeur_ecran = nouvelle_fenetre.winfo_screenwidth()
    hauteur_ecran = nouvelle_fenetre.winfo_screenheight()
    nouvelle_fenetre.attributes('-fullscreen', True)
    nouvelle_fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}+0+0")

    nouvelle_fenetre.geometry('1530x780')
    nouvelle_fenetre.resizable(False,False)
    nouvelle_fenetre.title('matrice x vecteur')
    nouvelle_fenetre['bg'] = '#BCD2EE'
    label=Label (nouvelle_fenetre,text="Menu",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#004E98')
    label.pack()
    label.place(x=150,y=80)
    button_dense=Button(nouvelle_fenetre,text="Matrice dense x Vecteur",command=lambda:fonctions2.matrice_vector(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_dense.pack()
    button_dense.place(x=40, y=120)
    button=Button(nouvelle_fenetre,text="Matrice triangulaire inférieur x Vecteur",command=lambda:fonctions2.multiply_triangulaire_inferieure_Vecteur(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button.pack()
    button.place(x=40, y=160)
    button2=Button(nouvelle_fenetre,text="Matrice triangulaire supérieur x Vecteur",command=lambda:fonctions2.triangulaire_superieure_x_vecteur(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button2.pack()
    button2.place(x=40, y=200)
    button3=Button(nouvelle_fenetre,text="Matrice demi bande supérieur x Vecteur",command=lambda:fonctions2.matrice_demi_band_sup_vector(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button3.pack()
    button3.place(x=40, y=240)
    button4=Button(nouvelle_fenetre,text="Matrice demi bande inféreiur x Vecteur",command=lambda:fonctions2.matrice_demi_bande_inf_fois_vect(nouvelle_fenetre),width=40,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button4.pack()
    button4.place(x=40, y=280)

    return_button = tk.Button(nouvelle_fenetre, text="Retour", command=retour_a_menu_principal,width=20,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    return_button.pack(side=BOTTOM)
    reopen_button = tk.Button(nouvelle_fenetre, text="Rafraichir", command=destroy_and_reopen_vect, width=20, height=1, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    reopen_button.pack(side=BOTTOM)
    
    nouvelle_fenetre.mainloop()
   

def passer_a_matrice_x_matrice():
    # Fermer la fenêtre actuelle
    fenetre.withdraw()
    global nouvelle_fenetre
    # Créer et afficher une nouvelle fenêtre de résolution
    nouvelle_fenetre = tk.Toplevel(fenetre)
    largeur_ecran = nouvelle_fenetre.winfo_screenwidth()
    hauteur_ecran = nouvelle_fenetre.winfo_screenheight()
    nouvelle_fenetre.attributes('-fullscreen', True)
    nouvelle_fenetre.geometry(f"{largeur_ecran}x{hauteur_ecran}+0+0")

    nouvelle_fenetre.geometry('1530x780')
    nouvelle_fenetre.resizable(False,False)
    nouvelle_fenetre.title('matrice x matrice')
    nouvelle_fenetre['bg'] = '#BCD2EE'
    label=Label (nouvelle_fenetre,text="Menu",font=("Times New Roman",15,"italic bold"),background='#BCD2EE',foreground='#004E98')
    label.pack()
    label.place(x=200,y=80)
    
    
    button_bande_demi_bande=Button(nouvelle_fenetre,text="Matrice bande x demi bande inférieur",command=lambda:fonctions2.multiply_bande_demi_bande(nouvelle_fenetre),width=55,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_bande_demi_bande.pack()
    button_bande_demi_bande.place(x=40, y=160)
    button_demi_demi_bande=Button(nouvelle_fenetre,text="Matrice demi bande inférieur x demi bande supérieure",command=lambda:fonctions2.triangulaire_inferieure_demi_bande_x_triangulaire_superieure_demi_bande(nouvelle_fenetre),width=55,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_demi_demi_bande.pack()
    button_demi_demi_bande.place(x=40, y=200)
    button_transposé=Button(nouvelle_fenetre,text="Matrice bande x matrice transposé",command=lambda:fonctions2.matrice_demi_band_sup_transposé(nouvelle_fenetre),width=55,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_transposé.pack()
    button_transposé.place(x=40, y=240)
    button_inverse=Button(nouvelle_fenetre,text="Matrice bande x matrice inverse",command=lambda:fonctions2.matrice_bande_fois_matrice_inverse(nouvelle_fenetre),width=55,height= 1, relief='raised' , borderwidth=5,font=("Times New Roman",10,"italic bold"),foreground='#004E98')
    button_inverse.pack()
    button_inverse.place(x=40, y=280)
    
    return_button = tk.Button(nouvelle_fenetre, text="Retour", command=retour_a_menu_principal,width=20,height= 2, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    return_button.pack(side=BOTTOM)
    reopen_button = tk.Button(nouvelle_fenetre, text="Rafraichir", command=destroy_and_reopen_mat, width=20, height=2, relief='raised' , borderwidth=5,font=("Times New Roman",12,"italic bold"),foreground='#004E98')
    reopen_button.pack(side=BOTTOM)

    nouvelle_fenetre.mainloop()


button=Button(text="Multiplication matrice × vecteur",command=passer_a_matrice_x_vecteur,width=35,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=1000, y=250)
button=Button(text="Multiplication matrice × matrice",command=passer_a_matrice_x_matrice,width=35,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=1000, y=350) 
button=Button(text="Résolution",command=passer_a_resolution,width=35,height= 2, relief='raised', highlightthickness=6 , borderwidth=5,font=("Times New Roman",15,"italic bold"))
button.pack()
button.place(x=1000, y=450)  

fenetre.mainloop()