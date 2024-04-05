import fitz

print("Bienvenido al convertidor de PDF a PNG :3 \n")

nombre_del_pdf = str(input("Digite el nombre del PDF sin la extensión: ")+".pdf")
nombre_de_salida = str(input("Digite el nombre de salida del archivo sin la extensión: ")+".png")
resolucion = int(input("Digite la resolución con la que quiere el archivo: "))

# Abrir el PDF con PyMuPDF
with fitz.open(nombre_del_pdf) as doc:
    # Obtener el tamaño de la página del PDF
    rect = doc[0].rect
    # Crear una nueva página en blanco con el tamaño del PDF
    blank_page = fitz.new_page(width=rect.width, height=rect.height)
    # Copiar el contenido del PDF a la página en blanco
    blank_page.insert_pdf(doc)
    # Guardar la página en blanco como imagen PNG
    blank_page.save(nombre_de_salida, dpi=(resolucion, resolucion))

print("La conversión ha sido exitosa :3")

