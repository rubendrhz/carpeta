from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from tabulate import tabulate
import pandas as pd

# Configuración del navegador Edge
options = EdgeOptions()
options.use_chromium = True
options.add_argument("--headless") # Ejecutar en segundo plano sin abrir el navegador
driver = Edge(options=options)

# Cargar la página web
url = "https://cahs.uc.edu/academic-programs/undergraduate-programs/social-work/directory.html"
driver.get(url)

# Obtener los elementos de la tabla
rows = driver.find_elements(By.XPATH, "//table[@id='directoryTable']/tbody/tr")

# Crear una lista vacía para almacenar los datos
data = []

# Iterar por cada fila de la tabla
for row in rows:
    # Obtener el nombre y apellido
    name = row.find_element(By.XPATH, "./td[1]").text.strip()
    first_name, last_name = name.split(" ", 1)
    # Obtener el correo electrónico
    email = row.find_element(By.XPATH, "./td[3]/a").text.strip()
    # Almacenar los datos en la lista
    data.append([first_name, last_name, email])

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(data, columns=["Nombre", "Apellido", "Correo electrónico"])

# Imprimir la tabla utilizando tabulate
print(tabulate(df, headers="keys", tablefmt="grid"))

# Cerrar el navegador
driver.quit()
