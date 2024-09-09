# receptor_de_callcenter.py
from flask import Flask
from celery import Celery
from datetime import datetime
import random

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="callcenter_request", queue="callcenter")
def callcenter_request():
    write_log.apply_async(("Receptor call center", "Mensaje recibido desde la plataforma de mensajes, enviando respuesta a la plataforma de mensajes.", datetime.now()))
    platform_callback.delay(get_status())


@celery.task(name="platform_callback", queue="platform")
def platform_callback(response):
    pass


@celery.task(name="write_log", queue="logs")
def write_log(component, message, date):
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
