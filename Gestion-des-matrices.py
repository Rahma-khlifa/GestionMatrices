from tkinter import *
from PIL import Image, ImageTk
import imageio
import colorthief
import fonctions as f
 
def get_dominant_color(image_path):
    # Open the image
    image = Image.open(image_path)

    # Use colorthief to get the dominant color
    
    dominant_color = image.getpixel((0,0))

    # Convert RGB to hexadecimal color code
    hex_color = "#{:02x}{:02x}{:02x}".format(*dominant_color)

    return hex_color

def perform_matrix_multiplication_interface():
    # Create a new window for matrix multiplication
    multiplication_window = Toplevel(fenetre)
    multiplication_window.title("Matrice Multiplication")

    # Add buttons or other elements for matrix multiplication
    button_multiply_dense = Button(multiplication_window, text="Matrice Dense", command=f.multiplication_matrice_vecteur(f.matrice,f.b))
    button_multiply_dense.pack(pady=10)

    button_multiply_triangular = Button(multiplication_window, text="Matrice Triangulaire", command=perform_matrix_multiplication_triangular)
    button_multiply_triangular.pack(pady=10)

def perform_matrix_multiplication_dense():
    print("Performing Matrix Multiplication - Dense")

def perform_matrix_multiplication_triangular():
    print("Performing Matrix Multiplication - Triangular")

def perform_linear_system_resolution():
    print("Performing Linear System Resolution")


  


fenetre = Tk()

fenetre.title('Gestion des Matrices')
fenetre['bg'] = 'white'
fenetre.resizable(height=False, width=False)
  
image_path = r"C:\Users\LENOVO\Downloads\istockphoto-1457115338-612x612.jpg"  # Use a raw string
original_image = Image.open(image_path)
converted_image = ImageTk.PhotoImage(original_image)

# Get the width and height of the image
image_width = converted_image.width()
image_height = converted_image.height()

# Set the window size to match the image size
fenetre.geometry(f"{image_width}x{image_height}")

# Create a label to hold the image
background_label = Label(fenetre, image=converted_image)
background_label.place(relwidth=1, relheight=1)  # Expand the label to fill the entire window

font_color = get_dominant_color(image_path)







mon_Menu = Menu(fenetre)






Multiplication_matrice_vecteur = Menu(mon_Menu, tearoff=0)
Multiplication_matrice_vecteur.add_command(label="Matrice dense ")
matrice_triangulaire=Menu(Multiplication_matrice_vecteur,tearoff=0)
matrice_triangulaire.add_command(label="inférieur ")
matrice_triangulaire.add_command(label="supérieur ")
matrice_inf =Menu(matrice_triangulaire,tearoff=0)
matrice_inf.add_command(label="dense")
matrice_inf.add_command(label="demi-bande")
matrice_triangulaire.add_cascade(label="Matrice inférieure",menu=matrice_inf)
matrice_sup =Menu(matrice_triangulaire,tearoff=0)
matrice_sup.add_command(label="dense")
matrice_sup.add_command(label="demi-bande")
matrice_triangulaire.add_cascade(label="Matrice supéreiure",menu=matrice_sup)
Multiplication_matrice_vecteur.add_cascade(label="Matrice triangulaire",menu=matrice_triangulaire)
mon_Menu.add_cascade(label="Multiplication Matrice-Vecteur", menu=Multiplication_matrice_vecteur)



Multiplication_matrice_matrice = Menu(mon_Menu, tearoff=0)
matrice_bande=Menu(Multiplication_matrice_matrice,tearoff=0)
matrice_bande.add_command(label="Matrice demi-bande inférieur ")
matrice_bande.add_command(label="Matrice inverse ")
matrice_bande.add_command(label="Matrice transposée")
Multiplication_matrice_matrice.add_cascade(label="Matrice Bande",menu=matrice_bande)

matric_demi_bande=Menu(Multiplication_matrice_matrice,tearoff=0)
matric_demi_bande.add_command(label="Multiplication_demi_bande supérieur")
Multiplication_matrice_matrice.add_cascade(label="Matrice demi Bande inféreiur ", menu=matric_demi_bande)
mon_Menu.add_cascade(label="Multiplication Matrice Matrice",menu=Multiplication_matrice_matrice)

resolution_systeme_lineaire = Menu(mon_Menu, tearoff=0)

# Méthode directes
methodes_directes = Menu(resolution_systeme_lineaire, tearoff=0)

elimination_gauss = Menu(methodes_directes, tearoff=0)
elimination_gauss.add_command(label="Matrice dense (Symétrique définie positive)")
elimination_gauss.add_command(label="Matrice bande (Symétrique définie positive)")

gauss_jordan = Menu(methodes_directes, tearoff=0)
# ... (Continue adding submenus for Gauss-Jordan)

methodes_directes.add_cascade(label="Méthodes d’élimination de Gauss", menu=elimination_gauss)
methodes_directes.add_cascade(label="Méthode d’élimination de Gauss-Jordan", menu=gauss_jordan)
# ... (Continue adding submenus for other direct methods)

# Méthodes itératives
methodes_iteratives = Menu(resolution_systeme_lineaire, tearoff=0)

jacobi = Menu(methodes_iteratives, tearoff=0)
jacobi.add_command(label="Matrice dense")

gauss_seidel = Menu(methodes_iteratives, tearoff=0)
gauss_seidel.add_command(label="Matrice dense")

methodes_iteratives.add_cascade(label="Méthode de Jacobi", menu=jacobi)
methodes_iteratives.add_cascade(label="Méthode de Gauss-Seidel", menu=gauss_seidel)
# ... (Continue adding submenus for other iterative methods)

resolution_systeme_lineaire.add_cascade(label="Méthodes directes", menu=methodes_directes)
resolution_systeme_lineaire.add_cascade(label="Méthodes itératives", menu=methodes_iteratives)

mon_Menu.add_cascade(label="Résolution d’un système linéaire", menu=resolution_systeme_lineaire)






frame_gestion=Frame(fenetre,bg=font_color,padx=8,pady=8)
frame_gestion.grid(row=0,column=23)
label1 = Label(frame_gestion, text="Gestion des matrices", font=("Cambria", 20, "italic bold"), fg="white", bg=font_color)
label1.grid(row=0,column=3)


#frame_lab2 = Frame(fenetre, padx=5, pady=5)
#frame_lab2.grid(row=4,column=25)
LabeL2 = Label(frame_gestion, text="Choisissez le type de Matrice")
LabeL2.grid(row=3,column=3)



button_multiply = Button(fenetre, text="Matrice Multiplication", command=perform_matrix_multiplication_interface)
button_multiply.grid(row=1, column=0, pady=10)

# Resolution buttons
button_resolution = Button(fenetre, text="Linear System Resolution", command=perform_linear_system_resolution)
button_resolution.grid(row=5, column=0, pady=10)


f.multiplication_matrice_vecteur(f.matrice,f.b)

   



fenetre.config(menu=mon_Menu)

fenetre.mainloop()
