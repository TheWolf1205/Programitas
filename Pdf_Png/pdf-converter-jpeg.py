from wand.image import Image

print("Bienvenido al convertidor de PDF a PNG :3 \n")

nombre_del_pdf = str(input("Digite el nombre del PDF sin la extención: ")+".pdf")
nombre_de_salida = str(input("Digite el nombre de salida del archivo sin la extención: ")+".png")
resolucion = int(input("Digite la resolucion con la que quiere el archivo: "))

# Aquí hago que tome al archivo PDF con la resolución resultante que quiero que quede y lo guardo en la variable imagen
with Image(filename=nombre_del_pdf, resolution= resolucion) as imagen:
    # Aquí le cambio el formato
    imagen.format = 'jpeg'
    # Aquí le pido que la guarde 
    imagen.save(filename=nombre_de_salida)

# Indico que fué exitosa la carga :3
print("La conversión ha sido exitosa :3")
