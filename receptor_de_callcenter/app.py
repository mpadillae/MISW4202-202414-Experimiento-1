# receptor_de_callcenter.py
from flask import Flask
from celery import Celery
import random

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="callcenter_request", queue="callcenter")
def callcenter_request():
    print("[Receptor call center] Mensaje recibido desde la plataforma de mensajes.")
    print("[Receptor call center] Enviando respuesta a la plataforma de mensajes.")
    platform_callback.delay(get_status())

@celery.task(name="platform_callback", queue="platform")
def platform_callback(response):
    pass

def get_status():
    # Simulando disponibilidad del 90%
    value = random.randint(1, 10)
    if value == 1:
        return "No disponible :("
    else:
        return "Disponible :)"

if __name__ == '__main__':
    app.run(port=5002)
