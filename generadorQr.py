#Programar en Python un generador de códigos qr personalizados (tamaño y color definidos por el usuario), el qr debe enlazar a la url de Python.Por Juan Fernandez. Para  programacion V-UBA

#Se importa libreria
import qrcode 
from qrcode import QRCode,constants

tamaño = int(input('Ingresa el tamaño del codigo QR '))
colorcodigo = input('Ingresa el color del codigo QR en Ingles ')
fondocodigo = input('Ingresa el color en ingles del fondo del codigo QR ')


# Crear una instancia de QRCode
qr = QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_Q,
    box_size=tamaño,
    border=4
)

# Agregar datos al código QR
data = "https://www.python.org"
qr.add_data(data)
qr.make(fit=True)

# Obtener la imagen generada
img = qr.make_image(fill_color=colorcodigo, back_color=fondocodigo)

# Guardar la imagen como archivo PNG
img.save("codigoQR.png")
