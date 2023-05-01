import requests
import smtplib
import time
from email.mime.text import MIMEText

# Define la URL de la página a monitorear y el intervalo entre solicitudes
url = "https://www.cursosdev.com/?page=1"
intervalo = 3600  # en segundos (1 hora)

# Define las credenciales SMTP y la dirección de correo electrónico para notificaciones
servidor_smtp = "smtp.outlook.com"
puerto_smtp = 587
usuario_smtp = "rubend1509@outlook.com"
contraseña_smtp = "27006941Carbo"
correo_destino = "cursosdevpruebabot@gmail.com"

# Inicializa la variable contenido_anterior con el contenido de la página al momento de ejecutar el bot
contenido_anterior = requests.get(url).content

while True:
    # Hace una solicitud a la página y obtiene su contenido
    contenido_actual = requests.get(url).content

    # Compara el contenido actual con el anterior. Si hay una actualización, envía un correo electrónico
    if contenido_actual != contenido_anterior:
        asunto = "¡Hay una actualización en CursosDEV!"
        cuerpo = "Se ha detectado una actualización en la página de CursosDEV. ¡Ve a echarle un vistazo!"
        mensaje = MIMEText(cuerpo)
        mensaje['Subject'] = asunto
        mensaje['From'] = usuario_smtp
        mensaje['To'] = correo_destino

        try:
            servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
            servidor.starttls()
            servidor.login(usuario_smtp, contraseña_smtp)
            servidor.sendmail(usuario_smtp, correo_destino, mensaje.as_string())
            servidor.quit()
            print("Se ha enviado una notificación de correo electrónico.")
        except Exception as e:
            print("Ha ocurrido un error al enviar el correo electrónico:", e)

    # Actualiza la variable contenido_anterior y espera el intervalo de tiempo antes de hacer la siguiente solicitud
    contenido_anterior = contenido_actual
    time.sleep(intervalo)
