# plataforma_de_mensajes.py
from flask import Flask
from celery import Celery
from datetime import datetime

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="platform_request", queue="platform")
def platform_request():
    write_log.apply_async(("Plataforma de mensajes", "Mensaje recibido desde el monitor, reenviando solicitud al receptor de call center.", datetime.now()))
    callcenter_request.apply_async()

@celery.task(name="platform_callback", queue="platform")
def platform_callback(response):
    write_log.apply_async(("Plataforma de mensajes", "Mensaje recibido desde el receptor de call center, enviando respuesta al monitor.", datetime.now()))
    monitor_callback.delay(response)

@celery.task(name="callcenter_request", queue="callcenter")
def callcenter_request():
    pass

@celery.task(name="monitor_callback", queue="monitor")
def monitor_callback(response):
    pass

@celery.task(name="write_log", queue="logs")
def write_log(component, message, date):
    pass


if __name__ == '__main__':
    app.run(port=5001)
