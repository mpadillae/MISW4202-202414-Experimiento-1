# plataforma_de_mensajes.py
from flask import Flask
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="platform_request", queue="platform")
def platform_request():
    print("[Plataforma de mensajes] Mensaje recibido desde el monitor.")
    print("[Plataforma de mensajes] Reenviando solicitud al receptor de call center.")
    callcenter_request.apply_async()

@celery.task(name="platform_callback", queue="platform")
def platform_callback(response):
    print("[Plataforma de mensajes] Mensaje recibido desde el receptor de call center.")
    print("[Plataforma de mensajes] Enviando respuesta al monitor.")
    monitor_callback.delay(response)

@celery.task(name="callcenter_request", queue="callcenter")
def callcenter_request():
    pass

@celery.task(name="monitor_callback", queue="monitor")
def monitor_callback(response):
    pass


if __name__ == '__main__':
    app.run(port=5001)
