# monitor.py
from flask import Flask, jsonify
from celery import Celery
from datetime import datetime

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@app.route("/status", methods=["GET"])
def get_status():
    write_log.apply_async(("Monitor", "Solicitud de consulta de estado encolada exitosamente.", datetime.now()))
    platform_request.apply_async()
    return jsonify({"status": "Solicitud de consulta de estado encolada exitosamente."})


@celery.task(name="monitor_callback", queue="monitor")
def monitor_callback(response):
    write_log.apply_async(("Monitor", f"Respuesta recibida desde la plataforma de mensajes, Status - {response}", datetime.now()))


@celery.task(name="platform_request", queue="platform")
def platform_request():
    pass


@celery.task(name="write_log", queue="logs")
def write_log(component, message, date):
    pass


if __name__ == '__main__':
    app.run(port=5000)
