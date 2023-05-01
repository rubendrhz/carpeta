import time
from selenium.webdriver.edge.service import Service


# Configuración del driver de Edge
driver = webdriver.Edge('ruta_al_controlador/msedgedriver.exe')


# Navegar a la página web
driver.get("https://cahs.uc.edu/academic-programs/undergraduate-programs/social-work/directory.html")

# Esperar a que cargue la página web
time.sleep(3)

# Encontrar todas las filas de la tabla
filas = driver.find_elements_by_css_selector(".tableizer-firstrow")
filas += driver.find_elements_by_class_name("tableizer-row")

# Crear listas para guardar nombres y correos
nombres = []
correos = []

# Iterar sobre las filas y extraer nombres y correos
for fila in filas:
    columnas = fila.find_elements_by_tag_name("td")
    nombre = columnas[0].text.strip()
    correo = columnas[1].text.strip()
    nombres.append(nombre)
    correos.append(correo)

# Mostrar las listas en la terminal
print("Lista de nombres:")
print(nombres)
print("Lista de correos:")
print(correos)

# Cerrar el navegador
driver.quit()

