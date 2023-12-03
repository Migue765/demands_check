from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome  import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import sqlite3

# Establecer una conexión a la base de datos SQLite
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


def wait_and_send_keys(driver, xpath, keys, wait_time=1):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(keys)


def wait_and_click(driver, xpath, wait_time=1):
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

#Variables de busqueda
field = '76001233300020200108900'
institution = 'TRIBUNAL ADMINISTRATIVO DEL VALLE DEL CAUCA'

# Ejecutar una consulta SQL para obtener el id_samui cuando name coincide
query = "SELECT id_samui FROM institutions WHERE name = ?"
cursor.execute(query, (institution,))

# Obtener el resultado de la consulta
resultado = cursor.fetchone()

# Cerrar la conexión a la base de datos
conn.close()

# Verificar si se encontró un resultado
if resultado is not None:
    id_proceso = field+str(resultado[0])
    url = 'https://samai.consejodeestado.gov.co/Vistas/Casos/list_procesos.aspx?guid='+id_proceso
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')
else:
    print(f"No se encontró ningún resultado para '{nombre_a_buscar}' (not found)")

