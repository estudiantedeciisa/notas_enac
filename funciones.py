from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

def Inicio_sesion(pagina):
    
    # Obtén la ruta del directorio actual donde se está ejecutando el script
    directorio_actual = os.path.dirname(__file__)

    # Crea la ruta relativa al archivo driver
    motor_edge = os.path.join(directorio_actual, "msedgedriver.exe")

    # Crea el servicio con la ruta correcta al controlador
    service = Service(motor_edge)

    # Inicia el WebDriver con el servicio
    driver = webdriver.Edge(service=service)
    
    # Abre la página
    driver.get(pagina)
    time.sleep(1)  # Espera para que el usuario vea que la página ha cargado

    # Escribe en el campo con id "logclave"
    clave_input = driver.find_element(by=By.ID, value="logclave") 
    clave_input.send_keys("clave del usuario privada") # Por motivos de seguridad, no puedo compartir la clave

    # Escribe en el campo con id "logrut"
    rut_input = driver.find_element(by=By.ID, value="logrut")
    rut_input.send_keys("rut de profesor") # Por motivos de seguridad, no puedo compartir el rut
    time.sleep(1)  # Espera para que el usuario vea el cambio

    # Pulsa el botón con id "ImageButton1"
    login_button = driver.find_element(by=By.ID, value="ImageButton1")
    login_button.click()
    time.sleep(1)  # Espera para que el usuario vea el clic y el inicio de sesión

    return driver












def buscar_elementos(pagina):
# Localizar la tabla por su id
    table = pagina.find_element(By.ID, "ctl00_ContentPlaceHolder1_Table1")
    celdas = table.find_elements(By.XPATH, ".//td")  # Ajusta el XPath según tu HTML

    carreras = []
    nueva_carrera = []

    for celda in celdas:
        texto_celda = celda.text
        if texto_celda.startswith("Carrera:"):
            # Si encontramos una nueva carrera, guardamos la porción anterior y empezamos una nueva
            if nueva_carrera:
                carreras.append(nueva_carrera.copy())  # Copiamos la lista para evitar referencias
            nueva_carrera = [texto_celda]
        else:
            # Si no es una nueva carrera, agregamos el texto a la porción actual
            nueva_carrera.append(texto_celda)

    # Agregar la última carrera (si existe) a la lista de carreras
    if nueva_carrera:
        carreras.append(nueva_carrera.copy())


    # obtener nombre de carreras
    nombre_carreras=[]
    for i in range(len(carreras)):
        nombre_carreras.append(carreras[i][0])
        nombre_carreras[i] =  f"sec.{carreras[i][5]} {nombre_carreras[i][8:]}. N° alumn: {carreras[i][7]}"

    # Dentro de la tabla, localizar el input con title="Ingreso de notas"
    input_element = table.find_elements(By.XPATH, ".//input[@title='Ingreso de notas']")

    #crear array de inputs
    input_list = []
    for input_element in input_element:
        input_list.append(input_element)

    arreglo_botones=[]
    print("esto es largo: ", len(input_list))
    for i in range(len(input_list)):
        if i % 2 == 0:
            arreglo_botones.append(input_list[i])
            
    input_list = []
    matriz=[nombre_carreras, arreglo_botones]
    print("Input guardado correctamente para su uso posterior.")
    
    return matriz
