import subprocess

def convertir_djvu_a_pdf(archivo_djvu, archivo_pdf):
    subprocess.run(["ddjvu", "-format=pdf", "-quality=85", archivo_djvu, archivo_pdf])

# Ejemplo de uso
archivo_djvu = "1.djvu"
archivo_pdf = "1.pdf"
convertir_djvu_a_pdf(archivo_djvu, archivo_pdf)

