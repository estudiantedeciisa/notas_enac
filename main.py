from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from funciones import Inicio_sesion, buscar_elementos
from clases import crear_ventana_cursos, crear_ventana_notas, excel, pregunta

# Abre la página de docentes
pagina_actual=Inicio_sesion("https://docentesnet.enac.cl/")

pagina_actual.get("https://docentesnet.enac.cl/Asignaturas.aspx")
time.sleep(1)

matriz=buscar_elementos(pagina_actual) #scrapear la pagina para obtener los info de los cursos

final = False
while final==False:
    # Crear una instancia de la ventana
    crear_ventana_cursos(matriz) #ventana para elegir que curso rellenar 

    time.sleep(2)

    nota_parcial=crear_ventana_notas() #ventana para decidir que nota modificar

    time.sleep(2)

    salida=False
    while salida==False:

        notas_ingresar = excel() #tomar notas de excel

        for numero in notas_ingresar:
            try:
                input_element = WebDriverWait(pagina_actual, 10).until(
                    EC.element_to_be_clickable((By.XPATH, nota_parcial))
                )
                
                input_element.clear()  # Limpia el valor actual
                input_element.send_keys(numero)
                
                # Simula la tecla Enter
                input_element.send_keys(Keys.RETURN)

            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        
        salida=pregunta("¿Quiere añadir más notas en este curso?")

    pagina_actual.get("https://docentesnet.enac.cl/Asignaturas.aspx")
    final=pregunta("¿Quiere ir a otro curso?")