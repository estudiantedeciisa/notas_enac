import tkinter as tk

from tkinter import scrolledtext

def crear_ventana_cursos(matriz):
    ventana = tk.Tk()
    ventana.title("Elija su curso")
    ventana.geometry("400x300+100+100")

    for i in range(len(matriz[0])):
        boton = tk.Button(ventana, text=matriz[0][i], command=lambda i=i: boton_pulsado(matriz[1][i]))
        boton.pack(side="top", padx=10, pady=10)

    def boton_pulsado(boton):
        # Aquí puedes implementar la lógica específica para cada botón
        print(f"Botón pulsado: {boton}")
        ventana.destroy()
        boton.click()

    ventana.mainloop()



def crear_ventana_notas():
    ventana = tk.Tk()
    ventana.title("Elija su nota")
    ventana.geometry("400x300+100+100")

    boton=[]

    def boton_pulsado(tipo, boton):
        # Aquí puedes implementar la lógica específica para cada botón
        print(f"Botón pulsado: {tipo}")
        ventana.destroy()
        boton.append(tipo)

    # Crear botones con texto "parcial 1", "parcial 2", etc.
    boton_a = tk.Button(ventana, text="parcial 1", command=lambda: boton_pulsado("//input[@title='PAR 1 20%']", boton))
    boton_b = tk.Button(ventana, text="parcial 2", command=lambda: boton_pulsado("//input[@title='PAR 2 20%']", boton))
    boton_c = tk.Button(ventana, text="parcial 3", command=lambda: boton_pulsado("//input[@title='PAR 3 30%']", boton))
    boton_d = tk.Button(ventana, text="parcial 4", command=lambda: boton_pulsado("//input[@title='PAR 4 30%']", boton))

    # Colocar los botones uno debajo del otro
    boton_a.pack(side="top", padx=10, pady=10)
    boton_b.pack(side="top", padx=10, pady=10)
    boton_c.pack(side="top", padx=10, pady=10)
    boton_d.pack(side="top", padx=10, pady=10)

    ventana.mainloop()
    return boton[0]



def excel():
    def obtener_datos(tabla):
        # Obtener el contenido pegado en el cuadro de texto
        contenido = cuadro_texto.get("1.0", tk.END)

        # Dividir el contenido por líneas (asumiendo que cada línea es una fila)
        fila = contenido.splitlines()

        # Crear una lista para almacenar los datos
        fila_sin_espacios = list(filter(lambda palabra: palabra != "", fila))

        #iterar
        for fila in fila_sin_espacios:
            fila = fila.replace(",", ".")  # Reemplazar comas por puntos
            tabla.append(float(fila))

        ventana.destroy()
    

    tabla=[]
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Pegar datos de Excel")

    # Crear un cuadro de texto para pegar los datos
    cuadro_texto = scrolledtext.ScrolledText(ventana, width=80, height=20)
    cuadro_texto.pack(padx=10, pady=10)

    # Botón para obtener los datos pegados
    boton_obtener = tk.Button(ventana, text="Obtener datos", command=lambda: obtener_datos(tabla))
    boton_obtener.pack(pady=10)

    # Ejecutar la aplicación
    ventana.mainloop()
    return tabla

    

def pregunta(pregunta):
    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("¿Agregar más notas?")
    ventana.geometry("300x300+100+100")

    # Función para manejar el botón "Sí"
    def opcion_si(valor):
        ventana.destroy()  # Cierra la ventana
        valor.append(False)

    # Función para manejar el botón "No"
    def opcion_no(valor):
        ventana.destroy()  # Cierra la ventana
        valor.append(True)


    valor=[]

    # Etiqueta con el mensaje
    etiqueta = tk.Label(ventana, text=pregunta)
    etiqueta.pack()

    # Botones
    boton_si = tk.Button(ventana, text="Sí", command=lambda: opcion_si(valor))
    boton_si.pack()

    boton_no = tk.Button(ventana, text="No", command=lambda: opcion_no(valor))
    boton_no.pack()

    # Ejecutar la ventana
    ventana.mainloop()
    return valor[0]

