import threading
import logging
from concatenacion import concatenar_horizontal
from archivos import escribir_imagen
from api import PixabayAPI
from PIL import Image


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = '/home/concurrente/concurrente/python-manipulando-imagenes-Pepitalapistolera/imagenes'
query = input(f"Que imagenes necesita? \n")
cuantas = int (input(f"cuantas imagenes quiere? \n"))
api = PixabayAPI('15310684-221a6950fdb7fd2822d3b4b82', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cuantas)

for u in urls:
  #t = threading.Thread(target=api.descargar_imagen, args=[u])
  api.descargar_imagen(u)
  logging.info(f'Descargando {u}')
  #t.start()

#lista = api.lista_rutas
def leer_imagen3(ruta):
  return Image.open(ruta)

print(api.lista_rutas)
for i in range(0,len(api.devolver_lista())-1):
  imagen1 = api.lista_rutas[i]
  imagen2 = api.lista_rutas[i+1]
  escribir_imagen('concatenada-horizontal.jpg', concatenar_horizontal([leer_imagen3(imagen1),leer_imagen3(imagen2)]))
  
