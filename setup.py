from cx_Freeze import setup, Executable

setup(
    name="Gestion des matrices",
    version="1.0",
    description="Cette application est pour la gestion des matrices",
    executables=[Executable("Gestion-des-matrices.py", base="Win32GUI",icon=r"C:\Users\LENOVO\Gestion-des-matrices\cube.ico")],
)